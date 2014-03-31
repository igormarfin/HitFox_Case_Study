#! /usr/bin/env python

"""
This is the Edge  class to  represent the adjancent edge between two nodes

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
import Node



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


class Edge(object):
 """ class to store and generate divsors """


 def __init__(self, name, wgt, *nodes):
  """ constructor """
  self.logger = logging.getLogger(self.__class__.__name__)
  self.__name=name
  self.__wgt=wgt
  self.__latex=False
  orig_name=name + "-orig"
  target_name=name + "-target"
  if (len(nodes[0])>0 and nodes[0][0]==None):  nodes[0][0]=Node.Node(orig_name)
  nodes[0][0].setEdges(self)

  if (len(nodes[0])>1 and nodes[0][1]==None):  nodes[0][1]=Node.Node(target_name)
  nodes[0][1].setEdges(self)


  self.__origNode = nodes[0][0]
  self.__targetNode = nodes[0][1]



 def getName(self):
  """ return the name of the Node """
  return self.__name



 def getWeight(self):
  """ return the weight """
  return self.__wgt

 def setLatex(self):
  """ to allow printings in the Latex format """
  self.__latex = not self.__latex
  if (self.__origNode != None and self.__origNode.getLatex()!=self.__latex): self.__origNode.setLatex()
  if (self.__targetNode != None and self.__targetNode.getLatex()!=self.__latex): self.__targetNode.setLatex()
  pass


 def getLatex(self):
  """ return the stats of the Latex output: allowed/not allowed """
  return self.__latex


# uncomment the line if you need a public "latex" attribute
# latex = property(getLatex, setLatex)

 def getOrigin(self):
  """ return the origin Node"""
  return self.__origNode

 def getTarget(self):
  """ return the target Node"""
  return self.__targetNode



 def __repr__ (self):
  """ return the representation "{ name : (weight, orig-name,target-name) } "
      if a  latex mode is  set up, returns latex commands
  """
  if (not self.__latex):  return " {%s : (%f,%s,%s) }" %(self.getName(),self.getWeight(), self.getOrigin().getName(),self.getTarget().getName())
  else:
   return """
                %s
                %s
                \\tikzset{EdgeStyle/.style={->}}
                \Edge[label=$%.2f$](%s)(%s)

          """%(repr(self.getOrigin()),repr(self.getTarget()),
                self.getWeight(), self.getOrigin().getName(),self.getTarget().getName())


 def __str__ (self):
  """ return the representation "{ name : (weight, orig-name,target-name) } "
      if a  latex mode is  set up, returns latex commands
  """

  if (not self.__latex):  return " {%s : (%f,%s,%s) }" %(self.getName(),self.getWeight(), self.getOrigin().getName(),self.getTarget().getName())
  else:
   return """
                %s
                %s
                \\tikzset{EdgeStyle/.style={->}}
                \Edge[label=$%.2f$](%s)(%s)

          """%(repr(self.getOrigin()),repr(self.getTarget()),
                self.getWeight(), self.getOrigin().getName(),self.getTarget().getName())





  
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


