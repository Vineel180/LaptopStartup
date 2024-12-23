from webbrowser import open as openSite
from os import startfile as openFolder
from subprocess import run

def openSites(List):
    for i in List:
        openSite(i)

def openApp(i):
    run(i, shell=True)
def openApps(List):
    for i in List:
        openApp(i)

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
