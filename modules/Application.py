import tkinter as tk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Sidgets dict
        self.widgets = {}

        # Main window geometry
        self.geometry("100x100")
        
        # Generating graphics
        self.widgets["labelA"] = tk.Label(text="Reconnections: 0")
        self.widgets["labelB"] = tk.Label(text="Sent Packets: 0")
        self.widgets["buttonA"] = tk.Button(height = 1, width = 10, text ="START", command = lambda: print("START"))
        self.widgets["buttonB"] = tk.Button(height = 1, width = 10, text ="EXIT", command = lambda: print("EXIT"))
        
        # Positioning Graphic
        self.widgets["labelA"].place(x=15, y=0)
        self.widgets["labelB"].place(x=15, y=20)
        self.widgets["buttonA"].place(x=15, y=40)
        self.widgets["buttonB"].place(x=15, y=65)

        # Adding counter
        self.labelAcounter = 0
        self.labelBcounter = 0

        # On reconnct callback
        def onReconnect(event):
            self.labelAcounter += 1
            self.widgets["labelA"].configure(text="Reconnections: {}".format(self.labelAcounter))

        # On reconnct callback
        def onPacketSent(event):
            self.labelBcounter += 1
            self.widgets["labelB"].configure(text="Sent Packets: {}".format(self.labelBcounter))

        # Events
        self.bind("<<reconnection>>", onReconnect)
        self.bind("<<packetSent>>", onPacketSent)