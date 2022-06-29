from .Portfolio import *

class Redwoods:
    def __init__(self, states: list, commision: float, default_buy_amount: int = 10, starting_funds: int = 10000) -> None:
        self.states = states

        self.portfolio = Portfolio()

        self.commision = commision
        self.default_buy_amount = default_buy_amount
        self.starting_funds = starting_funds

        self.current_index = 0
        self.old_value = 0
        self.funds = self.starting_funds

    def step(self, action: int) -> None:
        # Do the action
        if action > 0:
            if self.funds >= self.states[self.current_index].price * action:
                self.funds -= self.states[self.current_index].price * action
                self.portfolio.buy(self.states[self.current_index].price, action)
        elif action == 0:
            pass
        elif action < 0:
            possible_to_sell = self.portfolio.sell(self.states[self.current_index].price, -1 * action)

            if possible_to_sell:
                self.funds += self.states[self.current_index].price * (-1 * action)

        # Observation
        self.current_index += 1
        observation = (self.states[self.current_index].norm, self.portfolio.holding(), self.funds)

        # Reward
        reward = self.portfolio.value() - self.old_value
        self.old_value = self.portfolio.value()

        # Done
        done = False
        if self.current_index == len(self.states) - 1:
            done = True
        
        return observation, reward, done, self.portfolio.value()

    def reset(self) -> None:
        self.portfolio = Portfolio()
        self.current_index = 0
        self.old_value = 0
        self.funds = self.starting_funds

        return self.states[self.current_index].norm

    def close(self) -> None:
        pass