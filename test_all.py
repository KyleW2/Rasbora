import pytest

from tools.Parsers import CSVParser
from tools.Preprocessing import FixedTimeHorizon, FixedTimeHorizonMinimized, SimpleMovingAverage, Aggregator

TEST_DATA_AMD = "data/test/AMD.csv"
TEST_DATA_INTC = "data/test/INTC.csv"


def test_CSVParser():
    test = CSVParser(TEST_DATA_AMD)

    assert test.getColumnTitles() == ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    assert type(test.getColumn("Close")) == type([])
    assert type(test.getColumn("Close")[0]) == type("")
    assert type(test.getColumnAsFloats("Close")[0]) == type(0.0)


def test_FixedTimeHorizon():
    data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
    test = FixedTimeHorizon(data)
    look_ahead = 5
    labeled = test.label(look_ahead, 1.10, 0.90)
    
    # Might not always be true but works for now
    assert len(labeled) == len(data) - look_ahead
    assert 1 in labeled
    assert 0 in labeled
    assert -1 in labeled

def test_FixedTimeHorizonMinimized():
    data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
    test = FixedTimeHorizonMinimized(data)
    look_ahead = 5
    labeled = test.label(look_ahead, 1.10, 0.90)
    
    # Might not always be true but works for now
    assert len(labeled) == len(data) - look_ahead
    assert 1 in labeled
    assert 0 in labeled
    assert -1 in labeled

def test_SimpleMovingAverage():
    data = CSVParser(TEST_DATA_AMD).getColumnAsFloats("Close")
    test = SimpleMovingAverage(data)
    labeled = test.label()[0]

    assert 1 in labeled
    assert -1 in labeled

def test_Aggregator():
    with pytest.raises(ValueError):
        test = Aggregator()
        test.combine([1, 2], [[1, 2, 3], [1, 2]])