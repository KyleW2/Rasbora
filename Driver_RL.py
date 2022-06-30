from tools.Parsers import *
from tools.Preprocessing import *
from models.reinforcement.enviroments.Taiga import *
from models.reinforcement.enviroments.Redwoods import *
from models.reinforcement.MCQRange import *

# Constants

APPLE_FILE = "data/dev/training/five_years/AAPL.csv"
AMAZON_FILE = "data/dev/training/five_years/AMZN.csv"
INTEL_FILE = "data/dev/training/five_years/INTC.csv"
MICROSOFT_FILE = "data/dev/training/five_years/MSFT.csv"
NVIDIA_FILE = "data/dev/training/five_years/NVDA.csv"
TESLA_FILE = "data/dev/training/five_years/TSLA.csv"

INDEX_FILE = "data/dev/training/five_years/IXIC.csv"

# Load data
# Apple
apple = CSVParser(APPLE_FILE).getColumnAsFloats("Close")
amazon = CSVParser(AMAZON_FILE).getColumnAsFloats("Close")
intel = CSVParser(INTEL_FILE).getColumnAsFloats("Close")
microsoft = CSVParser(MICROSOFT_FILE).getColumnAsFloats("Close")
nvidia = CSVParser(NVIDIA_FILE).getColumnAsFloats("Close")
tesla = CSVParser(TESLA_FILE).getColumnAsFloats("Close")

index = CSVParser(INDEX_FILE).getColumnAsFloats("Close")

# Make data
apple_norm = Normalize(apple, index, 3)
amazon_norm = Normalize(amazon, index, 3)
intel_norm = Normalize(intel, index, 3)
microsoft_norm = Normalize(microsoft, index, 3)
nvidia_norm = Normalize(nvidia, index, 3)
tesla_norm = Normalize(tesla, index, 3)

class StockPoint:
    def __init__(self, norm: float, price: float) -> None:
        self.norm = norm
        self.price = price

apple_data = [StockPoint(apple_norm[i], apple[i]) for i in range(0, len(apple_norm))]
amazon_data = [StockPoint(amazon_norm[i], amazon[i]) for i in range(0, len(amazon_norm))]
intel_data = [StockPoint(intel_norm[i], intel[i]) for i in range(0, len(intel_norm))]
microsoft_data = [StockPoint(microsoft_norm[i], microsoft[i]) for i in range(0, len(microsoft_norm))]
nvidia_data = [StockPoint(nvidia_norm[i], nvidia[i]) for i in range(0, len(nvidia_norm))]
tesla_data = [StockPoint(tesla_norm[i], tesla[i]) for i in range(0, len(tesla_norm))]

# Make enviroment
# , amazon_data, intel_data, microsoft_data, nvidia_data, tesla_data
env = Redwoods([apple_data], 0.0, starting_funds = 10000)

# Make agent
agent = MonteCarloQ(env, 0.05, 1.0, 10)

try:
    bhss = agent.runSeries_Redwoods(10000)
    first_bhs = bhss[0]
    last_bhs = bhss[1]

    test = ScatterPlot(apple_data, first_bhs, show = False, save = True)
    test = ScatterPlot(apple_data, last_bhs, show = False, save = True)
except KeyboardInterrupt:
    #print(agent.close())
    pass