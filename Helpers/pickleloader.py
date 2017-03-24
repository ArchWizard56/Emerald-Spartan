'''
Created on Mar 23, 2017

@author: ArchWizard
'''
import sys
import pickle
from Helpers.pickleVariable import pickleVariable
def pickleloader(label, file):
    #open the file
    try:
        f = open(file, 'rb')
    #excepting FileNotFound for custom error
    #If the input is not a valid file    
    except FileNotFoundError:
        #exiting and printing custom error
        print("We couldn't find " + file + " please make sure the file has been properly created. Probably by running py.py")
        sys.exit("File not found")
    try:
        #looping through the file
        while True:
            #loading the pickle thing
            var = pickle.load(f)
            #testing if the pickle value is what i'm looking for
            if var.label == label:
                #if so return the value and exit
                return var.value
                sys.exit
    #allowing for invalid label            
    except EOFError:
        #print out custom label
        print("We couldn't find the variable")
        sys.exit("Variable not found")
