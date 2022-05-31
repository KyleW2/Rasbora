import random
import time
from .states.MCQState import *
from .Step import *

class MonteCarloQ:
    def __init__(self, enviroment: object, alpha: float, steps_to_explore: float, epsilon: float) -> None:
        self.env = enviroment
        
        self.alpha = alpha
        self.steps_to_explore = steps_to_explore
        self.epsilon = epsilon

        # Keys: tuple = (norm)
        # Value: State = State()
        self.policy = {}

        # Class var for induvidual episodes
        # Reset each time
        self.episode = []

    def eGreey(self, state: tuple):
        # Chance to be greedy
        if random.random() < (1 - self.epsilon):
            # Return max action
            return self.policy[state].getMaxAction()
        # Explore with random action
        else:
            return random.choice([-1, 0, 1])
    
    def randomAction(self) -> int:
        return random.choice([-1, 0, 1])
    
    def updateV(self):
        # Nest for loops uh-oh!
        # RIP any sort of speed
        alreadyVisited = []
        for i in range(0, len(self.episode)):
            stateTuple = self.episode[i].getState()
            action = self.episode[i].getAction()

            # If first occurence of s
            if (stateTuple, action) not in alreadyVisited:
                # Sum rewards
                r = 0
                for j in range(i, len(self.episode)):
                    r += self.episode[j].getReward()

                # Append r to s's returns
                self.policy[stateTuple].updateReturns(action, r)
                self.policy[stateTuple].updateValue(action, self.alpha)

                # Added to list of visited states
                alreadyVisited.append((stateTuple, action))
    
    def runEpisode(self) -> float:
        # Reset the stuff
        self.episode = []
        observation = self.env.reset()
        done = False
        step = 0

        # Loop for each step
        while not done:
            # Create tuple representing current state
            stateTuple = observation

            # Add state to policy if new
            if stateTuple not in self.policy.keys():
                self.policy[stateTuple] = MCQState(stateTuple)
            
            # Find next action using e-greedy
            action = self.eGreey(stateTuple)

            if step <= self.steps_to_explore:
                action = self.randomAction()

            # Observe r and s'
            observation, reward, done, made, spent = self.env.step(action)

            # Add step to episode
            self.episode.append(Step(stateTuple, action, reward))

            step += 1

        self.updateV()
        return (made, spent)

    def runSeries(self, episodes: int) -> None:
        for i in range(0, episodes):
            start_time = time.time()
            profit = self.runEpisode()
            print(f"episode: {i}, profit: {'{:.2f}'.format(profit[0] - profit[1])}, made: {'{:.2f}'.format(profit[0])}, spent: {'{:.2f}'.format(profit[1])}, time: {'{:.2f}'.format(time.time() - start_time, 2)}")

            if self.epsilon > .1:
                self.epsilon *= .9999
    
    def close(self):
        self.env.close()