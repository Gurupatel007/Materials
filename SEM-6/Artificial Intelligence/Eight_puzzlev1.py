# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:47:02 2024

@author: Dr.Devang.S.Pandya
"""

from enum import Enum
import time
class Action(Enum):
    MoveUp = 1
    MoveDown = 2
    MoveLeft = 3
    MoveRight = 4
    NoAction = 5
# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position=[], parent=None,action = Action.NoAction):
        self.position = position
        self.parent = parent
        self.action = action
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        strAction = ""
        if(self.action != Action.NoAction):
            strAction = self.action


        return '\n'.join([
        str(strAction),
        str(self.position[:3]),
        str(self.position[3:6]),
        str(self.position[6:9])
        ]).replace('[', '').replace(']', '').replace(',', '').replace('0', '_')


    def generate_a_star_heuristic_value(self,goal):
        self.h = sum([1 if self.position[i] != goal[i] else 0 for i in range(8)])
        self.f = self.depth + self.h
    def get_all_successors(self):
        successors = []
        i = self.position.index(0)
        #Move Down
        if i in [3, 4, 5, 6, 7, 8]:
          new_board = self.position[:]
          new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
          successors.append( Node(new_board, self,Action.MoveDown))
        #Move Right
        if i in [1, 2, 4, 5, 7, 8]:
          new_board = self.position[:]
          new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
          successors.append( Node(new_board, self,Action.MoveRight))
        #Move left
        if i in [0, 1, 3, 4, 6, 7]:
          new_board = self.position[:]
          print(self.position[:])
          new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
          print(new_board)
          successors.append( Node(new_board, self,Action.MoveLeft))
        #Move Up
        if i in [0, 1, 2, 3, 4, 5]:
          new_board = self.position[:]
          new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
          successors.append( Node(new_board, self,Action.MoveUp))
        return successors
class AstarSearch:
  def __init__(self,initial_node, goal_node):
      # Create a start node and an goal node
      self.initial_node = Node(initial_node, None)
      # Create lists for open nodes and closed nodes
      # Add the initial node
      self.open = [self.initial_node]
      self.closed = []
      self.goal_node = Node(goal_node, None)
      self.execution()
  def __repr__(self):
    return ""
  def get_path(self,current_node):
    path = []
    while current_node != self.initial_node:
      path.append(str(current_node))
      current_node = current_node.parent
    path.append(str(self.initial_node))
    # Return reversed path
    return path[::-1]
  # Best-first search Execution: return Shortest Path otherwise None
  def perform_algorithm(self):
      # Loop until the open list is empty
      while len(self.open) > 0:
          # Sort the open list to get the node with the lowest cost first
          self.open.sort()
          # Get the node with the lowest cost
          current_node = self.open.pop(0)
          # Add the current node to the closed list
          self.closed.append(current_node)
          # Check if we have reached the goal, return the path
          if current_node == self.goal_node:
              return current_node
          # Get allSuccesors (Successors)
          allSuccesors = current_node.get_all_successors()
          # Calculate function f = g + h
          self.calculate_evaluation_fx_value(allSuccesors)
          # Loop allSuccesors
          for successor in allSuccesors:
            # Check if the successor is in the closed list and open list
            if not self.is_in_closed(successor) and not self.is_in_open(successor):
              # Everything is green, add successor to open list
              self.open.append(successor)
      # Return None, no path is found
      return None
  def calculate_evaluation_fx_value(self,allSuccesors):
    # Loop allSuccesors
      for successor in allSuccesors:
        # Calculate function f = g + h
        successor.generate_a_star_heuristic_value(self.goal_node.position)
  def is_in_closed(self,successor):
    return successor in self.closed
  
  # Check if a successor should be added to open list
  def is_in_open(self,successor):
      for node in self.open:
          #found successor in Open list
          if successor == node:
            #if successor is better than node then remove node from open list
            if successor.f < node.f:
                self.open.remove(node)
                return False
            else:
              return True
      return False
  def execution(self):
      start_time = time.time_ns()
      result_node = self.perform_algorithm()
      end_time = time.time_ns()
      path = self.get_path(result_node)
      print('\n'.join(path))
      print('Total Performed Move: {0}'.format(len(path)-1))
      print("Execution Time= ",convert_duration_from_nanoseconds(end_time-start_time))
      print()
def convert_duration_from_nanoseconds(total_nanoseconds):
    seconds, remaining_ns = divmod(total_nanoseconds, 1e9)
    minutes, seconds = divmod(seconds, 60)
    milliseconds, remaining_ns = divmod(remaining_ns, 1e6)
    microseconds, remaining_ns = divmod(remaining_ns, 1e3)


    result = ""
    if minutes: result += f"{int(minutes)} minute{'s' if minutes > 1 else ''} "
    if seconds: result += f"{int(seconds)} second{'s' if seconds > 1 else ''} "
    if milliseconds: result += f"{int(milliseconds)} millisecond{'s' if milliseconds > 1 else ''} "
    if microseconds: result += f"{int(microseconds)} microsecond{'s' if microseconds > 1 else ''} "
    if remaining_ns: result += f"{int(remaining_ns)} nanosecond{'s' if remaining_ns > 1 else ''} "


    return result.strip()


#start = [1, 7, 4, 6, 8, 3, 2, 5, 0]
#initial = [3, 0, 7, 2, 8, 1, 6, 4, 5]
#initial = [1, 2, 3, 4, 0, 5, 7, 8, 6]
#initial = [2, 8, 3, 1, 6, 4, 7, 0, 5]
#goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]


AstarSearch(initial_node=[1, 2, 3, 0, 4, 6, 7, 5, 8],
            goal_node=[1, 2, 3, 4, 5, 6, 7, 8, 0])
# AstarSearch(initial_node=[3, 0, 7, 2, 8, 1, 6, 4, 5],
#             goal_node=[1, 2, 3, 8, 0, 4, 7, 6, 5])
