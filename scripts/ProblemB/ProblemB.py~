#! /usr/bin/env python



"""
This is the ProblemB  class to  find the shortes path between two Nodes in the Graph


To test the class :

       ./%prog    [--debug] [--tkinter]
       

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

import Graph
import Path
import Node
import Edge


parser=OptionParser(usage=__doc__)


parser.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser.add_option("--tkinter",dest="tkinter",help="to start gui",default=False,action="store_true")


parser.disable_interspersed_args()


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



INT_MAX=100



class ProblemB(object):
 """ class of ProblemB """
 global INT_MAX



 def __init__(self, graph=None):
  """ constructor """
  self.logger = logging.getLogger(self.__class__.__name__)
  if (graph is not None):
   self.__graph=graph
  else:
   self.__graph=Graph.Graph("empy")

  self.__dist=[None]*len(self.__graph.getNodes())
  pass

 def sort(self,nd1,nd2):
  """ to sort the set of nodes """
  return cmp(self.__dist[nd1.getIndex()],self.__dist[nd2.getIndex()]) or ( not (cmp(self.__dist[nd1.getIndex()],self.__dist[nd2.getIndex()])) and cmp(nd1.getIndex(),nd2.getIndex()))


 def getShortestPath(self, nd1, nd2):
  """ find the shorters weighted path between nd1 and nd2 """

  if (len(nd1.getEdges())*len(nd2.getEdges())<1 ): return Path.Path("shortest-path")
  if (len(self.__graph.getNodes())<1): return Path.Path("shortest-path")

  nodes = self.__graph.getNodes()
  edges = self.__graph.getEdges()
  paths={}
  path=[]
#  adj=[dict()]*len(nodes)
#  adj=[None]*len(nodes)
  adj={}
#  print "adj=",adj
  for edg in edges:
#   print "edg=",edg
#   print "before ", adj.get(edg.getOrigin().getIndex(),{})

#   _dict=adj.get(edg.getOrigin().getIndex(),{})
#   _dict.update({edg.getTarget().getName():edg.getWeight()})
#   adj[edg.getOrigin().getIndex()]=_dict

   _dict=adj.get(edg.getOrigin().getIndex(),{})
   _dict.update({edg.getTarget():edg.getWeight()})
   adj[edg.getOrigin().getIndex()]=_dict

#   adj[edg.getOrigin().getIndex()][edg.getTarget().getName()]=edg.getWeight()
#   adj[edg.getOrigin().getIndex()].update({edg.getTarget().getName():edg.getWeight()})
#   adj[edg.getOrigin().getIndex()].update({edg.getTarget():edg.getWeight()})

#   print "index=",edg.getOrigin().getIndex()
#   print "orig=", edg.getOrigin().getName()
#   print "content=",adj[edg.getOrigin().getIndex()]
#   print adj

#  print "adj[5]=",adj[5]
#  print "adj[3]=",adj[3]


  srcIndex = nd1.getIndex()
  trgtIndex = nd2.getIndex()
#  print "srcIndx=",srcIndex
#  print "trgtIndx=",trgtIndex

  for i in range(len(nodes)):
   if (i==srcIndex):
    self.__dist[i]=0.
   else:
    self.__dist[i]=INT_MAX

  q=set()
  q.add(nd1)
  paths[nd1.getIndex()]=paths.get(nd1.getIndex(),[]) + [nd1]
  while len(q)>0:
   q=set(sorted(q,cmp=self.sort))
   node=q.pop()
   if (trgtIndex == node.getIndex()): return   Path.Path("shortest-path",paths[trgtIndex])
   for k,v in adj[node.getIndex()].items():
     newDist = self.__dist[node.getIndex()] + v
     if newDist<self.__dist[k.getIndex()]:
      if k in q: q.remove(k)
      self.__dist[k.getIndex()] = newDist
      q.add(k)
      paths[k.getIndex()]=paths[node.getIndex()]
      paths[k.getIndex()]=paths.get(k.getIndex(),[]) + [k]


  return Path.Path("shortest-path")





""" 
main subroutine

