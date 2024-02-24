# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:27:38 2024

@author: gurup
"""
class Node:
    def __init__(self,name,children,parent):
        self.name = name
        self.children = children
        self.parent = parent

class Tree:
    def __init__(self,root):
        self.root = root
    
    def insert_node(self,name,parent):
        child_node = Node(name,[],parent)
        #parent.children.append(child_node)
        #return child_node
        if parent is None:
            self.root = child_node
        else:
            parent.children.append(child_node)
        return child_node

obj_amit = Node("amit",[],None)
tree = Tree(obj_amit)
#child of amit
obj_rahul = tree.insert_node("rahul", obj_amit)
obj_priya = tree.insert_node("priya", obj_amit)

#child of rahul
obj_sanjay = tree.insert_node("sanjay", obj_rahul)
obj_ravi = tree.insert_node("ravi", obj_rahul)

#child of priya
obj_nisha = tree.insert_node("nisha", obj_priya)
obj_claire = tree.insert_node("claire", obj_priya)

#child ofsanjay
obj_deepak = tree.insert_node("deepak", obj_sanjay)
obj_raj = tree.insert_node("raj", obj_sanjay)
obj_suresh = tree.insert_node("suresh", obj_sanjay)

#child of ravi


#child of nisha
obj_lisa = tree.insert_node("lisa", obj_nisha)

#child of claire
obj_eric = tree.insert_node("eric", obj_claire)

#child of deepak
obj_vinay = tree.insert_node("vinay", obj_deepak)
obj_akash = tree.insert_node("akash", obj_deepak)

#child of raj
obj_gaurav = tree.insert_node("gaurav", obj_raj)

#child of suresh
obj_meena = tree.insert_node("meena", obj_suresh)

#child of lisa
obj_sam = tree.insert_node("sam", obj_lisa)
obj_john= tree.insert_node("john", obj_lisa)

#child of vinay
obj_ankit = tree.insert_node("ankit", obj_vinay)
obj_harsh = tree.insert_node("harsh", obj_vinay)

#child of gaurav
obj_aditya = tree.insert_node("aditya", obj_gaurav)
obj_sneha = tree.insert_node("sneha", obj_gaurav)
obj_alice = tree.insert_node("alice", obj_gaurav)

#child of meena
obj_reena = tree.insert_node("reena", obj_meena)

#child of ankit
obj_abhishek = tree.insert_node("abhishek", obj_ankit)

#child of harsh
obj_puneet = tree.insert_node("puneet", obj_harsh)
obj_vikas = tree.insert_node("vikas", obj_harsh)
obj_varun = tree.insert_node("varun", obj_harsh)

#child of sneha
obj_anjali = tree.insert_node("anjali", obj_sneha)
obj_arjun = tree.insert_node("arjun", obj_sneha)

#child of alice
obj_carol = tree.insert_node("carol", obj_alice)
obj_dave = tree.insert_node("dave", obj_alice)

#child of abhishek
obj_rohan = tree.insert_node("rohan", obj_abhishek)
obj_ajay = tree.insert_node("ajay", obj_abhishek)

#child of anjali
obj_nidhi = tree.insert_node("nidhi", obj_anjali)

#child of arjun
obj_sachin = tree.insert_node("sachin", obj_arjun)
obj_sumit = tree.insert_node("sumit", obj_arjun)

#child of rohan
obj_aruna = tree.insert_node("aruna", obj_rohan)
obj_ramji = tree.insert_node("ramji", obj_rohan)

#child of ajay
obj_virat = tree.insert_node("virat", obj_ajay)
obj_isha = tree.insert_node("isha", obj_ajay)

#child of nidhi
obj_prem = tree.insert_node("prem", obj_nidhi)
obj_lina = tree.insert_node("lina", obj_nidhi)


def print_path(node):
    r_list=[]
    while(node!=None):
        r_list.append(node.name)
        node = node.parent
    reverse_list= r_list[::-1]
    print("Path: ",'->'.join(reverse_list))
    print("cost: ",(len(reverse_list)-1))
    
def bfs_search(tree,search_string):
    queue = [tree.root]
    while(len(queue)!=0):
        pop_node = queue.pop(0)
        if(pop_node.name==search_string):
            return pop_node
        queue.extend(pop_node.children)
    return None


'''
print(tree.root.name)  # Output: amit
print(tree.root.children[0].name)  # Output: rahul
print(tree.root.children[0].children[0].name)  # Output: sanjay
'''
search_string = input("Enter the search string: ")
result = bfs_search(tree, search_string) 
if(result!=None):
    print_path(result)
else:
    print(search_string+" is not available in the tree")