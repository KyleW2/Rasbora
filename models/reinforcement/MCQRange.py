import random
import time
from .states.MCQRState import *
from .Step import *

class MonteCarloQ:
    def __init__(self, enviroment: object, alpha: float, epsilon: float, range: int) -> None:
        self.env = enviroment
        
        self.alpha = alpha
        self.epsilon = epsilon

        self.range = range

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
            return self.randomAction()

    def randomAction(self) -> int:
        return random.randint(-1 * self.range, self.range)
    
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

        bhs = []

        # Loop for each step
        while not done:
            # Create tuple representing current state
            stateTuple = observation

            # Add state to policy if new
            if stateTuple not in self.policy.keys():
                self.policy[stateTuple] = MCQRState(stateTuple, self.range)
            
            # Find next action using e-greedy
            action = self.eGreey(stateTuple)
            
            if action > 0:
                bhs.append("b")
            elif action == 0:
                bhs.append("h")
            elif action < 0:
                bhs.append("s")

            # Observe r and s'
            observation, reward, done, value = self.env.step(action)

            # Add step to episode
            self.episode.append(Step(stateTuple, action, reward))

            step += 1

        self.updateV()
        return value, bhs

    def runSeries_Taiga(self, episodes: int) -> None:
        f = open("mcq_results.csv", "w")
        f.write("episide,made,spent,profit,buys,holds,sells,time\n")
        f.close()

        for i in range(0, episodes):
            start_time = time.time()
            profit = self.runEpisode()

            f = open("mcq_results.csv", "a")
            f.write(f"{i},{'{:.2f}'.format(profit[0])},{'{:.2f}'.format(profit[1])},{'{:.4f}'.format(profit[0] - profit[1])},{profit[2]},{profit[3]},{profit[4]},{'{:.2f}'.format(time.time() - start_time, 2)}\n")
            f.close()

            print(f"episode: {i}, epsilon: {self.epsilon}, time: {'{:.2f}'.format(time.time() - start_time, 2)}, profit: {'{:.4f}'.format(profit[0] - profit[1])}, {profit[2]}, {profit[3]}, {profit[4]}")    
            
            if self.epsilon > .1:
                self.epsilon *= .999
    
    def runSeries_Redwoods(self, episodes: int) -> None:
        start_time = time.time()
        value = self.runEpisode()
        first_bhs = value[1]
        value = value[0]

        for i in range(0, episodes - 1):
            start_time = time.time()
            value = self.runEpisode()
            last_bhs = value[1]
            value = value[0]
            print(f"episode: {i}, epsilon: {'{:.3f}'.format(self.epsilon)}, time: {'{:.2f}'.format(time.time() - start_time)}, ending value: {value}")

            self.epsilon *= .999
        
        return first_bhs, last_bhs
    
    def close(self):
        self.env.close()
        return self.policy