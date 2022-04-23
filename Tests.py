import unittest

from tools.Parsers import CSVParser
from tools.Preprocessing import FixedTimeHorizon, FixedTimeHorizonMinimized, SimpleMovingAverage
from tools.Visualization import ScatterPlot, ComparePlot

TEST_DATA_AMD = "data/test/AMD.csv"
TEST_DATA_INTC = "data/test/INTC.csv"

class TestParsers(unittest.TestCase):
    def test_CSVParser(self):
        test = CSVParser(TEST_DATA_AMD)

        self.assertEqual(test.getColumnTitles(), ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
        self.assertEqual(type(test.getColumn("Close")), type([]))
        self.assertEqual(type(test.getColumn("Close")[0]), type(""))
        self.assertEqual(type(test.getColumnAsFloats("Close")[0]), type(0.0))

class TestPreprocessing(unittest.TestCase):
    def test_FixedTimeHorizon(self):
        data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
        test = FixedTimeHorizon(data)
        look_ahead = 5
        labeled = test.label(look_ahead, 1.10, 0.90)
        
        # Might not always be true but works for now
        self.assertEqual(len(labeled), len(data) - look_ahead)
        self.assertTrue(1 in labeled)
        self.assertTrue(0 in labeled)
        self.assertTrue(-1 in labeled)

    def test_FixedTimeHorizonMinimized(self):
        data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
        test = FixedTimeHorizonMinimized(data)
        look_ahead = 5
        labeled = test.label(look_ahead, 1.10, 0.90)
        
        # Might not always be true but works for now
        self.assertEqual(len(labeled), len(data) - look_ahead)
        self.assertTrue(1 in labeled)
        self.assertTrue(0 in labeled)
        self.assertTrue(-1 in labeled)
    
    def test_SimpleMovingAverage(self):
        data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
        test = SimpleMovingAverage(data)
        labeled = test.label()[0]

        self.assertTrue(1 in labeled)
        self.assertTrue(-1 in labeled)

class TestVisualization(unittest.TestCase):
    def test_ScatterPlot(self):
        data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
        look_ahead = 20
        labels = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)
        test = ScatterPlot(data[0:len(data) - look_ahead], labels, show = False)
    
    def test_ComparePlot(self):
        data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
        look_ahead = 20
        labels1 = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)

        sma = SimpleMovingAverage(data).label()
        labels2 = sma[0]
        data2 = sma[1]

        test = ComparePlot(data[0:len(data) - look_ahead], data2, labels1, labels2, show = True)

if __name__ == "__main__":
    unittest.main()