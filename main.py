#!/usr/bin/env python

""" Program used to automatically reconnect to wifi. Clean, easy and no useless stuff. (Makes no coffee ;( )"""

# Importing sys
from distutils.cmd import Command
import sys

# Importing pygame
import pygame

# Imports connection module
from modules import Connection
from modules import Application

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
    
    # Defining onReconnection and onPacketSent
    onReconnection = lambda: app.event_generate("<<reconnection>>")
    onPacketSent =  lambda: app.event_generate("<<packetSent>>")

    # Creates a new connection on a separate thread
    connection = Connection(loginUrl, pingHost, username, password, onReconnection, onPacketSent)

    def onButtonAPress():
        # Change Text
        app.widgets["buttonA"].configure(text = "START" if app.widgets["buttonA"]["text"] == "STOP" else "STOP")

        # Pause or unpause 
        connection.pause()

    # Adding button functions
    app.widgets["buttonA"].configure(command=onButtonAPress)
    app.widgets["buttonB"].configure(command=sys.exit)



    app.mainloop()
    sys.exit()

 
if __name__ == "__main__":
    
    # Dormitory web url
    loginUrl = "http://192.168.55.250/redirect.cgi?arip=www.gstatic.com&original_url=http%3A%2F%2Fwww.gstatic.com%2Fgenerate%5F204"
    pingHost = "8.8.8.8" # This is a google host

    # Reading login data from file
    loginData = None
    with open("loginData.txt", "r") as f:
        loginData = [d.strip() for d in f.readlines()]

    # Launching program
    main(loginUrl, pingHost, loginData[0], loginData[1])