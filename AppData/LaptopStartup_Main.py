from webbrowser import open as openSite
from subprocess import run

def openSites(List):
    for i in List:
        openSite(i)

def openApp(i):
    run(i, shell=True)
def openApps(List):
    for i in List:
        openApp(i)
