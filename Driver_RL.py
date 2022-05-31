from tools.Parsers import *
from tools.Preprocessing import *
from models.reinforcement.enviroments.Taiga import *
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

# Make enviroment
env = Taiga(norm, close, 0.99)

# Make agent
agent = MonteCarloQ(env, 0.05, 0, 1.0)

agent.runSeries(10000)