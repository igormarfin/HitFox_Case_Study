#! /usr/bin/env python

"""
This is a steering script to run TripleBtagAnalysis code

Examples:

       ./%prog 				---> run using default settings
       ./%prog  --test  	---> to test helper classes (only for test versions)
       ./%prog  --mva 		---> to run with mva selection

       ./%prog  --default_ini="MyTripleBtagAnalysis_SF_default.ini"  --user_ini="MyTripleBtagAnalysis_SF.ini"
							---> to run on "non-standard" ini files
   
       ./%prog  --lists_of_ntuples="*file*Run2012*txt" 
							---> to set up a pattern of files with lists of ntuples

       ./%prog  --lists_of_mva_files="*file*Run2012*selTree*root" 
							---> to set up a pattern of files with mva selTrees.


       ./%prog  --mva_path="/my/path/to/mva/selTree/root/files/"
							---> to set up a base path where the mva selTree files can be found

       ./%prog  --debug		---> to print debug info

       ./%prog  --no-systematics="No_Sys"		
							---> to change the sub-folder name for "no systematics" case


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

# designed but not implemented support
#from multiprocessing import Pool, Lock 

import math
import numpy
import random
import array
import copy
import subprocess
import os.path
import ConfigParser as cp
import logging

import  fnmatch
import cPickle as pickle
import zlib
import unittest
import inspect

parser=OptionParser(usage=__doc__)


parser.add_option("--mva",dest="mva",help="to switch on mva selection",default=False,action="store_true")
parser.add_option("--test",dest="test",help="to perform test of helper classes",default=False,action="store_true")
parser.add_option("--debug",dest="debug",help="to print debug info",default=False,action="store_true")
parser.add_option("--default_ini",dest="default_ini",type="string",help="to change the default ini file")
parser.add_option("--user_ini",dest="user_ini",type="string",help="to change the user ini file")
parser.add_option("--lists_of_ntuples",dest="lists_of_ntuples",type="string",help="to set up a pattern for file with  lists of ntuples")
parser.add_option("--no-systematics",dest="nosystem",type="string",help="the folder name for \"no systematics\" case")



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


##################
# initial settings
##################
#
#
#pattern of files with lists of ntuples
lists_of_ntuples="*file*Run2012*txt"
lists_of_mva_files="*file*Run2012*selTree*root"

# executable: TripleBtagAnalysis
triple_b_tag_exec="$CMSSW_BASE/bin/$SCRAM_ARCH/TripleBtagAnalysis_SF"


# ini files for TripleBtagAnalysis executable
default_ini="TripleBtagAnalysis_SF_default.ini"
user_ini="TripleBtagAnalysis_SF.ini"

#possible systematic variation
# a new keyword: All
systematic_type= ["JES", "JERSF", "BTagSF","All"]
systematic_direction=["UP", "DOWN"]

#executable: mkdir
mkdirp="mkdir -p"

#No systematics handler
nosystem="NoSystematics"

# mva: OFF(False)/ON(True)
mva=False

""" 
helper classes

