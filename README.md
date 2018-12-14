# Google Pixel File Redater
I don't have a creative name but oh well. In a nutshell, it takes files in the format of Screenshot_YYYY-MM-DD-hh-mm-ss and uses the file name to change the 'Last Modified' meta tag on them.

# Why?
The Google Pixel automatically dates and names every single photo or video taken in a very beautiful manner, down to the last second. However, it does not have meta tag for photo taken and only relies on the last modified date. Thus, on Google Photos, with the thousands of screenshots of my beloved girlfriend, it would be tedious to sit down and reorganize every single photo.

# How?
Simply take all the screenshots and place them into one folder along with EXIF.py then run python3 EXIF.py and Python will automatically sort and redate every single file inside of the directory.

# Foreword
This code is a baseline and can always be changed to include different file formats, different filenames, and different datings.

