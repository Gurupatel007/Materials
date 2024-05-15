class Node:
  def __init__(self,x,y,parent):
    self.x = x
    self.y = y
    self.parent = parent

  def apply_action(self,rule_no,w):
    x = self.x
    y = self.y

    if rule_no==1:
      if x < w.maxjug1:
        x = w.maxjug1
      else:
        return None

    elif rule_no==2:
      if y < w.maxjug2:
        y = w.maxjug2
      else:
        return None

    elif rule_no==3:
      if x > 0:
        x = 0
      else:
        return None

    elif rule_no==4:
      if y > 0:
        y = 0
      else:
        return None

    elif rule_no==5:
      if 0 < x+y >= w.maxjug1 and y > 0:
        x = w.maxjug1
        y = y-(w.maxjug1-x)
      else:
        return None

    elif rule_no==6:
      if 0 < x+y >= w.maxjug2 and x > 0:
        x = x-(w.maxjug2-y)
        y = w.maxjug2
      else:
        return None

    elif rule_no==7:
      if 0 < x+y <= w.maxjug1 and y >= 0:
        x = x+y
        y = 0
      else:
        return None

    elif rule_no==8:
      if 0 < x+y <= w.maxjug2 and x >= 0:
        y = x+y
        x = 0
      else:
        return None


    if(x==self.x and y==self.y):
      return None
    return Node(x,y,self)

  def __repr__(self):
    return "("+str(self.x)+","+str(self.y)+")"

  def generateAllsuccesor(self,w):
    child_list=[]
    for rule_no in range(1,9):
      result = self.apply_action(rule_no,w)
      if(result != None):
        child_list.append(result)
    return child_list

class waterjug:
  def __init__(self,maxjug1,maxjug2,goal_state):
    self.maxjug1 = maxjug1
    self.maxjug2 = maxjug2
    self.goal_state = goal_state

class bfs_search:
  def __init__(self,initial_state,w):
    self.initial_state = initial_state
    self.w = w

  def execution(self):
    queue = [self.initial_state]
    while(len(queue) != 0):
      current_node = queue.pop(0)
    #   print("Current Node: ",current_node,", Goal State: ",self.w.goal_state)
      if current_node.x == self.w.goal_state.x and current_node.y == self.w.goal_state.y:
        return current_node
      queue.extend(current_node.generateAllsuccesor(self.w))
    return None

def print_path(node):
    r_list=[]
    while(node!=None):
        r_list.append(repr(node));
        node = node.parent
    reverse_list= r_list[::-1]
    print("Path: ",'->'.join(reverse_list));
    print("cost: ",len(reverse_list)-1)


maxjug1 = int(input("Enter the max value of jug1: "))
maxjug2 = int(input("Enter the max value of jug2: "))
goal_state_x = int(input("Enter the goal state of jug1: "))
# goal_state_y = int(input("Enter the goal state of jug2: "))

if maxjug1 <= 0 or maxjug2 <= 0 or goal_state_x <= 0:
    print("Please enter a positive value.")
elif maxjug1 == 1:
    print("The maxjug1 value can't be 1")

# w = waterjug(maxjug1, maxjug2, Node(goal_state_x, 0, None))
# initial_state = Node(0, 0, None)
# bfs = bfs_search(initial_state, w)
# result_node = bfs.execution()
# print_path(result_node)
    
if maxjug1 <= 0 or maxjug2 <= 0:
    print("Jug capacities must be positive values.")
elif goal_state_x < 0 or goal_state_x > maxjug1:# or goal_state_y < 0 or goal_state_y > maxjug2:
    print("Please enter valid goal states for jugs that do not exceed their capacities and are non-negative.")
elif maxjug1 == 1:
    print("The maxjug1 value can't be 1")
else:
    w = waterjug(maxjug1, maxjug2, Node(goal_state_x, 0, None))
    initial_state = Node(0, 0, None)
    bfs = bfs_search(initial_state, w)
    result_node = bfs.execution()
    if result_node:
        print("Solution Found\n")
        print_path(result_node)
    else:
        print("No solution found.")


# for goalstate of maxjug2 uncomment below code and comment above code
""""
if maxjug1 <= 0 or maxjug2 <= 0:
    print("Jug capacities must be positive values.")
elif goal_state_x < 0 or goal_state_x > maxjug1:# or goal_state_y < 0 or goal_state_y > maxjug2:
    print("Please enter valid goal states for jugs that do not exceed their capacities and are non-negative.")
else:
    w = waterjug(maxjug1, maxjug2, Node(goal_state_x, goal_state_y, None))
    initial_state = Node(0, 0, None)
    bfs = bfs_search(initial_state, w)
    result_node = bfs.execution()
    if result_node:
        print_path(result_node)
    else:
        print("No solution found.")
"""