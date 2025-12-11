from abc import ABC, abstractmethod

class Browser_Manager(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stop command, common")

class ChromeBrowser(Browser_Manager):

    def start(self):
        print("We are staring the chrome")

tc = ChromeBrowser()
tc.start()
tc.stop()