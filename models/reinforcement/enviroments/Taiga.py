from .Portfolio import *

"""
Taiga doesn't limit the agent to starting funds

Reward scheme:
    buying  -> -1
    holding -> 0
    selling -> 1 if made a profit
            -> -1 if made a loss
"""

class Taiga:
    def __init__(self, states: list, values: list, commision: float, default_buy_amount: int = 10) -> None:
        self.states = states
        self.values = values

        self.spent = 0
        self.made = 0
        self.portfolio = Portfolio()

        self.default_buy_amount = default_buy_amount
        self.commision = commision

        self.current_index = 0
    
    # Returns tuple (observation, reward, done)
    def step(self, action: int) -> tuple:
        self.current_index += 1

        # Observation
        observation = self.states[self.current_index]

        # Action
        if action == 1:
            self.spent += self.values[self.current_index] * self.default_buy_amount
            self.portfolio.buy(self.values[self.current_index], self.default_buy_amount)
        if action == -1:
            self.made += self.portfolio.value()
            self.portfolio.dump()

        # Rewards
        points = self.portfolio.points(self.values[self.current_index])
        if points >= 0.5:
            reward = 1
        elif points < -0.5:
            reward = -1
        else:
            reward = 0

        # Done
        done = False
        if self.current_index + 1 == len(self.states):
            done = True
        
        return observation, reward, done, self.made, self.spent

    # Returns Initial observation
    def reset(self) -> float:
        self.spent = 0
        self.made = 0
        self.portfolio = Portfolio()

        self.current_index = 0

        return self.states[self.current_index]
    
    # Dummy method?
    def close(self) -> None:
        pass