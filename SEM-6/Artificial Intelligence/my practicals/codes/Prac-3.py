# enum, eq, lt, cnp, gt, repr   

from enum import Enum

class actions(Enum):
    moveUp = -3
    moveDown = +3
    moveLeft = -1
    moveRight = +1

class Node:
    def __init__(self,puzzle_list,parent,action):
        self.puzzle_list = puzzle_list
        self.parent = parent
        self.action = action
        if self.parent != None:
            self.g = self.parent.g+1
        else:
            self.g = 0
            self.f = 0
    def __eq__(self, __value: object) -> bool:
        pass
    def __lt__():
        pass
    def apply_action(self,action,index_Zero):
        if action == moveUp:
            if index_Zero not in [0,1,2]:
                swap(index_Zero,index_Zero-3)

"""
from enum import Enum

class actions(Enum):
    moveUp = -3
    moveDown = +3
    moveLeft = -1
    moveRight = +1

class Node:
    def __init__(self, puzzle_list, parent, action):
        self.puzzle_list = puzzle_list
        self.parent = parent
        self.action = action
        if self.parent != None:
            self.g = self.parent.g + 1
        else:
            self.g = 0
            self.f = 0

    def __eq__(self, other):
        return self.puzzle_list == other.puzzle_list

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return "Node({})".format(self.puzzle_list)

    def apply_action(self, action, index_Zero):
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Define your goal state here

        if self.puzzle_list == goal_state:
            return  # Do not apply any action if the current state is the goal state

        if action == actions.moveUp:
            if index_Zero not in [0, 1, 2]:
                self.swap(index_Zero, index_Zero - 3)
        elif action == actions.moveDown:
            if index_Zero not in [6, 7, 8]:
                self.swap(index_Zero, index_Zero + 3)
        elif action == actions.moveLeft:
            if index_Zero not in [0, 3, 6]:
                self.swap(index_Zero, index_Zero - 1)
        elif action == actions.moveRight:
            if index_Zero not in [2, 5, 8]:
                self.swap(index_Zero, index_Zero + 1)

    def swap(self, i, j):
        self.puzzle_list[i], self.puzzle_list[j] = self.puzzle_list[j], self.puzzle_list[i]

"""

