# # enum, eq, lt, cnp, gt, repr   

# # from enum import Enum

# # class actions(Enum):
# #     moveUp = -3
# #     moveDown = +3
# #     moveLeft = -1
# #     moveRight = +1

# # class Node:
# #     def __init__(self,puzzle_list,parent,action):
# #         self.puzzle_list = puzzle_list
# #         self.parent = parent
# #         self.action = action
# #         if self.parent != None:
# #             self.g = self.parent.g+1
# #         else:
# #             self.g = 0
# #             self.f = 0
# #     def __eq__(self, __value: object) -> bool:
# #         pass
# #     def __lt__():
# #         pass
# #     def apply_action(self,action,index_Zero):
# #         if action == moveUp:
# #             if index_Zero not in [0,1,2]:
# #                 swap(index_Zero,index_Zero-3)


# from enum import Enum

# class actions(Enum):
#     moveUp = -3
#     moveDown = +3
#     moveLeft = -1
#     moveRight = +1

# class Node:
#     def __init__(self, puzzle_list, parent, action):
#         self.puzzle_list = puzzle_list
#         self.parent = parent
#         self.action = action
#         if self.parent:
#             self.g = self.parent.g + 1
#         else:
#             self.g = 0
#             self.f = 0  # Initially set f to 0 if there's no parent
#         self.h = 0  # Placeholder for heuristic calculation
#         self.CalculateFvalue() 

#     def generateAllSuccesor(self,goal_state):
#         index_Zero = self.puzzle_list.index(0)
#         child_list = []
#         for action in actions:
#             if self.apply_action(action, index_Zero,goal_state) != None:
#                 child_node = Node(self.puzzle_list, self, action)
#                 child_list.append(child_node)
#                 self.apply_action(action, index_Zero,goal_state)
#         return child_list

#     def CalculateFvalue(self):
#         self.f = self.g + self.h

#     def __eq__(self, other):
#         # if other is None:
#         #     return False
#         # return self.puzzle_list == other.puzzle_list
#         def __eq__(self, other):
#             if other is None:
#                 return False
#             if isinstance(other, list):
#                 return self.puzzle_list == other
#             if isinstance(other, Node):
#                 return self.puzzle_list == other.puzzle_list
#             return False

#     def __lt__(self, other):
#         return self.f < other.f

#     def __repr__(self):
#         return "Node({})".format(self.puzzle_list)

#     def apply_action(self, action, index_Zero,goal_state):
#         # goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Define your goal state here

#         if self.puzzle_list == goal_state:
#             return  # Do not apply any action if the current state is the goal state

#         if action == actions.moveUp:
#             if index_Zero not in [0, 1, 2]:
#                 self.swap(index_Zero, index_Zero - 3)
#                 return True
#         elif action == actions.moveDown:
#             if index_Zero not in [6, 7, 8]:
#                 self.swap(index_Zero, index_Zero + 3)
#                 return True
#         elif action == actions.moveLeft:
#             if index_Zero not in [0, 3, 6]:
#                 self.swap(index_Zero, index_Zero - 1)
#                 return True
#         elif action == actions.moveRight:
#             if index_Zero not in [2, 5, 8]:
#                 self.swap(index_Zero, index_Zero + 1)
#                 return True
#         return False

#     def swap(self, i, j):
#         self.puzzle_list[i], self.puzzle_list[j] = self.puzzle_list[j], self.puzzle_list[i]

# class AstarSearch:
#     def __init__(self,initial_state ,goal_state):
#         self.goal_state = goal_state
#         self.openlist = [initial_state]
#         self.closelist = []

#     def perform_algorithm(self):
#         while len(self.openlist)!=0: 
#             self.openlist.sort()
#             current_node = self.openlist.pop(0)
#             self.closelist.append(current_node)
#             if current_node == self.goal_state:
#                 return current_node
#             child_list = current_node.generateAllSuccesor(self.goal_state)
#             for child in child_list:
#                 child.CalculateFvalue()
#                 if child not in self.openlist and child not in self.closelist:
#                     self.openlist.append(child)
#                 elif child in self.openlist:
#                     index = self.openlist.index(child)
#                     # self.openlist[index] = child
#                     if child.f < self.openlist[index].f:
#                         self.openlist[index] = child
#         return None    
        
# def main():
#     initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Define your initial state here
#     goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Define your goal state here
#     initial_node = Node(initial_state, None, None)
#     goal_node = Node(goal_state, None, None)
#     astar = AstarSearch(initial_node, goal_node)
#     result = astar.perform_algorithm()
#     if result == None:
#         print("No solution found")
#     else:
#         print("Solution found")
#         print(result.puzzle_list)
#         print(result.g)
#         print(result.f)
#         print(result.action)
#         print(result.parent)
#         print(result)
#         print(result.__repr__())
#         print(result.__lt__(result))
#         print(result.__eq__(result))

# # if __name__ == "__main__":
# main()

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
        self.h = 0  # Heuristic value placeholder
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
        # Heuristic (h) calculation is missing here. It needs to be implemented for A* to work properly.
        # Currently, it's using a placeholder value (0), which effectively turns this into Dijkstra's algorithm.
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

def main():
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_node = Node(initial_state, None, None)
    astar = AstarSearch(initial_node, goal_state)
    result = astar.perform_algorithm()

    if result:
        print("Solution found")
        actions_taken = []
        while result:
            if result.action:
                actions_taken.append(result.action.name)
            result = result.parent
        print("Actions:", list(reversed(actions_taken)))
    else:
        print("No solution found")

main()