"""

class Configurator(object):
 """ class to read ini files """

# logger2=logging.getLogger(self.__class__.__name__)

 def __init__(self):
  self.Config=cp.ConfigParser()
  self.logger = logging.getLogger(self.__class__.__name__)

   
 def ConfigSectionMap(self,section):
    dict1 = {}
    options = self.Config.options(section)
    for option in options:
        try:
            dict1[option] = self.Config.get(section, option)
            if dict1[option] == -1:
                self.logger.debug("skip: %s" % option)
        except:
            self.logger.warning("exception on %s!" % option)
            dict1[option] = None
    return dict1




 def ReadIni(self,basic_ini="TripleBtagAnalysis_SF_default.ini",user_ini="TripleBtagAnalysis_SF.ini"):
  """   read ini files  
        return name of the scenario, systematic variation, mva_file
  """
 
  scenario=None
  systematic_var=None
  mva_file=None
 
# try to read default ini
  if (os.path.exists(basic_ini)):
   try:
    self.Config.read(basic_ini)
    scenario=self.ConfigSectionMap("TripleBtagAnalysis_SF_General")["scenario"]
    systematic_name=self.ConfigSectionMap("TripleBtagAnalysis_SF_SystematicUncertainties")["name"]
    if (len([i for i in systematic_type if i.lower()==systematic_name.lower()])>0 ):
     autolog("found correct variation: %s" % systematic_name,self.logger)
     systematic_var=systematic_name
    systematic_dir=self.ConfigSectionMap("TripleBtagAnalysis_SF_SystematicUncertainties")["direction"]
    if (len([i for i in systematic_direction if i.lower()==systematic_dir.lower()])>0 ) and (systematic_var!=None):
     systematic_var=systematic_var+"_"+systematic_dir  
    if (systematic_var==None):
     self.logger.warning("No systematics")
   except:
    self.logger.warning("Something wrong with %s" % basic_ini)
  else:
   self.logger.warning("File %s not found"%basic_ini)

# try to read user ini
  if (os.path.exists(user_ini)):
   try:
    self.Config.read(user_ini)
    scenario=self.ConfigSectionMap("TripleBtagAnalysis_SF_General")["scenario"]
   except:
    pass
   try:
    systematic_name=self.ConfigSectionMap("TripleBtagAnalysis_SF_SystematicUncertainties")["name"]
    if (len([i for i in systematic_type if i.lower()==systematic_name.lower()])>0 ):
     autolog("found correct variation: %s" % systematic_name,self.logger)
     systematic_var=systematic_name
    systematic_dir=self.ConfigSectionMap("TripleBtagAnalysis_SF_SystematicUncertainties")["direction"]
    if (len([i for i in systematic_direction if i.lower()==systematic_dir.lower()])>0 ) and (systematic_var!=None):
     systematic_var=systematic_var+"_"+systematic_dir  
    if (systematic_var==None):
     self.logger.warning("No systematics")    
   except:
    self.logger.warning("Something wrong with %s" % user_ini)
  else:
   self.logger.warning("File %s not found"%user_ini)

  return (scenario,systematic_var)

 def ChangeField(self,ini_file="TripleBtagAnalysis_SF.ini",section=None,field=None,value=None,new_ini_file="TripleBtagAnalysis_SF_new.ini"):
  """ to change fields in ini files """
 
  self.Config.read(ini_file)
  if all(v is not None for v in [section,field,value]):
   try:
    self.Config.set(section,field,value)
    f=open(new_ini_file,"wb")
    self.Config.write(f)
   except:
    self.logger.warning("something wrong with new ini")
  return


class FileUtils(object):
 """ class to work with files  """

 def __init__(self):
  self.logger = logging.getLogger(self.__class__.__name__)
  pass

 def Run(self,prog,args="", shell="/bin/bash"):
  """ to run executable """

  if (len(prog))<=0 : return None

  autolog(prog+" "+args,self.logger)
  p=subprocess.Popen(prog+" "+args,  stdout=subprocess.PIPE, shell=True,executable =shell)
  res,err=p.communicate()
  autolog(res,self.logger)
  return (res,err)


 def CreateFolder(self,domkdir=True,*args):
  """ create folder as arg1/arg2/arg3 etc 
      and return it back  
  """
  folder=""
  for arg in args: folder+=str(arg)+"/"
  fU=FileUtils()
  if (domkdir): out,err=fU.Run(mkdirp,folder)
  
  return folder  

 
 def GetListOfFiles(self,pattern="*", path=""):
  """ find files using pattern
    example: find all root files in theMergeList-pythia_QCD_Pt-30To50 subfolder of 
    /data/user/marfin/CMSSW_5_3_3/src/Analysis/HbbMSSMAnalysis/test/Analysis2012/

    GetListFiles("*the*30To50*root","/data/user/marfin/CMSSW_5_3_3/src/Analysis/HbbMSSMAnalysis/test/Analysis2012/"
  """
  treeroot=os.getcwd()
  if (len(path)!=0): treeroot=path

  results = []
  for base, dirs, files in os.walk(treeroot):
    files=map(lambda x: base+"/"+x,files)
    goodfiles = fnmatch.filter(files, pattern)
    results.extend(os.path.join(base, f) for f in goodfiles)

  return list(set(results))



class ExternalAction(FileUtils):
 """ to do external actions like a copy, on  ini files, list files
 """

 def __init__(self,cmd="",level=0,orig=None):
  if orig==None:
   self.logger = logging.getLogger(self.__class__.__name__)
   self.cmd=cmd
   self.inilevel=level
   self.level=level
   self.myarg=""
  if orig is not None and isinstance(orig,ExternalAction):
   self.__dict__ = dict(orig.__dict__)
   self.__dict__["level"]-=1
  return


 def __call__(self, arg):
  if (self.cmd==""): return
  if (arg and self.inilevel==self.level): self.myarg=arg
  strcmd=self.cmd
  autolog("I'm in external(2) %s"%strcmd, self.logger)
  strcmd=re.sub("%s",self.myarg,strcmd)
  autolog("I'm in external(3) %s"%strcmd, self.logger)
  autolog("I'm in external(5) %d"%self.level, self.logger)
  autolog("I'm in external(6) %d"%self.inilevel, self.logger)
  if (self.inilevel!=self.level): self.cmd=strcmd
  if (self.level!=0): return
  autolog("I'm externally  doing %s"%strcmd,self.logger)
  self.Run(strcmd)
  return

class InternalAction(Configurator):
 """ to change fields in  ini files 
 """

 def __init__(self,file="",args=[],level=0,orig=None):
  if orig==None:
   self.logger = logging.getLogger(self.__class__.__name__)
   self.file=file
   self.args=args
   self.level=level
   self.inilevel=level
   self.myarg=""
   super(InternalAction,self).__init__()
  if orig is not None and isinstance(orig,InternalAction):
   self.__dict__ = dict(orig.__dict__)
   self.__dict__["level"]-=1
   super(InternalAction,self).__init__()
  return


 def __call__(self, *args):
  autolog("I'm in internal call", self.logger)
  if (self.file==""): return 
  if (len(self.args)<3): return
  if (len(args)<1): return
  autolog("I'm in internal call(2)", self.logger)
  if (self.inilevel==self.level):  self.myarg=args[0]
  autolog("args[0]: %s"%args[0],self.logger)
  autolog("myarg: %s"%self.myarg,self.logger)
  if (self.level!=0): return
  autolog("I'm internally  doing on %s"%self.myarg,self.logger) 
  self.ChangeField(self.file,self.args[0],self.args[1],self.myarg,self.args[2])   
  return



class Transformer(object):
 """ to transform input string to output string 
     It uses the some pattern:   name of file ==>(pattern)==>name of the directory
 """

 def __init__(self,pattern,replacement):
  self.logger = logging.getLogger(self.__class__.__name__)
  self.pattern=pattern
  self.replacement=replacement
  return

 def __call__(self,arg):

  """ do transformation like    re.sub(self.pattern,self.replacement,arg) """ 


  return re.sub(self.pattern,self.replacement,arg)



class Looper(FileUtils):
 """  to organize loop """
 
 def __init__(self,loop,prog,args="",createFolder=True):
  self.loop=loop
  self.prog=prog
  self.args=args
  self.looper=None
  self.executors_ext=[]
  self.executors_int=[]
  self.transformers=[]
  self.domkdir=createFolder
  self.nExecsExt=0
  self.nExecsInt=0
  self.logger = logging.getLogger(self.__class__.__name__)
  return

 def SetInnerLoop(self,looper=None):
  self.looper=looper
  return

 def AddExternalExecutors(self,Executors,initial=True):
  if (initial): self.nExecsExt+=len(Executors)
  for i in range(len(self.executors_ext)-self.nExecsExt): self.executors_ext.pop(0)
  self.executors_ext=Executors+self.executors_ext
  
  return

 def AddInternalExecutors(self,Executors,initial=True):
  if (initial): self.nExecsInt+=len(Executors)
  for i in range(len(self.executors_int)-self.nExecsInt): self.executors_int.pop(0)
  self.executors_int= Executors + self.executors_int 
  return

 def CopyExternalExecutors(self):
  autolog("We are in CopyExternalExecutors()",self.logger)
  return [ExternalAction("",0,a) for a in self.executors_ext]

 def CopyInternalExecutors(self):
  autolog("We are in CopyInteranlExecutors()",self.logger)
  return [InternalAction("",[],0,a) for a in self.executors_int]

 def SetTransformers(self,transformers=[]):
  self.transformers=transformers
  autolog(self.transformers,self.logger)
  return

 def __add__(self, rhs):
#   return Looper(self.loop, self.prog+" "+self.args+" ; "+rhs.prog)
    newloop=Looper(self.loop+rhs.loop,"")
    newloop.__dict__["executors_ex"]=self.__dict__["executors_ex"]+rhs.__dict__["executors_ex"]
    newloop.__dict__["executors_int"]=self.__dict__["executors_int"]+rhs.__dict__["executors_int"]
    newloop.__dict__["transformers"]=self.__dict__["transformers"]+rhs.__dict__["transformers"]
    newloop.__dict__["prog"]=self.__dict__["prog"] + " " + self.__dict__["args"]+ " ; " + rhs.__dict__["prog"] + " " + rhs.__dict__["args"]
    newloop.__dict__["args"]=""
    newloop.__dict__["domkdir"]=self.__dict__["domkdir"]

 def __radd__(self, rhs):
#   return Looper(self.loop, self.prog+" "+self.args+" ; "+rhs.prog)
    newloop=Looper(self.loop+rhs.loop,"")
    newloop.__dict__["executors_ex"]=self.__dict__["executors_ex"]+rhs.__dict__["executors_ex"]
    newloop.__dict__["executors_int"]=self.__dict__["executors_int"]+rhs.__dict__["executors_int"]
    newloop.__dict__["transformers"]=self.__dict__["transformers"]+rhs.__dict__["transformers"]
    newloop.__dict__["prog"]=self.__dict__["prog"] + " " + self.__dict__["args"]+ " ; " +   rhs.__dict__["prog"]+" "+rhs.__dict__["args"]
    newloop.__dict__["args"]=""
    newloop.__dict__["domkdir"]=self.__dict__["domkdir"]


 def Runloop(self):
  for lp in self.loop:
   origlp=lp
   for tF in self.transformers: 
    lp=tF(lp)
   if (self.domkdir): 
    self.Run(mkdirp,lp)
#   try:
    if (self.domkdir): os.chdir(lp)
    autolog("Original loop element: %s"%origlp,self.logger)
    autolog("transformed loop element: %s"%lp,self.logger)
    self.logger.info("Directory :: %s ::"%os.getcwd())
    for execs in self.executors_ext: execs(origlp)
    autolog("passed external ops",self.logger)
    for execs in self.executors_int: execs(origlp)
    autolog("passed internal ops",self.logger)
    if (self.looper!=None): 
     autolog("We are inner loop",self.logger)
     self.looper.AddExternalExecutors(self.CopyExternalExecutors(),False)
     self.looper.AddInternalExecutors(self.CopyInternalExecutors(),False)
     autolog("We pass AddExecutors()",self.logger)
     self.looper.Runloop()
    res,err=self.Run(self.prog,self.args)
    autolog("result from Run():  %s"%res,self.logger) 
    if (self.domkdir): os.chdir("..")
#   except:
#    self.logger.warning("Exception in RunLoop()")    
  return   

  
class MyTests(unittest.TestCase):
 """ to test features """

 def __ini__(self):
  pass

 def test1(self):
  
  config=Configurator()
  (scenario,systematic)=config.ReadIni(default_ini,user_ini)
  autolog("Test of readini")
  autolog("SCENARIO: %s"%scenario)
  autolog("SYSTEMATICS: %s"%systematic)
  self.failUnless(True)


 def test2(self):
  
  fU=FileUtils()
  autolog("Test of FileUtils.GetListOfFiles()")
  autolog("All Files: %s"%fU.GetListOfFiles())
  autolog("Only ini Files: %s"%fU.GetListOfFiles("*ini*"))
  self.failUnless(True)

 def test3(self):
  
  fU=FileUtils()
  autolog("Test of FileUtils.Run()")
  out,err=fU.Run("ls ","-lrth *ini") 
  autolog(" ls all *ini in the current dir:\n%s"%out)
  self.failUnless(True)

 def test4(self):

  config=Configurator()
  (scenario,systematic)=config.ReadIni(default_ini,user_ini)
  fU=FileUtils()
  logger.debug("Test of FileUtils.CreateFolder()")
  fld=fU.CreateFolder(False,scenario,systematic)
  autolog("prototype of the folder to contain results:  %s"%fld)
  self.failUnless(True)


 def test6(self):
  config=Configurator()
  autolog("Test of Configurator.changefield()")
  config.ChangeField(user_ini,"TripleBtagAnalysis_SF_SystematicUncertainties","Name","JES","TripleBtagAnalysis_SF_new.ini")
  config.ChangeField("TripleBtagAnalysis_SF_new.ini","TripleBtagAnalysis_SF_SystematicUncertainties","size","1","TripleBtagAnalysis_SF_new.ini")
  config.ChangeField("TripleBtagAnalysis_SF_new.ini","TripleBtagAnalysis_SF_SystematicUncertainties","direction","DOWN","TripleBtagAnalysis_SF_new.ini")
  self.failUnless(True)


 def test7(self):
  fU=FileUtils()
  autolog("Test of Transformer")
  filelists=fU.GetListOfFiles('*file*txt',"")
  tF=Transformer(r'(.*/)(.*?)_(.*)(\.txt)', r'\3')
  for filelist in filelists:
   autolog("transformation:  %s"%tF(filelist))
  self.failUnless(True)


 def test8(self):

  config=Configurator()
  (scenario,systematic)=config.ReadIni(default_ini,user_ini)
  fU=FileUtils()
  filelists=fU.GetListOfFiles('*file*txt',"")
  tF=Transformer(r'(.*/)(.*?)_(.*)(\.txt)', r'\3')
  logger.debug("Test of Looper")
  systematic=systematic.split("_")
  mylooper=Looper([str(scenario)],"pwd")   
  mylooper4=Looper(filelists,"ls","",True)
  mylooper4.SetTransformers([tF])
  if (str(systematic[0]).lower()=="all"):   
   mylooper1=Looper(systematic_direction,"pwd")
   mylooper2=Looper(systematic_direction,"sleep 1; for ((i=1;i<5;i++)); do echo $i; done")
   mylooper3=Looper(systematic_direction,"pwd")
   mylooper1+=mylooper2+mylooper3
   mylooper0=Looper(systematic_type[:-1],"pwd")
   mylooper0.SetInnerLoop(mylooper1) 
   mylooper4.SetInnerLoop(mylooper0) 
  mylooper.SetInnerLoop(mylooper4) 
  mylooper.Runloop()
  self.failUnless(True)


# do not test test9, replace _test9 by test9 to perform the test
 def test9(self):

  logger.debug("Test of Executor: External")
  config=Configurator()
  (scenario,systematic)=config.ReadIni(default_ini,user_ini)
  fU=FileUtils()
  filelists=fU.GetListOfFiles('*file*txt',"")
  tF=Transformer(r'(.*/)(.*?)_(.*)(\.txt)', r'\3')
  systematic=systematic.split("_")
  mylooper=Looper([str(scenario)],"pwd")
  mylooper1=Looper(filelists,"ls","",True)
  mylooper1.SetTransformers([tF])
  exec1 =ExternalAction("cp %s theMergeList.txt",0)
  inifiles=fU.GetListOfFiles("*TripleBtagAnalysis_SF*ini*")  
  if (len(inifiles)>0): mylooper1.AddExternalExecutors([ExternalAction("cp %s ."%file,0) for file in inifiles] )
  mylooper1.AddExternalExecutors([exec1])
  mylooper.SetInnerLoop(mylooper1)
  mylooper.Runloop()   
  self.failUnless(True)


# do not test test10 
 def test10(self):


  logger.debug("Test of Executor: Internal")
  config=Configurator()
  (scenario,systematic)=config.ReadIni(default_ini,user_ini)
  fU=FileUtils()
#  filelists=fU.GetListOfFiles('*file*Run2012B*txt',"")
  filelists=fU.GetListOfFiles('*file*Run2012*txt',"")
  tF=Transformer(r'(.*/)(.*?)_(.*)(\.txt)', r'\3')
  systematic=systematic.split("_")
  mylooper=Looper([str(scenario)],"pwd")
  mylooper1=Looper(filelists,"ls","",True)
  mylooper1.SetTransformers([tF])
  inifiles=fU.GetListOfFiles("*TripleBtagAnalysis_SF*ini*")  
  if (len(inifiles)>0): mylooper1.AddExternalExecutors([ExternalAction("cp %s ."%file,2) for file in inifiles] )
  mylooper1.AddExternalExecutors([ExternalAction("cp %s theMergeList.txt",2)])
  if (str(systematic[0]).lower()=="all"):   
   mylooper2=Looper(systematic_type[:-1],"pwd")
   mylooper3=Looper(systematic_direction,"pwd")
   mylooper2.AddInternalExecutors([InternalAction(user_ini,["TripleBtagAnalysis_SF_SystematicUncertainties","Name",user_ini],1)])
   mylooper3.AddInternalExecutors([InternalAction(user_ini,["TripleBtagAnalysis_SF_SystematicUncertainties","direction",user_ini],0)])
   mylooper2.SetInnerLoop(mylooper3) 
   mylooper1.SetInnerLoop(mylooper2) 
  mylooper.SetInnerLoop(mylooper1) 
  mylooper.Runloop()
  self.failUnless(True)



""" 
main subroutine

"""  

if  __name__ == '__main__':
 """ main subroutine """

### read options and prepare settings 

 if options.test and str(__status__).lower()=="test":
  autolog("Test of the helper classes:\n\n\n")
  sys.argv=[sys.argv[0]]
  unittest.main()

 if (options.lists_of_ntuples): lists_of_ntuples=options.lists_of_ntuples 
 if (options.default_ini): default_ini=options.default_ini
 if (options.user_ini): user_ini=options.user_ini
 if (options.nosystem): nosystem=options.nosystem


### Begin of the main loop #####
 config=Configurator()
 (scenario,systematic)=config.ReadIni(default_ini,user_ini)
 fU=FileUtils()
 filelists=fU.GetListOfFiles(lists_of_ntuples)
 tF=Transformer(r'(.*/)(.*?)_(.*)(\.txt)', r'\3')
 if (systematic): systematic=systematic.split("_")
 else: systematic=[nosystem]
 mylooper=Looper([str(scenario)],"echo")
 mylooper1=Looper(filelists,"echo","",True)
 mylooper1.SetTransformers([tF])
 inifiles=fU.GetListOfFiles("*"+default_ini+"*")  
 inifiles+=fU.GetListOfFiles("*"+user_ini+"*")  
 if (str(systematic[0]).lower()=="all"):   
  if (len(inifiles)>0): mylooper1.AddExternalExecutors([ExternalAction("cp %s ."%file,2) for file in inifiles] )
  mylooper1.AddExternalExecutors([ExternalAction("cp %s theMergeList.txt",2)])
  mylooper2=Looper(systematic_type[:-1],"echo")
  mylooper3=Looper(systematic_direction,"echo")
  mylooper2.AddInternalExecutors([InternalAction(user_ini,["TripleBtagAnalysis_SF_SystematicUncertainties","Name",user_ini],1)])
  mylooper3.AddInternalExecutors([InternalAction(user_ini,["TripleBtagAnalysis_SF_SystematicUncertainties","direction",user_ini],0)])
  mylooper2.SetInnerLoop(mylooper3) 
  mylooper1.SetInnerLoop(mylooper2) 
 elif  str(systematic[0]).lower() in [str(c).lower() for c in systematic_type[:-1] ]:
  if (len(inifiles)>0): mylooper1.AddExternalExecutors([ExternalAction("cp %s ."%file,2) for file in inifiles] )
  mylooper1.AddExternalExecutors([ExternalAction("cp %s theMergeList.txt",2)])
  mylooper2=Looper([systematic[0]],"echo")
  mylooper3=Looper([systematic[1]],"echo")
  mylooper2.SetInnerLoop(mylooper3)
  mylooper1.SetInnerLoop(mylooper2)
 else :
  if (len(inifiles)>0): mylooper1.AddExternalExecutors([ExternalAction("cp %s ."%file,1) for file in inifiles] )
  mylooper1.AddExternalExecutors([ExternalAction("cp %s theMergeList.txt",1)])
  mylooper2=Looper([systematic[0]],"echo")
  mylooper1.SetInnerLoop(mylooper2)
 mylooper.SetInnerLoop(mylooper1) 
 mylooper.Runloop()

