# Importing std libraries
import time, os

# Importing thread
from threading import Thread

# Importing selenium stuff
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Importing ping
from pythonping import ping

class Connection(Thread, Chrome):
    def __init__(self, loginUrl, pingHost, username, password, deltaT=5, onReconnect=None):
        """Initializes a connection to the provider and keeps the connection active

        Args:
            loginUrl (string): url to the login page
            pingHost (string): ip to the ping server to check if online
            username (string): username used to login
            password (string): password used to login
            deltaT (int, optional): _description_. Defaults to 5.
            onReconnect (int, optional): _description_. Defaults to None.
        """
        super().__init__()

        # Lets make it sneaky :)
        options = Options()
        options.headless = True
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        super(Thread, self).__init__(executable_path=("webdriver/chromedriver.exe" if os.name == "nt"  else "webdriver/chromedriver"), options=options)

        # This thread is obviosly not stopped
        self.paused = True

        # Reconections
        self.onReconnect = onReconnect
        self.sentPackets = 0

        # Connection data
        self.pingHost = pingHost
        self.loginUrl = loginUrl
        self.username = username
        self.password = password
        self.deltaT = deltaT

        # Thread starting itself as daemon 
        self.setDaemon(True)
        
        # Starting thread
        self.start()  

    def checkConnection(self, pingHost):
        """Checks if pc is online by sending a single packet to pinghost
        and expecting a packet in response

        Args:
            pingHost (tring): ip to the ping host

        Returns:
            bool: returns True if connection needs to be reenstablished
        """
        # Pinging google is fun!!
        _ = ping(pingHost, match=True, count=1)
        self.sentPackets += 1
        return not _.success()

    def login(self, url, username, password):
        """Executes login routine (ノಠ益ಠ)ノ彡┻━┻

        Args:
            url (string): url to login page
            username (string): username used to login
            password (string): password used to login
        """
        # Navigating to login page
        self.get(url)

        # Selecting elements
        _username = self.find_element(By.NAME, "username")
        _password = self.find_element(By.NAME, "password")
        submitBtn = self.find_element(By.ID, "submit-btn")

        # Login
        _username.send_keys(username)
        _password.send_keys(password)
        submitBtn.click()        

    def run(self):
        """Function automatically called by thread, contains auto-login logic
        """
        while True:
            # Sleep for 2 second 
            time.sleep(self.deltaT)

            # If this thread is not paused check for connection
            if not self.paused:
                if(self.checkConnection(self.pingHost)):
                    self.login(self.loginUrl, self.username, self.password)
                    self.onReconnect()
