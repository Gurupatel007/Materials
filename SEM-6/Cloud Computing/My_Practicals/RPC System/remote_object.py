# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:30:04 2024

@author: gurup
"""

import Pyro4

@Pyro4.expose
class Calculator(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
