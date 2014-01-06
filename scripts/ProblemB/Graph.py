#! /usr/bin/env python

"""
This is the Graph  class to  represent any consequent connections between
Nodes.


  " Node_orig1->Edge1->Node_taarget1->Edge2->Node_target2->..."


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
import Edge


parser2=OptionParser(usage=__doc__)


parser2.add_option("--test",dest="test",help="to perform test of helper classes",default=False,action="store_true")
parser2.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser2.add_option("--tkinter",dest="tkinter",help="to make a Tkinter window",default=False,action="store_true")

parser2.disable_interspersed_args()



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


class Graph(object):
 """ class to store and generate Graph """


 def __init__(self, name):
  """ constructor """

  self.logger = logging.getLogger(self.__class__.__name__)

  self.__name = name
  self.__latex=False
  self.__edges=[]

  pass



 def getName(self):
  """ return the name of the Node """
  return self.__name


 def setEdges(self, edge):
  """ add the node to the path """
  if edge is not None and isinstance(edge,Edge.Edge): self.__edges.append(edge)
  pass


 def getNodes(self):
  """ to get all nodes of the Graph  """
  nodes=set()

  for edge in self.__edges:
   nodes.add(edge.getOrigin())
   nodes.add(edge.getTarget())
  return nodes





 def getEdges(self):
  """ to get all connections between the nodes """

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
  """ return the representation " Graph: name <<<< \n node-info-1 \n node-info-2 \n ... \n <<<< "
      if a  latex mode is  set up, returns latex commands
  """
  nodes_str="\n "
  edges_str="\n "

  for  node in self.getNodes():
   if node is not None: nodes_str+= str(node) + "\n"
  for  edge in self.getEdges():
   if edge is not None: edges_str+= str(edge) + "\n"
  if (not self.__latex):
   res_str = " Graph:  %s <<<<   %s   <<<<"
   return  res_str%(self.getName(),nodes_str)
  else:
   return """
                \documentclass[11pt]{scrartcl}
                \usepackage{tkz-graph}
                \\begin{document}
                \\begin{center}
                \\begin{tikzpicture}
                \SetVertexNormal[Shape      = circle, FillColor  = orange, LineWidth  = 2pt]
                \SetUpEdge[lw  = 2pt,  color      = black,  labelcolor = white,  labeltext  = red, labelstyle = {sloped,draw,text=blue}]
                \GraphInit[vstyle=Normal]
                \SetGraphUnit{10}

                %s

                \end{tikzpicture}
                \end{center}
                \end{document}
          """%( edges_str)


 def __str__ (self):
  """ return the representation " Graph: name <<<< \n node-info-1 \n node-info-2 \n ... \n <<<< "
      if a  latex mode is  set up, returns latex commands
  """
  nodes_str="\n "
  edges_str="\n"

  for  node in self.getNodes():
   if node is not None: nodes_str+= str(node) + "\n"
  for  edge in self.getEdges():
   if edge is not None: edges_str+= str(edge) + "\n"
  if (not self.__latex):
   res_str = " Graph:  %s <<<<   %s   <<<<"
   return  res_str%(self.getName(),nodes_str)
  else:
   return """
                \documentclass[11pt]{scrartcl}
                \usepackage{tkz-graph}
                \\begin{document}
                \\begin{center}
                \\begin{tikzpicture}
                \SetVertexNormal[Shape      = circle, FillColor  = orange, LineWidth  = 2pt]
                \SetUpEdge[lw  = 2pt,  color      = black,  labelcolor = white,  labeltext  = red, labelstyle = {sloped,draw,text=blue}]
                \GraphInit[vstyle=Normal]
                \SetGraphUnit{10}

                %s

                \end{tikzpicture}
                \end{center}
                \end{document}
          """%( edges_str)

 def writeToFile(self,filename_prefix,filename_sufix):
  """ to write Graph to the file """
  file=open(filename_prefix+self.getName()+filename_sufix,"w")
  file.write(repr(self))
  file.close()
  pass


  
class MyTests(unittest.TestCase):
 """ to test features """

 def __ini__(self):
  pass

 def test1(self):
  """ to test Edge """

  autolog("test of Edge ")

  nodes=[None,None]

  edge = Edge.Edge("edge1",2.0,nodes)
  autolog("edge: %s"%edge)
  autolog("node1: %s"%nodes[0])
  autolog("node2: %s"%nodes[1])



  self.failUnless(True)


 def test2(self):
  """ to test Node """

  autolog("test of Node ")

  node1=[None]
  node2=Node.Node("node2")
  nodes=node1+[node2]
  autolog("(*) node2 %s"%node2)

  edge = Edge.Edge("edge2",1.0,nodes)
  autolog("edge: %s"%edge)
  autolog("node1: %s"%nodes[0])
  autolog("node2: %s"%nodes[1])



  self.failUnless(True)

 def test22(self):
  """ to test Node indexes """

  autolog("test of Node indexes")

  node1=[None]
  node2=Node.Node("node2")
  nodes=node1+[node2]

  edge = Edge.Edge("edge2",1.0,nodes)
  node3=Node.Node("node3")
  autolog("node1: %s"%nodes[0].getIndex())
  autolog("node2: %s"%nodes[1].getIndex())
  autolog("node3: %s"%node3.getIndex())
  



  self.failUnless(True)


 def test3(self):
  """ to test Latex Mode in  Node/Edge """

  autolog("test of Latex Mode in Node/Edge ")

  node2=Node.Node("node2")
  node2.setLatex()
  autolog("%s"%node2)


  node1=[None]
  nodes=node1+[node2]
  edge = Edge.Edge("edge",1.0,nodes)
  edge.setLatex()
  autolog("%s"%edge)
  autolog("%s"%nodes[0])
  autolog("%s"%node2)



  self.failUnless(True)


 def test4(self):
  """ to test Graph"""

  autolog("test of Graph ")
  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nodes2=[nodes[0],nd1]
  edge2 = Edge.Edge("edge2",0.5,nodes2)


  autolog("%s"%edge)
  autolog("%s"%edge2)

  graph=Graph("gr1")
  graph.setEdges(edge)
  graph.setEdges(edge2)

  autolog(" %s  "%graph)



  self.failUnless(True)


 def test5(self):
  """ to test Latex Mode of  Graph"""

  autolog("test of Graph ")
  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nodes2=[nodes[0],nd1]
  edge2 = Edge.Edge("edge2",0.5,nodes2)


  autolog("%s"%edge)
  autolog("%s"%edge2)

  graph=Graph("gr1")
  graph.setEdges(edge)
  graph.setEdges(edge2)
  graph.setLatex()

  autolog(" %s  "%graph)



  self.failUnless(True)


 def _test55(self):
  """ to test  writeToFile """

  autolog("test of Graph.writeToFile ")
  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nodes2=[nodes[0],nd1]
  edge2 = Edge.Edge("edge2",0.5,nodes2)



  graph=Graph("gr1")
  graph.setEdges(edge)
  graph.setEdges(edge2)
  graph.setLatex()
  graph.writeToFile("../../latex/",".tex")


  self.failUnless(True)



 def test6(self):
  """ to test the presence of some commands """

  import os

  res=os.system("which pdflatex")
  self.assertEqual(res,0)
  assert 0 == res

  res=os.system("which convert")
  self.assertEqual(res,0)
  assert 0 == res



 def test7(self):
  """ to test the ImageTk """


  import Image
  import ImageTk
  import Tkinter

  import os

  file=open("my_test.tex","w")
  content="""
               \documentclass[11pt]{scrartcl}
               \\begin{document}
               \\begin{center}
                \Huge{HELLO WORLD!}
                \end{center}
                \end{document}
  """
  file.write(content)
  file.close()

  res=os.system("pdflatex my_test.tex")
  self.assertEqual(res,0)
  assert 0 == res

  res=os.system("convert my_test.pdf my_test.png")
  self.assertEqual(res,0)
  assert 0 == res


  wind = Tkinter.Tk()
  imageFile2 = Image.open("my_test.png")
  image2 = ImageTk.PhotoImage(imageFile2)
  panel2 = Tkinter.Label(wind , image=image2)
  panel2.place(relx=0.0, rely=0.0)

  
  res=os.system("rm my_test.*")
  self.assertEqual(res,0)
  assert 0 == res
  





def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(MyTests))
    return suite





""" 
main subroutine

