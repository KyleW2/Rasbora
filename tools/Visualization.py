import matplotlib.pyplot as plt

class ScatterPlot():
    def __init__(self, data: list, labels: list, show: bool = True) -> None:
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

class ComparePlot():
    def __init__(self, data1: list, data2: list, labels1: list, labels2: list, show: bool = True) -> None:
        colors1 = []
        for i in range(0, len(labels1)):
            if labels1[i] == 1:
                colors1.append("b")
            elif labels1[i] == 0:
                colors1.append("#808080")
            else:
                colors1.append("r")
        
        colors2 = []
        for i in range(0, len(labels2)):
            if labels2[i] == 1:
                colors2.append("b")
            elif labels2[i] == 0:
                colors2.append("#808080")
            else:
                colors2.append("r")

        plt.scatter([y for y in range(0, len(data1))], data1, c = colors1)
        plt.plot([y for y in range(0, len(data2))], data2)

        if show:
            plt.show()