"""  

def main():
 """ main subroutine """


 nodes=[None,None]
 edge1 = Edge.Edge("edge1",2.0,nodes)

 nodes2=[nodes[1],None]
 edge5 = Edge.Edge("edge5",1.0,nodes2)

 nodes3=[nodes2[1],None]
 edge6 = Edge.Edge("edge6",0.1,nodes3)

 nodes4=[nodes2[1],None]
 edge7 = Edge.Edge("edge7",0.5,nodes4)

 nodes5=[nodes3[1],nodes4[1]]
 edge8 = Edge.Edge("edge8",2.0,nodes5)

 nodes6=[nodes3[1],nodes2[1]]
 edge9 = Edge.Edge("edge9",0.1,nodes6)


 nd1=Node.Node("node1")

 nodes7=[nd1,nodes[0]]
 edge2 = Edge.Edge("edge2",0.5,nodes7)

 nodes8=[nd1,nodes5[0]]
 edge3 = Edge.Edge("edge3",2.5,nodes8)

 graph=Graph.Graph("graph1")
 graph.setEdges(edge1)
 graph.setEdges(edge2)
 graph.setEdges(edge3)
 graph.setEdges(edge5)
 graph.setEdges(edge6)
 graph.setEdges(edge7)
 graph.setEdges(edge8)
 graph.setEdges(edge9)


 print graph

 src=nd1
# trgt=  nodes3[1]
 trgt=  nodes4[1]

 prblmB=ProblemB(graph)
 path=prblmB.getShortestPath(src,trgt)
 print "Find the shortest path between \n %s \n and \n %s \n"%(str(src),str(trgt))

 print path

 pass


def mainTkinter():
 """ main subroutine with GUI """
 
 import Tkinter
 import Image
 import ImageTk
 import Tkinter

 class GraphWindow(object):

 
  def __init__(self,obj):
   self.obj=obj
   self.graph=None
   self.pathWindow=None


  def paint(self):

   tmpNode = Node.Node("tmp")
   tmpNode.resetIndex()

   nodes=[None,None]
   edge1 = Edge.Edge("edge1",2.0,nodes)

   nodes2=[nodes[1],None]
   edge5 = Edge.Edge("edge5",1.0,nodes2)

   nodes3=[nodes2[1],None]
   edge6 = Edge.Edge("edge6",0.1,nodes3)

   nodes4=[nodes2[1],None]
   edge7 = Edge.Edge("edge7",0.5,nodes4)

   nodes5=[nodes3[1],nodes4[1]]
   edge8 = Edge.Edge("edge8",2.0,nodes5)

   nodes6=[nodes3[1],nodes2[1]]
   edge9 = Edge.Edge("edge9",0.1,nodes6)


   nd1=Node.Node("node1")

   nodes7=[nd1,nodes[0]]
   edge2 = Edge.Edge("edge2",0.5,nodes7)

   nodes8=[nd1,nodes5[0]]
   edge3 = Edge.Edge("edge3",2.5,nodes8)


   graph=Graph.Graph("graph1")
   self.graph=graph

   self.graph.setEdges(edge1)
   self.graph.setEdges(edge2)
   self.graph.setEdges(edge3)
   self.graph.setEdges(edge5)
   self.graph.setEdges(edge6)
   self.graph.setEdges(edge7)
   self.graph.setEdges(edge8)
   self.graph.setEdges(edge9)

# src=nd1
# trgt=  nodes3[1]
# trgt=  nodes4[1]
   self.src=nd1
   self.trgt=nodes4[1]

   prblmB=ProblemB(self.graph)
   self.path=prblmB.getShortestPath(self.src,self.trgt)


   self.path.setLatex()


   self.graph.setLatex()

   self.graph.writeToFile("./",".tex")
   os.system("pdflatex "+self.graph.getName()+".tex")
   os.system("convert "+self.graph.getName()+".pdf " + self.graph.getName()+".png")
   self.imageFile = Image.open(self.graph.getName()+".png")
   self.image2 = ImageTk.PhotoImage(self.imageFile)
   self.panel = Tkinter.Label(self.obj, image=self.image2)
   self.panel.image=self.image2
   self.panel.grid(column=0,row=1)
   os.system("rm "+self.graph.getName()+"*")

   if (self.pathWindow): self.pathWindow.destroy()

   self.pathWindow = Tkinter.Toplevel(self.obj)
   self.pathWindow.title("The shortest path: %s -> %s "%(self.src.getName(),self.trgt.getName()))
   self.pathWindow.geometry('600x600')
   pathHandler=PathWindow(self.pathWindow,self.path)
#   button2 = Tkinter.Button(self.pathWindow, text = u"Generate Path !", command = pathHandler.paint)
#   button2.grid(column=0,row=0)
   pathHandler.paint()
   self.pathWindow.grid_columnconfigure(0,weight=1)
   self.pathWindow.resizable(True,False)



 class PathWindow(object):

#  global path

  def __init__(self,obj,path):
   self.obj=obj
   self.path=path



  def paint(self):

#   self.path.setLatex()
   self.path.writeToFile("./",".tex")
   os.system("pdflatex "+self.path.getName()+".tex")
   os.system("convert "+self.path.getName()+".pdf " + self.path.getName()+".png")
   self.imageFile = Image.open(self.path.getName()+".png")
   self.image2 = ImageTk.PhotoImage(self.imageFile)
   self.panel = Tkinter.Label(self.obj, image=self.image2)
   self.panel.image=self.image2
   self.panel.grid(column=0,row=1)
   os.system("rm "+self.path.getName()+"*")


# path=None

## graph window
 grWindow = Tkinter.Tk()
 grWindow.geometry('600x600')
 grWindow.title("Graph")
 grHandler=GraphWindow(grWindow)
 button = Tkinter.Button(grWindow, text = u"Generate Graph !", command = grHandler.paint)
 button.grid(column=0,row=0)
 grWindow.grid_columnconfigure(0,weight=1)
 grWindow.resizable(True,False)



# pathWindow = Tkinter.Toplevel(grWindow)
# pathWindow.geometry('600x600')
# pathHandler=PathWindow(pathWindow)
# button2 = Tkinter.Button(pathWindow, text = u"Generate Path !", command = pathHandler.paint)
# button2.grid(column=0,row=0)
# pathWindow.grid_columnconfigure(0,weight=1)
# pathWindow.resizable(True,False)

 grWindow.mainloop()



 return 



if  __name__ == '__main__':
 """ main subroutine """

 if options.tkinter: mainTkinter()
 else: main()


