import matplotlib.pyplot as plt
import time

class ScatterPlot():
    def __init__(self, data: list, labels: list, show: bool = True, save: bool = True) -> None:
        colors = []
        for i in range(0, len(labels)):
            if labels[i] == 1:
                colors.append("b")
            elif labels[i] == 0:
                colors.append("#808080")
            else:
                colors.append("r")

        plt.scatter([y for y in range(0, len(data))], data, c = colors)

        if show:
            plt.show()
        
        if save:
            plt.savefig(f"plot_{time.time()}.jpg", dpi = 300)

class ComparePlot():
    def __init__(self, data1: list, data2: list, labels: list, show: bool = True, save: bool = False) -> None:
        colors1 = []
        for i in range(0, len(labels)):
            if labels[i] == 1:
                colors1.append((0, 0, 1, 1))
            elif labels[i] == 0:
                colors1.append((0.5, 0.5, 0.5, 0.1))
            else:
                colors1.append((1, 0, 0, 1))

        plt.scatter([y for y in range(0, len(data1))], data1, c = colors1)
        plt.plot([y for y in range(0, len(data2))], data2)

        if show:
            plt.show()
        
        if save:
            plt.savefig(f"plot_{time.time()}.jpg", dpi = 300)