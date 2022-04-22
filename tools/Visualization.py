import matplotlib.pyplot as plt

class ScatterPlotter():
    def __init__(self, data: list, labels: list, show: bool = True) -> None:
        colors = []
        for i in range(0, len(labels)):
            if labels[i] == 1:
                colors.append("g")
            elif labels[i] == 0:
                colors.append("b")
            else:
                colors.append("r")

        plt.scatter([y for y in range(0, len(data))], data, c = colors)

        if show:
            plt.show()