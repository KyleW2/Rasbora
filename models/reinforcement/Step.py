class Step:
    def __init__(self, state: tuple, action: int, reward: int) -> None:
        self.state = state
        self.action = action
        self.reward = reward
    
    def __str__(self) -> str:
        return "[" + str(self.state) + ", " + str(self.action) + ", " + str(self.reward) + "]"
    
    def getState(self) -> tuple:
        return self.state
    def getAction(self) -> int:
        return self.action
    def getReward(self) -> int:
        return self.reward