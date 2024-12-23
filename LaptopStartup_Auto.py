import vinDateTime
import vinTextFiles
import vinInternet
import vinAppWindows
import Settings.Settings as Settings
import Settings.List as a
import AppData.LaptopStartup_Main as b
### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ###

def RUN_APP():
    # daily 1/2
    b.openApps(a.DAILY_APPS)

    # weekly
    b.openFolder_ifMatch(a.WEEKLY_FOLDERS, dateTimeW[-1])
    b.openSite_ifMatch(a.WEEKLY_SITES, dateTimeW[-1])

    # monthly
    b.openSite_ifMatch(a.MONTHLY_SITES, dateTimeW[6:8])

    # quarterly
    b.openFolder_ifMatch(a.QUARTERLY_FOLDERS, dateTimeW[4:8])
    b.openSite_ifMatch(a.QUARTERLY_SITES, dateTimeW[4:8])

    #yearly
    b.openSite_ifMatch(a.YEARLY_SITES, dateTimeW[4:8])

    # daily 2/2
    b.openSites(a.DAILY_SITES)
    if not vinAppWindows.getWindow_regex("Microsoft Teams", activate=False):
        vinInternet.sleep(1)
        vinAppWindows.getWindow_regex("Microsoft Teams", activate=False)

### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ###

def checkInternet():
    if not vinInternet.checkInternetConnection():
        print("No internet connection found.")
        vinInternet.waitForInternetConnection()
        print("Internet connection found.")

dateTimeW = vinDateTime.getDateTimeWeekday()
if int(dateTimeW[8:12]) > int(Settings.startAppAfterTime):
    lastDate = vinTextFiles.readFile(Settings.lastDate_filePath)
    if dateTimeW[0:8] != lastDate:
        vinTextFiles.writeFile(Settings.lastDate_filePath, dateTimeW[0:8])
        checkInternet()
        RUN_APP()
