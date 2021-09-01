import os
import tkinter as Tkinter
from tkinter import filedialog
import random
import time
import shutil
import ntpath
ptriggers = os.listdir(r"nerd stuff dont look u nerd/triggers")
pevents = "nerd stuff dont look u nerd/events"
template = "nerd stuff dont look u nerd/template"
pcustoms = "nerd stuff dont look u nerd/customs"


dest = r"C:\Users\david\AppData\Roaming\.minecraft\saves\MinecraftBut"



triggers = [
]

events = [
]

customs = [
]




for file in os.listdir(r"nerd stuff dont look u nerd/triggers"):
    if file != "template":
        triggers.append(file)

for file in os.listdir(r"nerd stuff dont look u nerd/events"):
    if file != "template":
        events.append(file)

for file in os.listdir(r"nerd stuff dont look u nerd/customs"):
    if file != "template":
        customs.append(file)
blacklist = []



def cloneDatapack():

    shutil.copytree(template,dest)

def lineprint(table):
    for i in table:
        print(i)


def goodCopy(src, destr):
    if not os.path.exists(destr):
        shutil.copyfile(src, destr)

def goodTree(src, destr):
    if not os.path.exists(destr):
        shutil.copytree(src, destr)

def isCommand(string):
    commands = [
        "setworld",
        "generate",
        "clear"
    ]
    triggers = []
    events = []
    customs = []
    blacklist = []
   # if os.path.exists(os.path.join(dest,"blacklist.txt")):
        #eblacklist = open(os.path.join(dest,"blacklist.txt"))

        #for line in eblacklist:
            #blacklist.append(line)
        #eblacklist.close()
    for file in os.listdir(r"nerd stuff dont look u nerd/triggers"):
        if file != "template":

            triggers.append(file)

    for file in os.listdir(r"nerd stuff dont look u nerd/events"):
        if file != "template":

            events.append(file)

    for file in os.listdir(r"nerd stuff dont look u nerd/customs"):
        if file != "template":

            customs.append(file)
            triggers.append(file)
    stringsplit = string.split()
    if stringsplit[0] == "generate":
        #This is where the real fun begins.
        print("Generating challenge")

        if stringsplit[1]:
            x = int(stringsplit[1])

        if os.path.exists(os.path.join(dest)):
            while (x > 0):
                getRandomChallenge()
                x = x - 1
        else:
            cloneDatapack()
            getRandomChallenge()
    if stringsplit[0] == "dgenerate":
        #This is where the real fun begins.
        print("Generating challenge")
        try:
            shutil.rmtree(dest)
        except:
            print("ERROR. ANOTHER PROCESS IS USING THE DATAPACK.")
        cloneDatapack()
        if stringsplit[1]:
            x = int(stringsplit[1])

        if os.path.exists(os.path.join(dest)):
            while (x > 0):
                getRandomChallenge()
                x = x - 1
        else:
            cloneDatapack()
            getRandomChallenge()
    if stringsplit[0] == "custom":
        #This is where the real fun begins.
        print("Generating CUSTOM challenge")

        if len(stringsplit) == 2:
            stringsplit.append("none")
        if os.path.exists(os.path.join(dest)):
            getRandomChallenge(stringsplit[1],stringsplit[2])
        else:
            cloneDatapack()
            getRandomChallenge(stringsplit[1],stringsplit[2])
    if stringsplit[0] == "customd":
        #This is where the real fun begins.
        print("Generating CUSTOM challenge and DELETING other datapacks.")
        try:
            shutil.rmtree(dest)
        except:
            print("ERROR. ANOTHER PROCESS IS USING THE DATAPACK.")
        cloneDatapack()
        if len(stringsplit) == 2:
            stringsplit.append("none")
        if os.path.exists(os.path.join(dest)):
            getRandomChallenge(stringsplit[1],stringsplit[2])
        else:
            cloneDatapack()
            getRandomChallenge(stringsplit[1],stringsplit[2])



