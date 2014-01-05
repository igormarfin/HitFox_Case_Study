__all__ = ['Edge','Node', 'Path', 'Graph', 'ProblemB' , 'main', 'suite' ]

# deprecated to keep older scripts who import this from breaking

from Edge import Edge
from Node import Node
from Path import Path
from Graph import Graph
#from Graph import suite
from ProblemB import ProblemB
from ProblemB import main


def suite():
    import unittest
    import doctest
    import Graph 
    suite = unittest.TestSuite()
    suite.addTests(Graph.suite())
    return suite

