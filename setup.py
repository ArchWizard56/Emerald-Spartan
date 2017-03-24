#import dependencies
import  pickle
import os
import sys
from Helpers.pickleVariable import pickleVariable
#open pickle file()
try:
    file = open("UserVariables.p", "r+b")
    reset = input("We detected preferences already filled in. Do you want to reset those preferences? (Proceding may break things) y to reset No to continue or exit to exit")
    if input == "y" or "Y" or "Yes":
        file.close()
        os.remove("UserVariables.p")
        file = open("UserVariables.p", "xb")   
        file.close()
        file = open("UserVariables.p", "r+b")
    elif input == "exit" or "Exit" or "Quit" or "quit":
        sys.exit("Exiting")
    elif input == "No" or "no":
        print("Continuing")

    else:
        print("please enter y, no, or exit")
except FileNotFoundError:
    file = open("UserVariables.p", "xb")
    file.close()
    file = open("UserVariables.p", "r+b")
#define setVars(to minimize repeats)
def setVars(default, question):
    #ask question
    var = input(question + " (default is " + default +")")
    #test if blank input was given. If so set it to default
    if var == "":
        var = default
    #return answer
    return var
#begin setting variables
#Ask where the minecraft install location is
minecraftLocation = pickleVariable("minecraftLocation", setVars("Minecraft/", "Please enter the location of your minecraft server install"))
#pickle answer
pickle.dump(minecraftLocation, file, -1)
print("Set to " + minecraftLocation.value)
#ask the name of the minecraft jar
minecraftJarName = pickleVariable("minecraftJarName",setVars("Minecraft.jar", "Please enter the name of your server jar"))
#pickle answer
pickle.dump(minecraftJarName, file, -1)
print("set to " + minecraftJarName.value)
#Ask for the starting ram for minecraft
Xms = pickleVariable("Xms", setVars("512M", "Please enter how much ram your server will start with. example: 512M or 1G "))
#pickle answer
pickle.dump(Xms, file, -1)
print("Set to " + Xms.value)
#Ask for the maximum amount of ram to start minecraft with
Xmx = pickleVariable("Xmx", setVars("1G", "Please enter the maximum amount of ram your server can use. example: 512M or 1G "))
#pickle answer
pickle.dump(Xmx, file, -1)
print("Set to " + Xmx.value)


file.close()