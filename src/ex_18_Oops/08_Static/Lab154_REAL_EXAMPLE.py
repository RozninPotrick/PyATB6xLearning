class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel.")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL.")

class TC1:

    def run(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:
    def run(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

tc1 = TC1()
tc1.run()

tc2 = TC1()
tc2.run()

