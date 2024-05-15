from enum import Enum

class Actions(Enum):
    moveUp = -3
    moveDown = 3
    moveLeft = -1
    moveRight = 1

class Node:
    def __init__(self, puzzle_list, parent, action):
        self.puzzle_list = puzzle_list
        self.parent = parent
        self.action = action
        # self.g = parent.g + 1 if parent else 0
        # self.h = 0
        # self.f = self.g + self.h
        if self.parent != None:
            self.g = self.parent.g + 1
        else:
            self.g = 0
            self.f = 0

    def generateAllSuccesor(self, goal_state):
        index_Zero = self.puzzle_list.index(0)
        child_list = []
        for action in Actions:
            new_puzzle_list = self.puzzle_list[:]
            if self.apply_action(action, index_Zero, new_puzzle_list, goal_state) is not None:
                child_node = Node(new_puzzle_list, self, action)
                child_list.append(child_node)
        return child_list

    def __eq__(self, other):
        if other is None:
            return False
        return self.puzzle_list == other.puzzle_list

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return "Node({})".format(self.puzzle_list)

    def apply_action(self, action, index_Zero, puzzle_list, goal_state):
        if puzzle_list == goal_state:
            return  # Do not apply any action if the current state is the goal state

        if action == Actions.moveUp and index_Zero not in [0, 1, 2]:
            self.swap(index_Zero, index_Zero - 3, puzzle_list)
            return True
        elif action == Actions.moveDown and index_Zero not in [6, 7, 8]:
            self.swap(index_Zero, index_Zero + 3, puzzle_list)
            return True
        elif action == Actions.moveLeft and index_Zero not in [0, 3, 6]:
            self.swap(index_Zero, index_Zero - 1, puzzle_list)
            return True
        elif action == Actions.moveRight and index_Zero not in [2, 5, 8]:
            self.swap(index_Zero, index_Zero + 1, puzzle_list)
            return True
        return False

    def swap(self, i, j, puzzle_list):
        puzzle_list[i], puzzle_list[j] = puzzle_list[j], puzzle_list[i]

class AstarSearch:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state.puzzle_list  # Expect a Node, but use its puzzle list for comparisons
        self.openlist = [initial_state]
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
                if child not in self.openlist and child not in self.closelist:
                    self.openlist.append(child)
                elif child in self.openlist:
                    index = self.openlist.index(child)
                    if child.f < self.openlist[index].f:
                        self.openlist[index] = child
        return None

def main():
    initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_node = Node(initial_state, None, None)
    goal_node = Node(goal_state, None, None)
    astar = AstarSearch(initial_node, goal_node)
    result = astar.perform_algorithm()
    if result is None:
        print("No solution found")
    else:
        print("Solution found")
        print(result.puzzle_list)

main()
