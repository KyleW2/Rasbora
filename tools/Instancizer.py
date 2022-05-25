import numpy as np

def Instancizer(points: list, labels: list) -> list:
    # I tried numpy...
    """
    # Create array with shape [[[p1, p2, ...], label], [[p1, p2, ...], label], ...]
    instances = np.zeros(shape = [len(labels), 2])

    for i in range(0, len(labels)):
        # Create array with shape [[p1, p2, ...], label]
        instance = np.zeros(shape = (1, 2))
        np.append(instance, np.zeros(shape = [1, 2]))

        # Append points to sub array
        for j in range(0, len(points)):
            np.append(instance[0], points[j][i])
        
        # Append label to array
        np.append(instance, labels[i])
        
        # Append instance to instances
        np.append(instances, instance)
    """

    # Create array with shape [[[p1, p2, ...], label], [[p1, p2, ...], label], ...]
    instances = []

    for i in range(0, len(labels)):
        # Create array with shape [[p1, p2, ...], label]
        instance = []
        instance.append([])

        # Append points to sub array
        for j in range(0, len(points)):
            instance[0].append(points[j][i])
        
        # Append label to array
        instance.append(labels[i])
        
        # Append instance to instances
        instances.append(np.array([np.array(instance[0]), instance[1]], dtype = object))

    return np.array(instances)