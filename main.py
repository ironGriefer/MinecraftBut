'''

This is a idea that I didn't steal from a youtuber or anything.
When you run the program, you can connect it to a minecraft world. Every time you type "generate", it will generate a new "Minecraft But" challenge in the world

'''
import os
import tkinter as Tkinter
from tkinter import filedialog
import random
import time
import shutil
triggers = os.listdir(r"nerd stuff dont look u nerd/triggers")
events = "nerd stuff dont look u nerd/events"
template = "nerd stuff dont look u nerd/template"
#customs = "nerd stuff dont look u nerd/customs"

trigger = ""
event = ""


dest = "result"

blacklist = os.path.join(dest,'blacklist.txt')


triggers = [
]

events = [
]

customs = [
]




for file in os.listdir(r"nerd stuff dont look u nerd/triggers"):
    if file != "template":
        triggers.append(file)
        print(file)

for file in os.listdir(r"nerd stuff dont look u nerd/events"):
    if file != "template":
        events.append(file)

#for file in os.listdir(r"nerd stuff dont look u nerd/customs"):
  #  if file != "template":
      #  customs.append(file)




def cloneDatapack():
    print("copying template")
    shutil.copytree(template,dest)

def lineprint(table):
    for i in table:
        print(i)

def isCommand(string):
    commands = [
        "setworld",
        "generate",
        "clear"
    ]
    if string == "generate":
        #This is where the real fun begins.
        print("Generating challenge")
        if not os.path.exists(os.path.join(dest,"McBut")):
            cloneDatapack()
        getRandomChallenge()
        print(os.path.join("nerd stuff dont look u nerd","triggers",trigger,"init.mcfunction"), trigger, "1")
        #init = open()
       # for line in init:
           # print(line)



def getRandomChallenge():
    trigger = triggers[random.randint(0,len(triggers)-1)]
    print(trigger, "2")
    event = events[random.randint(0,len(events)-1)]


lineprint([
    "================================",
    "Welcome to the \"Minecraft But Challenge Generator\"",
    "================================",
    "Please select a world file to start.",
    "================================",
    "Type \"setworld\" at any time to set your world file to something else."
])
def getUserFile():
    time.sleep(1.5)
    root = Tkinter.Tk(screenName="Choose a file u nerd",baseName="fileee",useTk=True)
    root.geometry("0x0")
    dest = filedialog.askdirectory(parent=root,initialdir=os.path.join(os.getenv("APPDATA"),".minecraft","saves"))
    root.destroy()

#getUserFile()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()
lineprint([
    "Now, type \"generate\" to generate a new challenge. This challenge will be added to the world.",
    "If you want to clear all challenges from a world, type \"clear\""
])
dest = os.path.join(dest,"datapacks","McBut")
while True:
    command = input("Insert Command:   ")
    isCommand(command)




###CLEANUP CLEANUP EVERYBODY CLEAN UP CLEAN UP CLEAN UP EVERYONE DO UR SHARE

#triggers.close()
#events.close()
#template.close()
#customs.close()
