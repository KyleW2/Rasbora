import random

"""
-1 = sell
0 = hold
1 = buy
"""

class MCQRState:
    def __init__(self, state: tuple, r: int) -> None:
        self.state = state

        self.returns = {}
        self.sumOfReturns = {}

        self.actionValues = {}

        for i in range(-1 * r, r + 1):
            self.returns[i] = []
            self.sumOfReturns[i] = 0
            self.actionValues[i] = 0
    
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