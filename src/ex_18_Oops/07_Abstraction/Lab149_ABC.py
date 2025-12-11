from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Staring")

    def stopBrowser(self):
        print("Stopping")

    def readFromExcel(self):
        print("readEfomExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.stopBrowser()
        self.readFromExcel()

tc1 = TC1()
tc1.runTc()

