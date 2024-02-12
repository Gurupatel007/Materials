# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:34 2024

@author: gurup
"""

import Pyro4
from remote_object import Calculator

def start_server():
    # Register the Calculator class as a Pyro object
    daemon = Pyro4.Daemon()                # Make a Pyro daemon
    uri = daemon.register(Calculator)      # Register the Calculator as a Pyro object
    ns = Pyro4.locateNS()                  # Find the name server
    ns.register("example.calculator", uri)  # Register the object with a name in the name server
    
    print("Ready. Object uri =", uri)
    daemon.requestLoop()                   # Start the loop

if __name__ == "__main__":
    start_server()
