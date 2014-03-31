#! /usr/bin/env python



"""
This is the ProblemA  class to  generate     divisors of  numeric keys in a list:

Example Input:
[7,4,2,10,3,6,4,5]

Example Output:
{
2 => [1],
3 => [1],
4 => [1,2],
5 => [1],
6 => [1,2,3],
7 => [1],
10 => [1,2,5],
}


To test the class :

       ./%prog   [--debug] [--tkinter] <args>
       where <args> is the space-separated list of numbers:   7 4 2 10 3 6 4 5


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


parser=OptionParser(usage=__doc__)


parser.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser.add_option("--tkinter",dest="tkinter",help="to start gui",default=False,action="store_true")



if ("pydoc" in str(sys.argv)): parser.add_option("-w",dest="none",default=False,action="store_true")

(options,args)=parser.parse_args()



##################
# Logging Service
##################
#
# logging level
if options.debug:
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

from DivisorsHash import DivisorsHash



class ProblemA(object):
 """ class of ProblemA """



 def __init__(self, keys=None):
  """ constructor """
  self.logger = logging.getLogger(self.__class__.__name__)
  self.__keys=keys
  self.__divisors=[]
  if ( isinstance(keys,types.ListType)): self.__keys.sort()
  pass


 def setKeys(self,keys=None):
  """ to set the keys """
  if keys == None:
   self.logger.warning("provide me a numeric key")
   raise ValueError("keys are empty ")
  if ( not isinstance(keys,types.ListType)): raise TypeError("It's not  the list of keys")
  if not all(isinstance(key, types.IntType) for key in keys):  raise TypeError("keys are not integers all")
  self.__keys=keys
  self.__keys.sort()
  pass


 def generate(self):
  """ to generate divisors for all input number """
  if self.__keys == None:
   self.logger.warning("provide me a numeric key")
   raise ValueError("keys are empty ")
  if ( not isinstance(self.__keys,types.ListType)): raise TypeError("It's not  the list of keys")
  if not all(isinstance(key, types.IntType) for key in self.__keys):  raise TypeError("keys are not integers all")
  for key in self.__keys:
   dh=DivisorsHash(key)
   dh.findDivisors()
   self.__divisors.append(dh)
  return self.__divisors



 def __repr__ (self):
  """ return the list of the representation "{ key: 'number' => value: 'divisors of the number in the list' }" """
  str1="{\n"
  for i in range(len(self.__keys)):
   if (i<len(self.__keys)-1): str1+=repr(self.__divisors[i])+",\n"
   else: str1+=repr(self.__divisors[i])+"\n } \n"

  return str1



 def __str__ (self):
  """ return the list of the representation "{ key: 'number' => value: 'divisors of the number in the list' }" """
  str1="{\n"
  for i in range(len(self.__keys)):
   if (i<len(self.__keys)-1): str1+=str(self.__divisors[i])+",\n"
   else: str1+=str(self.__divisors[i])+"\n } \n"

  return str1



  



""" 
main subroutine

"""  

def main():
 """ main subroutine """

### read options and prepare settings 

 if (len(args)<1):
  print "provide the input list"
  print __doc__
 else:
  keys=[int(x) for x in args]
  pA = ProblemA()
  pA.setKeys(keys)
  pA.generate()
  print pA
 return

def mainTkinter():
 """ main subroutine with GUI """
 
 import Tkinter

 class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        pass

    def initialize(self):
        self.grid()
        self.title("ProblemA")

        self.entryVariable = Tkinter.StringVar() 
        self.labelVariable = Tkinter.StringVar() 

        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.grid(column=0,row=0,sticky='EW')

        button = Tkinter.Button(self,text=u"Process Numbers !",  command=self.OnButtonClick)
        button.grid(column=1,row=0)


        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

        pass


    def OnButtonClick(self):
        self.OnPressEnter(self)

    def OnPressEnter(self,event):
        args1 =  self.entryVariable.get().split()
        keys=[int(x) for x in args1]
        pA = ProblemA()
        pA.setKeys(keys)
        pA.generate()
        self.labelVariable.set("%s"%pA) 



 app = simpleapp_tk(None)
 app.mainloop()  
 return 


if  __name__ == '__main__':
 """ main subroutine """

 if options.tkinter: mainTkinter()
 else: main()


