#!/usr/bin/env python

""" Program used to automatically reconnect to wifi. Clean, easy and no useless stuff. (Makes no coffee ;( )"""

# Importing sys
import sys

# Importing pygame
import pygame

# Imports connection module
from modules import Connection
from modules import Button
from modules import CounterText
from modules import Text

# Header
__author__ = "Alkhasar"
__copyright__ = "Copyright di mago merlino, non può essere infranto"
__credits__ = ["Alkhasar", "IlMistico"]
__version__ = "1.0.0"
__status__ = "Prototype"

def main(loginUrl, pingHost, username, password):
    """ Program main loop, quits on user interaction

    Args:
        loginUrl (string): url to connection provider
        pingHost (string): ip to a ping host (usually google)
        username (string): username used to login
        password (string): password used to login
    """

    ############
    # Graphics #
    ############

    # Initializes pygame
    pygame.init()

    # Objects List
    objects = []

    # Initilizing screen
    screen = pygame.display.set_mode((250, 250))
    pygame.display.set_caption("Autoconnect")

    # Pause auto connector
    def pauseAutoConnector():
        connection.paused = not connection.paused

    def closeProgram():
        pygame.quit()
        sys.exit()

    objects.append(Button(screen, 75, 75, 100, 50, "START", "STOP", pauseAutoConnector))
    objects.append(Button(screen, 75, 145, 100, 50, "EXIT", "", closeProgram))

    # Creating counters
    connectionCounter = CounterText(screen, "Riconnesioni Totali: ", screen.get_width()/2, 20)
    objects.append(connectionCounter)

    # Creating packet text
    packetText = Text(screen, "Pacchetti inviati: 0", screen.get_width()/2, 40)
    objects.append(packetText)

    ###############
    # Application #
    ###############

    # Creates a new connection on a separate thread
    connection = Connection(loginUrl, pingHost, username, password, 5, connectionCounter.increment)
    
    # Application Loop
    while True:
        screen.fill((0, 255, 153))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Placebo text (to make user happy seeing something moving :[ )
        packetText.changeText("Pacchetti inviati: {}".format(connection.sentPackets))

        # Updating every graphic element
        for o in objects:
            o.update()

        pygame.display.flip()
        pygame.time.Clock().tick(10)


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