import AppData.LaptopStartup_Main as b
import Settings.List as a

print("0: Tick tick. 1: Daily. 2: Weekly. 3: Monthly. 4: Quarterly. 5: Yearly.")
userInput = list(input("Input: "))

if "1" in userInput:
    b.openApps(a.DAILY_APPS)
if "2" in userInput:
    b.openAllFolders(a.WEEKLY_FOLDERS)
    b.openAllSites(a.WEEKLY_SITES)
if "3" in userInput:
    b.openAllSites(a.MONTHLY_SITES)
if "4" in userInput:
    b.openAllFolders(a.QUARTERLY_FOLDERS)
    b.openAllSites(a.QUARTERLY_SITES)
if "5" in userInput:
    b.openAllSites(a.YEARLY_SITES)
if "1" in userInput:
    b.openSites(a.DAILY_SITES)
    b.getMsTeams()

if "0" in userInput:
    b.openTickTick()
