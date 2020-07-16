#! /usr/bin/python3

from tkinter import Tk
#from tkinter import messagebox
#from functools import partial
#import os
#import time
import datetime

# Initial variables - Start
timeNow = datetime.datetime.now()
writeYear = 2020 # Enter the year you started writing the program
lineFeed = "\n"
programTitle = "NordVPN Controller"
programVersion = "Version 1.0.0" # New GUI layout
programmerName = " David Brown (rpitns@gmail.com)"
if timeNow.year > writeYear:
    programAuthor = "©" + str(writeYear) + "-" + str(timeNow.year) + programmerName
else:
    programAuthor = "©" + str(writeYear) + programmerName
aboutMessage = programTitle + lineFeed + programVersion + lineFeed + programAuthor
print(aboutMessage) #Debug
# Initial variables - End


# Main program - Start
root = Tk() # root window created. Here, that would be the only window, but
            # you can later have windows within windows.
windowHeight = int(root.winfo_screenheight()/100*75) # Set the main window height to 75% of the screen height
windowWidth = int(root.winfo_screenwidth()/100*75) # Set the main window width to 75% of the screen width

screenWidth = int(root.winfo_screenwidth())
screenHeight = int(root.winfo_screenheight())
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2) # Get the screen width and divide by 2, then minus the result of 'windowWidth' divided by 2
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2) # Get the screen height and divide by 2, then minus the result of 'windowHeight' divided by 2
print ("Screen size = {}w by {}h".format(screenWidth, screenHeight))
print ("Window size = {}w by {}h".format(windowWidth, windowHeight))
print ("Screen position {} right, {} down".format(positionRight, positionDown))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown)) # Positions the window in the center of the page.

#app = Window(root)
#root.mainloop()
# Main program - Start