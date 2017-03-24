'''
Created on Mar 23, 2017

@author: ArchWizard
At the moment this is only a wrapper for bash however next it will be
a wrapper for the minecraft server. Then the master I/O port/server for the minecraft server! 
'''
# Import Dependices
import pickle
import subprocess
import threading
from time import sleep
from Helpers.pickleloader import pickleloader
#define where variables are
UserVars = "../UserVariables.p"
#extract Variables from pickle
minecraftLocation = pickleloader("minecraftLocation", UserVars)
minecraftJarName = pickleloader("minecraftJarName", UserVars)
Xms = pickleloader("Xms", UserVars)
Xmx = pickleloader("Xmx", UserVars)
#Create process
process = subprocess.Popen("/bin/bash", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
#p = subprocess.Popen("java -jar -Xms" + Xms, + " -Xmx" +Xmx + " " + minecraftLocation + minecraftJarName + " nogui", stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#Define Monitor thread
class Monitor(threading.Thread):
    def run(self):
            #Grab the stdout line as it becomes available
            #this will loop until the process terminates
            while process.poll() is None:
                mon = process.stdout.readline()
                print(mon)
#Same thing as above but for errors also                
class Monerr(threading.Thread):
    def run(self):
            while process.poll() is None:
                mon = process.stderr.readline()
                print(mon)
#start the threads
Monitor().start()
Monerr().start()
#ask for input
command = input("Please enter a command >>> ")
#write the command to stdin
process._stdin_write(command)
# When the subprocess terminates there might be unconsumed output 
# that still needs to be processed.
print(process.stdout.read())