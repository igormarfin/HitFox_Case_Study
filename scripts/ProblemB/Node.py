#! /usr/bin/env python

"""
This is the Node  class to  represent Nodes connected by an edge:

  " Node_orig->Edge->Node_taarget "

To test the class :

       ./%prog --test  --debug


"""

__author__ =  'Igor Marfin'
__copyright__ = "Copyright 2013, DESY HiggsGroup"
__credits__ = ["Igor Marfin", "DESY HiggsGroup"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Igor Marfin"
__email__ = "marfin@mail.desy.de"
__status__ = "Test"


# import all modules which might be useful 


import time
import os
import sys
import commands
import re
from optparse import OptionParser

import types
import math
import unittest
import logging
import inspect
import random
import Edge

parser2=OptionParser(usage=__doc__)

parser2.disable_interspersed_args()

parser2.add_option("--test",dest="test",help="to perform test of helper classes",default=False,action="store_true")
parser2.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser2.add_option("--tkinter",dest="tkinter",help="to make a Tkinter window",default=False,action="store_true")



if ("pydoc" in str(sys.argv)): parser2.add_option("-w",dest="none",default=False,action="store_true")

(options2,args2)=parser2.parse_args()


##################
# Logging Service
##################
#
# logging level
if options2.debug:
 LOG_LEVEL=logging.DEBUG
 logging.basicConfig(stream=sys.stderr, level=LOG_LEVEL) 
 logger = logging.getLogger(inspect.stack()[-1][1])
else:
 LOG_LEVEL=logging.WARNING
 logging.basicConfig(stream=sys.stderr, level=LOG_LEVEL) 
 logger = logging.getLogger(inspect.stack()[-1][1])
 


#
#my autolog
#
def autolog(message,mylogger=None):
 """ to print debug messages """

# Get the previous frame in the stack, otherwise it would
# be this function!!!
 func = inspect.currentframe().f_back.f_code
# Dump the message + the name of this function to the log.
 if (mylogger==None):
  logger.debug("%s in %i ==> %s  " % (
  func.co_name, 
  func.co_firstlineno,
  message
  ))
 else:
  mylogger.debug("%s in %s:%i ==> %s  " % (
  func.co_name, 
  func.co_filename, 
  func.co_firstlineno,
  message
  ))
  return
##################





""" 
helper classes   and tests

"""


class Node(object):
 """ class to store and generate divsors """

 index=0

 def __init__(self, name):
  """ constructor """

  self.logger = logging.getLogger(self.__class__.__name__)

  self.__index = self.__class__.index
  self.__class__.index+=1
  self.__name = name
  self.__latex=False
  self.__x = self.getRandom(15.)
  self.__y = self.getRandom(15.)
  self.__edges=[]

  pass

 def resetIndex(self):
  """ to null the index """
  self.__class__.index=0


 def __eq__(self,other):
  if (other != None): return self.getIndex() == other.getIndex()
  else: return False


 def __hash__(self): return self.getIndex()


 def getIndex(self):
  """ return index of the node in the grap """
  return self.__index

 def getName(self):
  """ return the name of the Node """
  return self.__name


 def getX(self):
  """ returns the X-position of the node for latex code """
  return self.__x

 def getY(self):
  """ returns the Y-position of the node for latex code """
  return self.__y


 def getRandom(self,rang):
  """ returns random uniformly distributed value in the range [0,rang) """
  return random.uniform(0,rang)


 def setEdges(self,edg=None):
  """ to add the connection to the node """
  if (edg!=None and isinstance(edg,Edge.Edge)):
   self.__edges.append(edg)
  self.__edges.sort(key=lambda x: x.getWeight())
# or
#  self.__edges.sort(key=lambda x: x._Edge__wgt)
  pass

 def getEdges(self):
  """ to get the connection to the node """
  return self.__edges



 def setLatex(self):
  """ to allow printings in the Latex format """
  self.__latex = not self.__latex
  edges = self.getEdges()
  for edge in edges:
   if edge is not None and  edge.getLatex() != self.__latex: edge.setLatex()
  pass


 def getLatex(self):
  """ return the stats of the Latex output: allowed/not allowed """
  return self.__latex


# uncomment the line if you need a public "latex" attribute
# latex = property(getLatex, setLatex)



 def __repr__ (self):
  """ return the representation " name => [ \n edge-info \n] "
      if a  latex mode is  set up, returns latex commands
  """
  if (not self.__latex):
   res_str = " %s => [   %s  ]"
   edge_str="\n "
   for  edge in self.__edges:
    if edge is not None:
     edge_str+= repr(edge) + ",\n"
   return  res_str%(self.getName(),edge_str)
  else:
   return """
                \\tikzset{VertexStyle/.append  style={fill}}
                \Vertex[x=%.1f ,y=%.1f]{%s}
          """%( self.getX(),self.getY(),self.getName() )


 def __str__ (self):
  """ return the representation " name => [ \n edge-info \n] "
      if a  latex mode is  set up, returns latex commands
  """


  if (not self.__latex):
   res_str = " %s => [   %s  ]"
   edge_str="\n "
   for  edge in self.__edges:
    if edge is not None: edge_str+= repr(edge) + ",\n"
   return  res_str%(self.getName(),edge_str)
  else:
   return """
                \\tikzset{VertexStyle/.append  style={fill}}
                \Vertex[x=%.1f ,y=%.1f]{%s}
          """%( self.getX(),self.getY(),self.getName() )



  
class MyTests(unittest.TestCase):
 """ to test features """

 def __ini__(self):
  pass



""" 
main subroutine

"""

if  __name__ == '__main__':
 """ main subroutine """

### read options and prepare settings 

 if options2.test and str(__status__).lower()=="test":
  autolog("Test of the helper classes:  not supported \n\n\n")