def getRandomChallenge(trigger="none", event="none"):
    triggerpath = os.path.join("nerd stuff dont look u nerd", "triggers")
    eventspath = os.path.join("nerd stuff dont look u nerd", "events")

    if trigger != "none" and event == "none":
        #its a custom
        triggerpath = os.path.join("nerd stuff dont look u nerd", "customs")
        trigger = os.path.join(triggerpath, trigger)


    elif trigger == "none" and event == "none":
        #in this case, the getRandomChallenge function was called with the intent of generating random challenges(no arguements where specified)
        numee = triggers[random.randint(0,len(triggers)-1)]
        trigger = os.path.join(triggerpath, numee)
        event = os.path.join(eventspath, events[random.randint(0, len(events) - 1)])

       # print(trigger + "DSA ASD")
    else:
        #arugements were given
        trigger = os.path.join(triggerpath, trigger)

        event = os.path.join(eventspath, event)






    dest_a = os.path.join(dest,"data","mcbut")
    ##Get display
    display = ""
    displayt = open(os.path.join(trigger,"display.txt"),"r")
    eventdisplay = ""
    if event != "none":
        displaye = open(os.path.join(event,"display.txt"),"r")
        for line in displaye:
            eventdisplay = line
        displaye.close()
    triggerdisplay = ""

    for line in displayt:
        triggerdisplay = line

    displayt.close()

    if event != "none":
        display = "Minecraft, but " + triggerdisplay + ", " + eventdisplay
    else:

        display = "Minecraft, but " + triggerdisplay

    lineprint([
        "===================",
        display,
        "=================="
    ])
    if event != "none":
        goodTree(event,os.path.join(dest_a,"functions",ntpath.basename(event)))
        init = open(os.path.join(event, "init.mcfunction"), "r")
        dinit = open(os.path.join(dest_a, "functions", "init.mcfunction"), "a")

        dinit.write("\n")
        for line in init:
            dinit.write("\n")
            dinit.write(line)
            dinit.write("\n")
        dinit.close()
        init.close()
        main = open(os.path.join(event, "main.mcfunction"), "r")
        dmain = open(os.path.join(dest_a, "functions", "main.mcfunction"), "a")
        for line in main:
            dmain.write("\n")
            dmain.write(line)
            dmain.write("\n")
        dmain.close()
        main.close()
    ######################################################################

    init = open(os.path.join(trigger,"init.mcfunction"),"r")
    dinit = open(os.path.join(dest_a, "functions","init.mcfunction"),"a")
    dinit.write("say " + display)
    dinit.write("\n")
    for line in init:
        dinit.write("\n")
        dinit.write(line)
        dinit.write("\n")
    dinit.close()
    init.close()
    main = open(os.path.join(trigger,"main.mcfunction"),"r")
    dmain = open(os.path.join(dest_a, "functions","main.mcfunction"),"a")
    for line in main:
        dmain.write("\n")
        dmain.write(line)
        dmain.write("\n")
    dmain.close()
    main.close()
    if event != "none":
        for file in os.listdir(os.path.join(event,"pred")):
            goodCopy(os.path.join(event,"pred",file),os.path.join(dest_a,"predicates",ntpath.basename(file)))
            for file in os.listdir(os.path.join(event, "loot_tables")):
                goodCopy(os.path.join(event, "loot_tables", file), os.path.join(dest_a, "loot_tables", ntpath.basename(file)))

    for file in os.listdir(os.path.join(trigger,"advancements")):
        goodCopy(os.path.join(trigger,"advancements",file),os.path.join(dest_a,"advancements",ntpath.basename(file)))
    for file in os.listdir(os.path.join(trigger,"predicates")):
        goodCopy(os.path.join(trigger,"predicates",file),os.path.join(dest_a,"predicates",ntpath.basename(file)))
    for file in os.listdir(os.path.join(trigger,"loot_tables")):
        goodCopy(os.path.join(trigger,"loot_tables",file),os.path.join(dest_a,"loot_tables",ntpath.basename(file)))
    for file in os.listdir(os.path.join(trigger,"mloot_tables")):
        goodTree(os.path.join(trigger,"mloot_tables",file),os.path.join(os.path.join(dest,"data","minecraft"),"loot_tables",ntpath.basename(file)))
    if not os.path.exists(os.path.join(dest_a,"functions",ntpath.basename(trigger))):
        os.mkdir(os.path.join(dest_a,"functions",ntpath.basename(trigger)))
    for file in os.listdir(os.path.join(trigger,"inserts")):
        goodCopy(os.path.join(trigger,"inserts",file),os.path.join(dest_a,"functions",ntpath.basename(trigger),ntpath.basename(file)))
        pathrr = os.path.join(dest_a,"functions",ntpath.basename(trigger),ntpath.basename(file))
        if event != "none":
            if ntpath.basename(pathrr) == "bridge.mcfunction":
                bridge = open(pathrr,'a')
                bridge.write("\n")
                bridge.write("execute at @s run function mcbut:" + ntpath.basename(event) + "/action")
                bridge.close()

    for file in os.listdir(os.path.join(trigger,"tags","blocks")):
       goodCopy(os.path.join(trigger,"tags","blocks",file),os.path.join(dest_a,"tags","blocks",ntpath.basename(file)))

    for file in os.listdir(os.path.join(trigger,"tags","entity_types")):
        goodCopy(os.path.join(trigger,"tags","entity_types",file),os.path.join(dest_a,"tags","entity_types",ntpath.basename(file)))




lineprint([
    "================================",
    "Welcome to the \"Minecraft But Challenge Generator\"",
    "================================",
    "Please select a world file to start.",
    "================================",
    "Type \"setworld\" at any time to set your world file to something else."
])

#time.sleep(1.5)
#root = Tkinter.Tk(screenName="Choose a file u nerd",baseName="fileee",useTk=True)
#root.geometry("0x0")
#dest = filedialog.askdirectory(parent=root,initialdir=os.path.join(os.getenv("APPDATA"),".minecraft","saves"))
#root.destroy()

#clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#clearConsole()
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
