#! /usr/bin/python3
# Thanks to Bryan Oakley (https://stackoverflow.com/users/7432/bryan-oakley) for the info on frames. See https://stackoverflow.com/a/60195495/12887659
#from tkinter import Tk, Frame, BOTH, Menu, messagebox, window
from tkinter import *
from tkinter import messagebox
from functools import partial
import os
import time
import datetime

# Initial variables - Start
timeNow = datetime.datetime.now()
writeYear = 2020 # Enter the year you started writing the program
lineFeed = "\n"
programTitle = "NordVPN Controller"
programVersion = "Version 1.0.0" # New GUI layout
programVersion = "Version 1.0.1" # Added Menu
programVersion = "Version 1.0.2" # Changes to about and exit boxes
programVersion = "Version 1.0.3" # Login section. Needs status message boxes
programVersion = "Version 1.0.4" # Added Status, Needs status messages
programmerName = " David Brown (rpitns@gmail.com)"
if timeNow.year > writeYear:
    programAuthor = "©" + str(writeYear) + "-" + str(timeNow.year) + programmerName
else:
    programAuthor = "©" + str(writeYear) + programmerName
aboutMessage = programTitle + lineFeed + programVersion + lineFeed + programAuthor
print(aboutMessage) #Debug
#userName = ""
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
        fileMainMenu.add_command(label="Status", command=self.vpnStatus)
        fileMainMenu.add_separator()
        fileMainMenu.add_command(label="Login", command=self.vpnLogin)
        fileMainMenu.add_command(label="Logout", command=self.vpnLogout)
        fileMainMenu.add_separator()
        fileMainMenu.add_command(label="Connect", command=self.vpnConnect)
        fileMainMenu.add_command(label="Disconnect", command=self.vpnDisconnect)
        fileMainMenu.add_separator()
        fileMainMenu.add_command(label="Exit", command=self.programExit) # File menu option
        menu.add_cascade(label="File", menu=fileMainMenu)
        
        helpMainMenu = Menu(menu, tearoff=0) #Create the Help menu container
        helpMainMenu.add_command(label="About", command=self.aboutProgram)
        menu.add_cascade(label="Help", menu=helpMainMenu)
        # create menu instance - End
        

    # Menu commands - Start
    def vpnStatus(self):
        o=os.popen('nordvpn status').read()
        statusFrame = Frame(self.master, bd=10, relief="groove")
        statusLabel1 = Label(statusFrame, text="{} Status".format(programTitle), font=("Helvetica", 16, "bold italic"))
        statusLabel2 = Label(statusFrame, text="{}".format(o), font=("Helvetica", 14))
        statusLabel1.grid(row=1, columnspan=3, padx=20, pady=20)
        statusLabel2.grid(row=2, columnspan=3, padx=20, pady=20)
        statusButton1 = Button(statusFrame, text="Ok", command=statusFrame.destroy)
        statusButton1.grid(row=4,column=1)
        statusFrame.place(relx=.5, rely=.5, anchor="c")
        statusFrame.grab_set()
        print(o)
    def vpnLogin(self):
        global loginFrame
        global userName
        global passWord
        global usernameEntry
        global passwordEntry
        # create the frame with a message and two buttons
        # which destroys the window
        loginFrame = Frame(self.master, bd=10, relief="groove")
        loginLabel1 = Label(loginFrame, text="Account Login\n\n", font=("Helvetica", 16, "bold italic"))
        loginLabel2 = Label(loginFrame, text="Username:", font=("Helvetica", 14))
        loginLabel3 = Label(loginFrame, text="Password:", font=("Helvetica", 14))
        loginLabel1.grid(row=1, columnspan=3, padx=20, pady=20)
        loginLabel2.grid(row=2, column=1, padx=20, pady=20)
        loginLabel3.grid(row=3, column=1, padx=20, pady=20)
        userName = StringVar()
        passWord = StringVar()
        usernameEntry = Entry(loginFrame, textvariable=userName).grid(row=2, column=2)
        passwordEntry = Entry(loginFrame, textvariable=passWord, show= '*').grid(row=3, column=2)
        loginButton1 = Button(loginFrame, text="Cancel", command=loginFrame.destroy)
        loginButton1.grid(row=4,column=2)
        #loginButton2 = Button(loginFrame, text="Login", command=self.loginCommand(userName,passWord))
        loginButton2 = Button(loginFrame, text="Login", command=self.loginCommand)
        # button2.pack(side="left", pady=20)
        loginButton2.grid(row=4,column=1)

        # overlay the "login" page on top of the root window
        loginFrame.place(relx=.5, rely=.5, anchor="c")
        #aboutFrame.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0) #If you want to completely hide the contents of the main window, you can change the place arguments to fill the window
        # force all events to go to the popup
        loginFrame.grab_set()
        
    def vpnLogout(self):
        global logoutFrame
        logoutFrame = Frame(self.master, bd=10, relief="groove")
        logoutLabel1 = Label(logoutFrame, text="Logout\n\n", font=("Helvetica", 16, "bold italic"))
        logoutLabel2 = Label(logoutFrame, text="Are you sure you want to logout of {}?".format(programTitle), font=("Helvetica", 14))
        logoutLabel1.grid(row=1, columnspan=2, padx=20, pady=20)
        logoutLabel2.grid(row=2, columnspan=2, padx=20, pady=20)
        logoutButton1 = Button(logoutFrame, text="No", command=logoutFrame.destroy)
        logoutButton1.grid(row=3,column=0)
        logoutButton2 = Button(logoutFrame, text="Yes", command=self.logoutCommand)
        logoutButton2.grid(row=3,column=1)
        logoutFrame.place(relx=.5, rely=.5, anchor="c")
        logoutFrame.grab_set()

    def vpnConnect(self):
        print("Connect")

    def vpnDisconnect(self):
        print("Disconnect")

    def programExit(self):
        # create the frame with a message and two buttons
        # which destroys the window
        exitFrame = Frame(self.master, bd=10, relief="groove")
        label1 = Label(exitFrame, text="Exit Application", font=("Helvetica", 16, "bold italic"))
        label2 = Label(exitFrame, text="Are you sure you want to exit {}?".format(programTitle), font=("Helvetica", 14))
        
        #label1.pack(side="top", padx=20, pady=20)
        label1.grid(row=1, columnspan=2, padx=20, pady=20)
        label2.grid(row=2, columnspan=2, padx=20, pady=20)
        #label2.pack(side="top", padx=20, pady=20)
        button1 = Button(exitFrame, text="No", command=exitFrame.destroy)
        # button1.pack(side="left", pady=20)
        button1.grid(row=3,column=0)
        button2 = Button(exitFrame, text="Yes", command=self.exitCommand)
        # button2.pack(side="left", pady=20)
        button2.grid(row=3,column=1)

        # overlay the "about" page on top of the root window
        exitFrame.place(relx=.5, rely=.5, anchor="c")
        #aboutFrame.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0) #If you want to completely hide the contents of the main window, you can change the place arguments to fill the window
        # force all events to go to the popup
        exitFrame.grab_set()
        
    def aboutProgram(self):
        # create the frame with a message and a button
        # which destroys the window
        aboutFrame = Frame(self.master, bd=10, relief="groove")
        label1 = Label(aboutFrame, text="About the application...", font=("Helvetica", 16, "bold italic"))
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
    def programStatus(self):
        global status
        global statusFrame
        status = statusMessage
        # create the frame with a message and a button
        # which destroys the window
        statusFrame = Frame(self.master, bd=10, relief="groove")
        statusLabel1 = Label(statusFrame, text="Status...", font=("Helvetica", 16, "bold italic"))
        statusLabel2 = Label(statusFrame, text="{}".format(status), font=("Helvetica", 14))
        statusButton = Button(statusFrame, text="Ok", command=self.statusExit)
        statusLabel1.pack(side="top", padx=20, pady=20)
        statusLabel2.pack(side="top", padx=20, pady=20)
        statusButton.pack(side="bottom", pady=20)

        # overlay the "about" page on top of the root window
        statusFrame.place(relx=.5, rely=.5, anchor="c")
        #aboutFrame.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0) #If you want to completely hide the contents of the main window, you can change the place arguments to fill the window
        # force all events to go to the popup
        statusFrame.grab_set()
    def statusExit(self):
        statusFrame.destroy()
        if status == "Username or password is not correct. Please try again.":
            self.vpnLogin()
    def loginCommand(self):
        global statusMessage
        #print("Login command reached")
        #print(userName)
        #print("Login Command Username: {}".format(userName))
        userName1 = userName.get()
        passWord1 = passWord.get()
        #print("After Get - Username: {}".format(username1))
        #print("After Get - Password: {}".format(password1))
        #print("nordvpn login -u {} -p {}".format(userName1, passWord1))
        loginFrame.destroy()
        o=os.popen("nordvpn login -u {} -p {}".format(userName1, passWord1)).read()
        #while "Status: Disonnected" in o:
        #    time.sleep(5)
        #    o=os.popen('nordvpn status').read()
        #o = "Welcome to NordVPN! You can now connect to VPN by using 'nordvpn connect'."
        if "You are already logged in." in o:
            print("You are already logged in. You can now connect to the VPN")
            statusMessage = "You are already logged in. You can now connect to the VPN"
        elif "Welcome to NordVPN!" in o:
            print("Welcome to NordVPN! You can now connect to the VPN")
            statusMessage = "Welcome to NordVPN! You can now connect to the VPN"
        else:
            print("Username or password is not correct. Please try again.")
            statusMessage = "Username or password is not correct. Please try again."
        self.programStatus()
        #wait_window(statusFrame) 
        #if statusMessage == "Username or password is not correct. Please try again.":
        #    self.vpnLogin()
    def logoutCommand(self):
        global statusMessage
        o=os.popen('nordvpn logout').read()
        logoutFrame.destroy()
        if "You are logged out" in o:
            print("You are now logged out.")
            statusMessage = "You are now logged out."
        elif "You are not logged in" in o:
            print ("You are already logged out.")
            statusMessage = "You are already logged out."
        else:
            print("Unknown error")
            statusMessage = "Unknown error"
        self.programStatus()
        
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
