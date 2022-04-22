import unittest

from tools.Parsers import CSVParser
from tools.Preprocessing import FixedTimeHorizon

class TestParsers(unittest.TestCase):
    def test_CSVParser(self):
        test = CSVParser("AMD.csv")

        self.assertEquals(test.getColumnTitles("Date,Open,High,Low,Close,Adj Close,Volume"))
        self.assertEquals(type(test.getColumn("Close")), type([]))
        self.assertEquals(type(test.getColumn("Close")[0]), type(""))
        self.assertEquals(type(test.getColumnAsFloats("Close")[0]), type(0.0))

class TestPreprocessing(unittest.TestCase):
    def test_fixed_time_horizion(self):
        pass

if __name__ == "__main__":
    unittest.main()