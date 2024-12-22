import vinDateTime
import vinTextFiles
import Settings.Settings as Settings
import Settings.List as a
import AppData.LaptopStartup_Main as b


dateTimeW = vinDateTime.getDateTimeWeekday()
if int(dateTimeW[8:12]) > int(Settings.startAppAfterTime):
    lastDate = vinTextFiles.readFile(Settings.lastDate_filePath)
    if dateTimeW[0:8] != lastDate:
        vinTextFiles.writeFile(Settings.lastDate_filePath, dateTimeW[0:8])

        # daily
        b.openSites(a.DAILY_SITES)
        b.openApps(a.DAILY_APPS)
