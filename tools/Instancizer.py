import numpy as np

class Instance:
    def __init__(self, points: list, label: int):
        self.points = points
        self.label = label
    
    def __str__(self) -> str:
        return f"Points: {self.points}, Label: {self.label}"

def Instancizer(points: list, labels: list) -> list:
    # Create list with shape [Instance(), Instance(), ...]
    instances = []

    for i in range(0, len(labels)):
        # Append points to temp list
        p = []
        for j in range(0, len(points)):
            p.append(points[j][i])
        
        # Append label to array
        instances.append(Instance(np.array(p), labels[i]))

    return np.array(instances, dtype = object)