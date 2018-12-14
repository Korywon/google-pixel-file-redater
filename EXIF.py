import os
import datetime
import time

# class to hold the date and time
class DateTime:
        year = 0
        month = 0
        day = 0
        hour = 0
        minute = 0
        second = 0

        # initializes DateTime object
        def __init__(self, inYear, inMonth, inDay, inHour, inMinute, inSecond):
                self.year = int(inYear)
                self.month = int(inMonth)
                self.day = int(inDay)
                self.hour = int(inHour)
                self.minute = int(inMinute)
                self.second = int(inSecond)

        # prints out date and time of object
        def print(self):
                print(self.year, "-", self.month, "-", self.day)
                print(self.hour, ":", self.minute, ":", self.second)

# array to hold the name of each array
fileNames = []

# grabs file names from directory
for root, dirs, files in os.walk("."):
	for filename in files:
                if ".py" not in filename:
                       fileNames.append(filename)

for i in fileNames:
        print(i)
        string = i.replace("Screenshot_", "")
        string = string.replace(".png", "")
        print(string)

        date = DateTime(string[0:4], string[4:6], string[6:8], string[9:11], string[11:13], string[13:15])
        date.print()

        dateTime = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
        modTime = time.mktime(dateTime.timetuple())

        os.utime(i, (modTime, modTime))
        print()

input("Execution finished. Press ENTER to continue...")
