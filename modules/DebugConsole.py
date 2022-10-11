import tkinter as tk
from threading import Lock
from datetime import datetime as date


class SingletonMeta(type):
    """Standard ThreadSafe singleton metaclass implementation
    """

    # Creating an instance dict and a thread lock
    _instances = {}
    _lock: Lock = Lock()

    # Function called to construct a class
    def __call__(cls, *args, **kwargs):
        # First thread goes over every other accessing thread waits
        with cls._lock:
            # If an instance does not exist, add it to instances
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        
        # Either return the created instance
        return cls._instances[cls]


class DebugConsole(metaclass=SingletonMeta):
    """Singleton class that represents the logging console.
    Only one logging console is alowed per program.
    """
    def __init__(self, textNode):
        self.textNode = textNode
        self.logText = ""
        self.path = "logs"

    def log(self, text):
        # Retrieving number of lines
        numlines = int(self.textNode.index("end - 1 line").split('.')[0])
        logMsg = "" + str(date.now()) + ": "+ text + '\n'

        # Setting widget mode to editable
        self.textNode["state"] = "normal"

        # Deleting previous lnes
        if numlines==5:
            self.textNode.delete(1.0, 2.0)

        # Adding a line and moving pointer to end
        self.textNode.insert(tk.END, logMsg)
        self.textNode.see(tk.END)

        # Setting widget mode to not editable
        self.textNode["state"] = "normal"

        # Adding msg to the string that is going to be saved on file
        self.logText += logMsg

    def saveLog(self):
        fileName = self.path + "/LogFile[" + str(date.now().date()) + "].txt"
        with open(fileName, "a") as f:
            for line in self.logText:
                f.write(line)

        
        