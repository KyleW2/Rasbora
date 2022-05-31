import random

"""
-1 = sell
0 = hold
1 = buy
"""

class MCQState:
    def __init__(self, state: tuple) -> None:
        self.state = state

        self.returns = {-1: [], 0: [], 1: []}
        self.sumOfReturns = {-1: 0, 0: 0, 1: 0}

        self.actionValues = {-1: 0, 0: 0, 1: 0}
    
    def __str__(self) -> str:
        return str(self.state)
    
    def getMaxAction(self) -> int:
        max = -100000000
        action = -1

        for k, v in self.actionValues.items():
            if v > max:
                max = v
                action = k
        
        return action
    
    def updateReturns(self, action: int, reward: float) -> None:
        self.returns[action].append(reward)
        self.sumOfReturns[action] += reward
    
    def getActionValue(self, action: int) -> float:
        return self.actionValues[action]
    
    def updateValue(self, action: int, alpha: float) -> None:
        g = self.sumOfReturns[action] / len(self.returns[action])
        self.actionValues[action] += alpha * (g - self.actionValues[action])