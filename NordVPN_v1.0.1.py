#! /usr/bin/python3

#from tkinter import Tk, Frame, BOTH, Menu, messagebox, window
from tkinter import *
from tkinter import messagebox
#from functools import partial
#import os
#import time
import datetime

# Initial variables - Start
timeNow = datetime.datetime.now()
writeYear = 2019 # Enter the year you started writing the program
lineFeed = "\n"
programTitle = "NordVPN Controller"
programVersion = "Version 1.0.0" # New GUI layout
programVersion = "Version 1.0.1" # Added Menu
programmerName = " David Brown (rpitns@gmail.com)"
if timeNow.year > writeYear:
    programAuthor = "©" + str(writeYear) + "-" + str(timeNow.year) + programmerName
else:
    programAuthor = "©" + str(writeYear) + programmerName
aboutMessage = programTitle + lineFeed + programVersion + lineFeed + programAuthor
print(aboutMessage) #Debug
# Initial variables - End

# Main class - Start
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
    
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("{} ({})".format(programTitle, programVersion))

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # create menu instance - Start
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        #file.add_command(label="Quick Connect", command=self.nord_qc)
        #file.add_command(label="Login", command=self.nord_login)
        #file.add_command(label="Login")
        #file.add_command(label="Status")
        #file.add_command(label="Disconnect")
        #file.add_command(label="Logout")
        fileMainMenu = Menu(menu, tearoff=0) #Create the File menu container
        fileMainMenu.add_command(label="Exit", command=self.programExit) # File menu option
        menu.add_cascade(label="File", menu=fileMainMenu)
        
        helpMainMenu = Menu(menu, tearoff=0) #Create the Help menu container
        helpMainMenu.add_command(label="About", command=self.aboutProgram)
        menu.add_cascade(label="Help", menu=helpMainMenu)
        # create menu instance - End


    # Menu commands - Start
    def programExit(self):
        #top_frame = tkinter.Frame(window).pack()
        # top_frame = Frame(Window).pack()
        exitMsgBox = messagebox.askquestion ("Exit Application","Are you sure you want to exit the application",icon = "warning")
        if exitMsgBox == "yes":
            root.destroy()
            exit()
    
    def aboutProgram(self):
        # create the frame with a message and a button
        # which destroys the window
        aboutFrame = Frame(self.master, bd=10, relief="groove")
        label1 = Label(aboutFrame, text="About the application...\n\n", font=("Helvetica", 16, "bold italic"))
        label2 = Label(aboutFrame, text="{}".format(aboutMessage), font=("Helvetica", 14))
        button = Button(aboutFrame, text="Ok", command=aboutFrame.destroy)
        label1.pack(side="top", padx=20, pady=20)
        label2.pack(side="top", padx=20, pady=20)
        button.pack(side="bottom", pady=20)

        # overlay the "about" page on top of the root window
        aboutFrame.place(relx=.5, rely=.5, anchor="c")
        #aboutFrame.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0) #If you want to completely hide the contents of the main window, you can change the place arguments to fill the window
        # force all events to go to the popup
        aboutFrame.grab_set()
     def exitCommand(self):
         root.destroy()
         exit()
    # Menu commands - End
    


# Main class - End

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

app = Window(root)
root.mainloop()
# Main program - End
