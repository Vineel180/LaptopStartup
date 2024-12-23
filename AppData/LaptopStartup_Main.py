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
