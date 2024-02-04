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
        parent.children.append(child_node)
        return child_node

obj_amit = Node("amit",[],None)
tree = Tree(obj_amit)
obj_rahul = tree.insert_node("rahul", obj_amit)
obj_sanjay = tree.insert_node("sanjay", obj_rahul)
        