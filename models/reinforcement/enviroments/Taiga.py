"""
Taiga doesn't limit the agent to starting funds

Reward scheme:
    buying  -> -1
    holding -> 0
    selling -> 1 if made a profit
            -> -1 if made a loss
"""

class Taiga:
    def __init__(self, states: list, values: list, commision: float) -> None:
        self.states = states
        self.values = values

        # Amount spent
        self.spent = 0
        # Amount made (not profit)
        self.made = 0
        # Number of shares being held
        self.holding = 0

        self.commision = commision

        self.current_index = 0
    
    # Returns tuple (observation, reward, done)
    def step(self, action: int) -> tuple:
        self.current_index += 1

        # Observation
        observation = self.states[self.current_index]

        # Rewards
        if action == -1:
            self.made += (1 - self.commision) * (self.holding * self.values[self.current_index])
            self.holding = 0

            if self.made > self.spent:
                reward = 1
            else:
                reward = -1

        if action == 0:
            reward = 0
        
        if action == 1:
            self.holding += 1
            self.spent += self.values[self.current_index]
            reward = -1

        # Done
        done = False
        if self.current_index + 1 == len(self.states):
            done = True
        
        return observation, reward, done, self.made, self.spent

    # Returns Initial observation
    def reset(self) -> float:
        self.spent = 0
        self.made = 0
        self.holding = 0

        self.current_index = 0

        return self.states[self.current_index]
    
    # Dummy method?
    def close(self) -> None:
        pass