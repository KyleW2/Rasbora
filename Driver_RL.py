from tools.Parsers import *
from tools.Preprocessing import *
from models.reinforcement.enviroments.Taiga import *
from models.reinforcement.enviroments.Redwoods import *
from models.reinforcement.MonteCarloQ import *

# Constants
STOCK_FILE = "data/dev/testing/INTC_for_index.csv"
INDEX_FILE = "data/dev/testing/IXIC.csv"

# Load data
parser = CSVParser(STOCK_FILE)
close = parser.getColumnAsFloats("Close")

ind_parser = CSVParser(INDEX_FILE)
ind_close = ind_parser.getColumnAsFloats("Close")

# Make data
norm = Normalize(close, ind_close, 3)

class StockPoint:
    def __init__(self, norm: float, price: float) -> None:
        self.norm = norm
        self.price = price

data = [StockPoint(norm[i], close[i]) for i in range(0, len(norm))]

# Make enviroment
env = Redwoods(data, 0.0)

# Make agent
agent = MonteCarloQ(env, 0.05, 1.0)

try:
    agent.runSeries_Redwoods(100000)
except KeyboardInterrupt:
    #print(agent.close())
    pass