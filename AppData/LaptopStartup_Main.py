from subprocess import run
import vinInternet
import vinAppWindows
import vinTaskManager

# for AUTO and MANUAL
from webbrowser import open as openSite
from os import startfile as openFolder
def openApp(i):
    run(i, shell=True)

def openSites(List):
    for i in List:
        openSite(i)
def openApps(List):
    for i in List:
        openApp(i)

def getMsTeams():
    if not vinAppWindows.getWindow_regex("Microsoft Teams", activate=False):
        vinInternet.sleep(1)
        vinAppWindows.getWindow_regex("Microsoft Teams", activate=False)

def openTickTick():
    if not vinAppWindows.getWindow("Tick Tick"):
        if vinTaskManager.isAppRunning("TickTick.exe"):
            vinTaskManager.stopApp("TickTick.exe")
            openApp(r"start ticktick://")
        else:
            openApp(r"start ticktick://")

def checkInternet():
    if not vinInternet.checkInternetConnection():
        print("Laptop Startup.py: No internet connection found.")
        vinInternet.waitForInternetConnection()
        print("Internet connection found.")

# for AUTO only
def openFolder_ifMatch(List, dataToMatch):
    for i in List:
        if i[0] == dataToMatch:
            openFolder(i[1])
def openSite_ifMatch(List, dataToMatch):
    for i in List:
        if i[0] == dataToMatch:
            openSite(i[1])

def toQuarterlyFormat(Input):
    Input0 = int(Input[0:2])
    #
    if Input0 % 3 == 1:
        Input0 = "A"
    elif Input0 % 3 == 2:
        Input0 = "B"
    else:
        Input0 = "C"
    #
    return Input0 + Input[2:]

# for MANUAL only
def openAllFolders(List):
    for i in List:
        openFolder(i[1])
def openAllSites(List):
    for i in List:
        openSite(i[1])
