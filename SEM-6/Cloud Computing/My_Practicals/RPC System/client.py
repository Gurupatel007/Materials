# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:54 2024

@author: gurup
"""

import Pyro4

uri = input("Enter the URI of the remote object: ")
calculator = Pyro4.Proxy(uri)  # Get a proxy to the remote object

print("\nWelcome to the calculator with add and subtract features.")
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

print("The result of addition is:", calculator.add(x, y))
print("The result of subtraction is:", calculator.subtract(x, y))

