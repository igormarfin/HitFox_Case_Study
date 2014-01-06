#! /usr/bin/env python

"""
This is the Path  class to  represent any consequent connections between
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


class Path(object):
 """ class to store and generate Paths """


 def __init__(self, name,nodes=None):
  """ constructor """

  self.logger = logging.getLogger(self.__class__.__name__)

  self.__name = name
  self.__latex=False
  if (nodes==None):  self.__nodes=[]
  else:  self.__nodes=nodes

  pass


 def getName(self):
  """ return the name of the Node """
  return self.__name


 def setNodes(self, node):
  """ add the node to the path """
  if node is not None and isinstance(node,Node.Node): self.__nodes.append(node)
  pass


 def getEdges(self):
  """ to get all nodes of the Graph  """
  edges=[]
  prev = self.__nodes[0]
  for i in range(1,len(self.__nodes)):
   __edges = prev.getEdges()
   for edg in __edges:
    if edg.getOrigin().getName() == prev.getName() and edg.getTarget().getName() ==  self.__nodes[i].getName():
     edges.append(edg)
   prev=self.__nodes[i]
  return edges



 def getTotalWeight(self):
  """ return total weight of the path """
  wgt=0.0
  for edg in self.getEdges():
   wgt+=edg.getWeight()
  return wgt



 def getNodes(self):
  """ to get all connections between the nodes """

  return self.__nodes





 def setLatex(self):
  """ to allow printings in the Latex format """
  self.__latex = not self.__latex
  nodes = self.getNodes()
  for node in nodes:
   if node is not None and  node.getLatex() != self.__latex: node.setLatex()
  pass


 def getLatex(self):
  """ return the stats of the Latex output: allowed/not allowed """
  return self.__latex


# uncomment the line if you need a public "latex" attribute
# latex = property(getLatex, setLatex)



 def __repr__ (self):
  """ return the representation " Path: name with total weight: 1.0 **** \n node-info-1 \n node-info-2 \n ... \n **** "
      if a  latex mode is  set up, returns latex commands
  """
  nodes_str="\n "
  edges_str="\n "

  for  node in self.getNodes():
   if node is not None: nodes_str+= str(node) + "\n"
  for  edge in self.getEdges():
   if edge is not None: edges_str+= str(edge) + "\n"
  if (not self.__latex):
   res_str = " Graph:  %s with total weight: %f ****   %s   ****"
   return  res_str%(self.getName(),self.getTotalWeight(),nodes_str)
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

                \mbox{Total weight: %f}

                \end{center}
                \end{document}
          """%(edges_str,self.getTotalWeight())


 def __str__ (self):
  """ return the representation " Path: name with total weight: 1.0 **** \n node-info-1 \n node-info-2 \n ... \n **** "
      if a  latex mode is  set up, returns latex commands
  """
  nodes_str="\n "
  edges_str="\n "

  for  node in self.getNodes():
   if node is not None: nodes_str+= str(node) + "\n"
  for  edge in self.getEdges():
   if edge is not None: edges_str+= str(edge) + "\n"
  if (not self.__latex):
   res_str = " Path:  %s with total weight: %f ****   %s   ****"
   return  res_str%(self.getName(),self.getTotalWeight(),nodes_str)
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

                \mbox{Total weight: %f}

                \end{center}
                \end{document}
          """%(edges_str,self.getTotalWeight())

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



 def test4(self):
  """ to test Path"""

  autolog("test of Path ")
  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nd2=Node.Node("nd2")
  nodes2=[nd1,nodes[0]]
  edge2 = Edge.Edge("edge2",0.5,nodes2)
  nodes3=[nodes[1],nd2]
  edge3 = Edge.Edge("edge3",1.5,nodes3)


  autolog("%s"%edge)
  autolog("%s"%edge2)
  autolog("%s"%edge3)

  path=Path("path1")
  print "size : ", len(path.getNodes())
  path.setNodes(nd1)
  path.setNodes(nodes[0])
  path.setNodes(nodes[1])
  path.setNodes(nd2)

#  print "size : ", len(path.getNodes())

  autolog(path.getNodes())
  autolog(" %s  "%path)


  self.failUnless(True)


 def test5(self):
  """ to test Latex Mode of  Path"""

  autolog("test of Path in Latex Mode")
  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nd2=Node.Node("nd2")
  nodes2=[nd1,nodes[0]]
  edge2 = Edge.Edge("edge2",0.5,nodes2)
  nodes3=[nodes[1],nd2]
  edge3 = Edge.Edge("edge3",1.5,nodes3)

  autolog("%s"%edge)
  autolog("%s"%edge2)
  autolog("%s"%edge3)

  path2=Path("path1")

  path2.setNodes(nd1)
  path2.setNodes(nodes[0])
  path2.setNodes(nodes[1])
  path2.setNodes(nd2)
  path2.setLatex()

  autolog(" %s  "%path2)


  self.failUnless(True)


 def test55(self):
  """ to test  writeToFile """

  autolog("test of Path.writeToFile ")

  nodes=[None,None]
  edge = Edge.Edge("edge",1.0,nodes)
  nd1=Node.Node("nd1")
  nd2=Node.Node("nd2")
  nodes2=[nd1,nodes[0]]
  edge2 = Edge.Edge("edge2",0.5,nodes2)
  nodes3=[nodes[1],nd2]
  edge3 = Edge.Edge("edge3",1.5,nodes3)


  autolog("%s"%edge)
  autolog("%s"%edge2)
  autolog("%s"%edge3)

  path=Path("path1")
  path.setNodes(nd1)
  path.setNodes(nodes[0])
  path.setNodes(nodes[1])
  path.setNodes(nd2)
  path.setLatex()

  autolog(" %s  "%path)


  path.writeToFile("../../latex/",".tex")



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
  







""" 
main subroutine

