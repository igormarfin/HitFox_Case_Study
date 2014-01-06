#! /usr/bin/env python

"""
This is the DivisorsHash  class to  generate   and store divisors of any numeric key

  "DivisorsHash { key: 'number' => value: 'divisors of the number in the list' }"

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

parser2=OptionParser(usage=__doc__)


parser2.add_option("--test",dest="test",help="to perform test of helper classes",default=False,action="store_true")
parser2.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser2.add_option("--tkinter",dest="tkinter",help="to print debug info",default=False,action="store_true")



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

class DivisorsHash(object):
 """ class to store and generate divsors """


 def __init__(self, key=None):
  """ constructor """
  self.logger = logging.getLogger(self.__class__.__name__)
  self.__key=key
  self.__divisors=[]
  pass


 def setKey(self,key=None):
  """ to set the key """
  if key == None:
   self.logger.warning("provide me a numeric key")
   raise ValueError("key is empty ")
  if not isinstance(key, types.IntType):  raise TypeError("key is non-integer")
  self.__key=key
  pass



 def getKey(self):
  """ to get the key """
  return self.__key


 def findDivisors(self):
  """ find and returns all divisors (as an ordered list) """

  if (self.__key == None):
   self.logger.warning("provide me a numeric key")
   raise ValueError("key is empty ")

  if not isinstance(self.__key, types.IntType):  raise TypeError("key is non-integer")

  if self.__key < 0 : self.__key*=-1
  keysqrt = math.sqrt(self.__key)
  for i in range(1,int(keysqrt)+1):
   if self.__key%i==0:
    self.__divisors.append(i)
    if i>1 and i<self.__key/i: self.__divisors.append(self.__key/i)
  self.__divisors.sort()
  return self.__divisors


 def getDivisors(self):
  """ return the list of divisors """
  return self.__divisors


# uncomment the line if you need a public "key" attribute
# key = property(getKey, setKey)




 def __repr__ (self):
  """ return the representation "{ key: 'number' => value: 'divisors of the number in the list' }" """
  return "  key: %d => %s " %(self.getKey(),repr(self.getDivisors()))


 def __str__ (self):
  """ return the representation "{ key: 'number' => value: 'divisors of the number in the list' }" """
  return "  key: %d => %s " %(self.getKey(),repr(self.getDivisors()))




  
class MyTests(unittest.TestCase):
 """ to test features """

 def __ini__(self):
  pass

 def test1(self):
  """ to test setKey()/getKey() """

  autolog("test of setKey() ")

  dh = DivisorsHash()
  try:
   dh.setKey(None)
  except Exception as e:
   autolog("Some problems are detected: %s"%e)


  try:
   dh.setKey("test")
  except Exception as e:
   autolog("Some problems are detected: %s"%e)

  try:
   dh.setKey(10)
   autolog("the key is %d"%dh.getKey())
  except Exception as e:
   autolog("Some problems are detected: %s"%e)

  self.failUnless(True)


 def test2(self):
  """ to test findDivisors() """

  autolog("test of findDivisors() ")

  dh = DivisorsHash()

  try:
   dh.setKey(10)
   autolog("the key is %d"%dh.getKey())
   autolog("the list of divisors is %s"%repr(dh.findDivisors()))
  except Exception as e:
   autolog("Some problems are detected: %s"%e)

  self.failUnless(True)



 def test3(self):
  """ to test representation of DivisorsHash """

  autolog("test of __str__() ")

  dh = DivisorsHash()

  try:
   dh.setKey(10)
   dh.findDivisors()
   autolog("%s"%dh)
  except Exception as e:
   autolog("Some problems are detected: %s"%e)

  self.failUnless(True)



""" 
main subroutine

"""  

if  __name__ == '__main__':
 """ main subroutine """

### read options and prepare settings 

 if options2.test and str(__status__).lower()=="test":
  autolog("Test of the helper classes:\n\n\n")
  sys.argv=[sys.argv[0]]
  unittest.main()


