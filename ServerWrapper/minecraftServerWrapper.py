'''
Created on Mar 23, 2017

@author: ArchWizard
At the moment this is only a wrapper for bash however next it will be
a wrapper for the minecraft server. Then the master I/O port for the minecraft server! 
'''
# Import Dependices
import pickle
import subprocess
import threading
from time import sleep
from Helpers.pickleloader import pickleloader
import pexpect
import sys
#define where variables are
UserVars = "../UserVariables.p"
#extract Variables from pickle
minecraftLocation = pickleloader("minecraftLocation", UserVars)
minecraftJarName = pickleloader("minecraftJarName", UserVars)
Xms = pickleloader("Xms", UserVars)
Xmx = pickleloader("Xmx", UserVars)
#Spawn the child process
minecraftServer = pexpect.spawn("/bin/bash")
class Monitor(threading.Thread):
    def run(self):
            #Grab the stdout line as it becomes available
            #this will loop until the process terminates
            while minecraftServer is not None:
                for line in minecraftServer:
                    print(line)
#Have Monitor thread exit on program exit
Monitor.daemon = True
#Start the Monitor thread
Monitor().start()
#main debug loop
while True:
    #ask for user input
    command = input("\n Please enter a bash command >>> ")
    #allowing for a clear exit
    if command == "exit":
        Monitor()._stop()
        sys.exit("Exiting")
    #send the command to the server    
    minecraftServer.sendline(command)





