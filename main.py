#!/usr/bin/env python

""" Program used to automatically reconnect to wifi. Clean, easy and no useless stuff. (Makes no coffee ;( )"""

# Importing sys
import sys

# Imports connection module
from modules import Connection
from modules import Application
from modules import DebugConsole

# Header
__author__ = "Alkhasar"
__copyright__ = "Copyright di mago merlino, non può essere infranto"
__credits__ = ["Alkhasar", "IlMistico"]
__version__ = "2.0.0"
__status__ = "Prototype"

def main(loginUrl, pingHost, username, password):
    """ Program main loop, quits on user interaction

    Args:
        loginUrl (string): url to connection provider
        pingHost (string): ip to a ping host (usually google)
        username (string): username used to login
        password (string): password used to login
    """

    # Application Instance
    app = Application()

    
    # Debug Console instance
    console = DebugConsole()
    
    # Defining onReconnection and onPacketSent
    onReconnection = lambda: app.event_generate("<<reconnection>>")
    onPacketSent =  lambda: app.event_generate("<<packetSent>>")
    onShutDown =  lambda: app.event_generate("<<shutdown>>")

    # Creates a new connection on a separate thread
    connection = Connection(loginUrl, pingHost, username, password, onReconnection, onPacketSent, onShutDown)

    def onButtonAPress():
        # Change Text
        app.widgets["buttonA"].configure(text = "START" if app.widgets["buttonA"]["text"] == "STOP" else "STOP")

        # Pause or unpause 
        pause = connection.pause()

        # Logging
        console.log("Program stopped" if pause else "Program started")
    
    def onExit():
        # Loggin program shutdown
        console.log("Program Shutdown")

        # Saving logfle
        console.saveLog()

        # Closing application
        sys.exit()
    
    # Binding shutdown event
    app.bind("<<shutdown>>", onExit)
        
    # Adding button functions
    app.widgets["buttonA"].configure(command=onButtonAPress)
    app.widgets["buttonB"].configure(command=onExit)

    # Quitting
    app.mainloop()
    
    # Application closed without closing logfile
    print("WARNING: Application closed without last logLine! Please use QUIT button!")

 
if __name__ == "__main__":

    # Reading login data from file
    loginData = None
    with open("loginData.txt", "r") as f:
        loginData = [d.strip()[(d.strip()).find('=') + 1:] for d in f.readlines()]

    # Launching program
    main(loginData[0], loginData[1], loginData[2], loginData[3])