"""

def main():
 """ main subroutine for console"""


 nodes=[None,None]
 edge = Edge.Edge("edge",1.0,nodes)
 nd1=Node.Node("nd1")
 nd2=Node.Node("nd2")
 nodes2=[nd1,nodes[0]]
 edge2 = Edge.Edge("edge2",0.5,nodes2)
 nodes3=[nodes[1],nd2]
 edge3 = Edge.Edge("edge3",1.5,nodes3)



 path=Path("path1")
 path.setNodes(nd1)
 path.setNodes(nodes[0])
 path.setNodes(nodes[1])
 path.setNodes(nd2)
 print path
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

        button = Tkinter.Button(self,text=u"Generate Path !",  command=self.OnButtonClick)
        button.grid(column=0,row=0)


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)


        pass


    def OnButtonClick(self):




        nodes=[None,None]
        edge = Edge.Edge("edge",1.0,nodes)
        nd1=Node.Node("nd1")
        nd2=Node.Node("nd2")
        nodes2=[nd1,nodes[0]]
        edge2 = Edge.Edge("edge2",0.5,nodes2)
        nodes3=[nodes[1],nd2]
        edge3 = Edge.Edge("edge3",1.5,nodes3)



        self.path=Path("path1")
        self.path.setNodes(nd1)
        self.path.setNodes(nodes[0])
        self.path.setNodes(nodes[1])
        self.path.setNodes(nd2)
        self.path.setLatex()



        self.path.writeToFile("./",".tex")
        os.system("pdflatex "+self.path.getName()+".tex")
        os.system("convert "+self.path.getName()+".pdf " + self.path.getName()+".png")
        imageFile = Image.open(self.path.getName()+".png")
        image2 = ImageTk.PhotoImage(imageFile)
        panel = Tkinter.Label(self , image=image2)
        panel.image=image2
#        panel.pack()
        panel.grid(column=0,row=1)
        os.system("rm "+self.path.getName()+"*")
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







