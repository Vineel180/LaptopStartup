import vinTerminalFormatting as f
import vinDateTime
import vinTextFiles
import Settings.Settings as Settings

dateTimeW = vinDateTime.getDateTimeWeekday()

if int(dateTimeW[8:10]) > 2:
    lastDate = vinTextFiles.readFile(Settings.lastDate_filePath)
    if dateTimeW[0:9] != lastDate:
        vinTextFiles.writeFile(Settings.lastDate_filePath, dateTimeW[0:9])