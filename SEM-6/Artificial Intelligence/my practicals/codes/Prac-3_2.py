from enum import Enum

class actions(Enum):
    moveUp = -3
    moveDown = +3
    moveLeft = -1
    moveRight = +1

class Node:
    def __init__(self, puzzle_list, parent, action):
        self.puzzle_list = puzzle_list.copy()  # Copy the list to avoid reference issues
        self.parent = parent
        self.action = action
        if self.parent:
            self.g = self.parent.g + 1
        else:
            self.g = 0
        self.h = 0  # Placeholder for heuristic value
        self.CalculateFvalue()

    def generateAllSuccesor(self, goal_state):
        index_Zero = self.puzzle_list.index(0)
        child_list = []
        for action in actions:
            new_puzzle_list = self.puzzle_list.copy()  # Work on a copy of the puzzle list
            if self.apply_action(action, index_Zero, new_puzzle_list):
                child_node = Node(new_puzzle_list, self, action)
                child_list.append(child_node)
        return child_list

    def CalculateFvalue(self):
        self.f = self.g + self.h

    def __eq__(self, other):
        return isinstance(other, Node) and self.puzzle_list == other.puzzle_list

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return "Node({})".format(self.puzzle_list)

    def apply_action(self, action, index_Zero, puzzle_list):
        if action == actions.moveUp and index_Zero not in [0, 1, 2]:
            puzzle_list[index_Zero], puzzle_list[index_Zero - 3] = puzzle_list[index_Zero - 3], puzzle_list[index_Zero]
            return True
        elif action == actions.moveDown and index_Zero not in [6, 7, 8]:
            puzzle_list[index_Zero], puzzle_list[index_Zero + 3] = puzzle_list[index_Zero + 3], puzzle_list[index_Zero]
            return True
        elif action == actions.moveLeft and index_Zero not in [0, 3, 6]:
            puzzle_list[index_Zero], puzzle_list[index_Zero - 1] = puzzle_list[index_Zero - 1], puzzle_list[index_Zero]
            return True
        elif action == actions.moveRight and index_Zero not in [2, 5, 8]:
            puzzle_list[index_Zero], puzzle_list[index_Zero + 1] = puzzle_list[index_Zero + 1], puzzle_list[index_Zero]
            return True
        return False

class AstarSearch:
    def __init__(self, initial_node, goal_state):
        self.goal_state = goal_state
        self.openlist = [initial_node]
        self.closelist = []

    def perform_algorithm(self):
        while self.openlist:
            self.openlist.sort()
            current_node = self.openlist.pop(0)
            self.closelist.append(current_node)
            if current_node.puzzle_list == self.goal_state:
                return current_node
            child_list = current_node.generateAllSuccesor(self.goal_state)
            for child in child_list:
                child.CalculateFvalue()
                if child not in self.openlist and child not in self.closelist:
                    self.openlist.append(child)
        return None    

def print_puzzle(puzzle_list):
    for i in range(0, 9, 3):
        print(puzzle_list[i:i+3])
    print()  # For better spacing

def main():
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_node = Node(initial_state, None, None)
    astar = AstarSearch(initial_node, goal_state)
    result = astar.perform_algorithm()

    if result:
        print("Solution found")
        path = []
        actions_taken = []
        while result:
            path.insert(0, result.puzzle_list)
            if result.action:
                actions_taken.insert(0, result.action)
            result = result.parent
        
        for i, state in enumerate(path):
            print_puzzle(state)
            if i < len(actions_taken):
                print(f"Action: {actions_taken[i].name}")
    else:
        print("No solution found")

main()