"""

def main():
 """ main subroutine for console"""

 nodes=[None,None]
 edge = Edge.Edge("edge",1.0,nodes)
 nd1=Node.Node("nd1")
 nodes2=[nodes[0],nd1]
 edge2 = Edge.Edge("edge2",0.5,nodes2)
 nodes3=[nd1,nodes[1]]
 edge3 = Edge.Edge("edge3",0.7,nodes3)



 graph=Graph("gr1")
 graph.setEdges(edge)
 graph.setEdges(edge2)
 graph.setEdges(edge3)
 print graph
 pass


def mainTkinter():
 """ main subroutine with GUI """

 import Tkinter
 import Image
 import ImageTk

 panel=None
 image2=None
 imageFile=None



 class simpleapp_tk(Tkinter.Tk):
    global panel,image2,imageFile

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        pass

    def setGraph(self,obj):
        self.graph=obj

    def initialize(self):
        self.grid()
        self.title("Graph")
        self.geometry('600x600')

        button = Tkinter.Button(self,text=u"Generate Graph !",  command=self.OnButtonClick)
        button.grid(column=0,row=0)


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)


        pass


    def OnButtonClick(self):


        nodes=[None,None]
        edge = Edge.Edge("edge",1.0,nodes)
        nd1=Node.Node("nd1")
        nodes2=[nodes[0],nd1]
        edge2 = Edge.Edge("edge2",0.5,nodes2)
        nodes3=[nd1,nodes[1]]
        edge3 = Edge.Edge("edge3",0.7,nodes3)




        self.graph=Graph("gr1")
        self.graph.setEdges(edge)
        self.graph.setEdges(edge2)
        self.graph.setEdges(edge3)
        self.graph.setLatex()



        self.graph.writeToFile("./",".tex")
        os.system("pdflatex "+self.graph.getName()+".tex")
        os.system("convert "+self.graph.getName()+".pdf " + self.graph.getName()+".png")
        imageFile = Image.open(self.graph.getName()+".png")
        image2 = ImageTk.PhotoImage(imageFile)
        panel = Tkinter.Label(self , image=image2)
        panel.image=image2
#        panel.pack()
        panel.grid(column=0,row=1)
        os.system("rm "+self.graph.getName()+"*")
        pass


 """
 nodes=[None,None]
 edge = Edge.Edge("edge",1.0,nodes)
 nd1=Node.Node("nd1")
 nodes2=[nodes[0],nd1]
 edge2 = Edge.Edge("edge2",0.5,nodes2)
 nodes3=[nd1,nodes[1]]
 edge3 = Edge.Edge("edge3",0.7,nodes3)




 graph=Graph("gr1")
 graph.setEdges(edge)
 graph.setEdges(edge2)
 graph.setEdges(edge3)
 graph.setLatex()
 """

 app = simpleapp_tk(None)
# app.setGraph(graph)
 app.mainloop()






 return 


if  __name__ == '__main__':
 """ main subroutine """

### read options and prepare settings 

 if options2.test and str(__status__).lower()=="test":
  autolog("Test of the helper classes:   \n\n\n")
  sys.argv=[sys.argv[0]]
  unittest.main()

 else:
  if options2.tkinter: mainTkinter()
  else: main()







