# Created by Christiaan Meijer 2012
from valueFunction import NNValueFunction
from world import CubeWorld
import random
random.seed(0)

class Learner(object):
    def __init__(self):
        self.stateValueFunction = None
        self.world = CubeWorld()
        self.explorationMethod = None # Options: 'greedy', 'epsilonGreedy', 'random'
        self.epsilon = None # Portion of random actions while using epsilonGreedy exploration method
        self.gamma = None # Discounting factor
        self.learn = None # Update the value function?

    def setValue(self, inputs, value):
        if self.stateValueFunction == None:
            self.stateValueFunction = NNValueFunction(len(inputs))
        self.stateValueFunction.set(inputs, value)

    def getValue(self, inputs):
        if self.stateValueFunction == None:
            self.stateValueFunction = NNValueFunction(len(inputs))
        return self.stateValueFunction.get(inputs)

    def iteration(self):
        action = self.determineAction()
        reward = self.world.performActionAndReceiveReward(action)
        bestValueAction = self.getBestValueAction()
        if bestValueAction[1] == None or self.world.hasEnded():
            nextValue = 0.0
        else:
            nextValue = bestValueAction[0]
        
        if self.learn:
            value = reward + self.gamma * nextValue
            if value > 1.0:
                print 'Value = {0} = {1} + {2} * {3}'.format(value, reward, self.gamma, nextValue)
                print self.world.hasEnded()
                print self.world.cube.isSolved()
                print self.world.cube
                raise Exception('Value exceeded expected maximum.')
            
            self.setValue(self.world.getState(), value)

    def determineAction(self):
        method = self.explorationMethod
        if method == None:
            method = 'greedy'
        if method == 'epsilonGreedy' and random.random() < self.epsilon:
            action = self.getRandomAction()
        if method == 'random':
            action = self.getRandomAction()
        if method == 'greedy' or 'epsilonGreedy':
            action = self.getGreedyAction()
        if action == None:
            raise Exception('Action could not be determined')
        return action
        
    def getGreedyAction(self):
        return self.getBestValueAction()[1]

    def getBestValueAction(self):
        valueActions = self.getPossibleValueActions()
        bestValueAction = (None, None)
        for valueAction in valueActions:
            if bestValueAction[0] == None or valueAction[0] > bestValueAction[0]:
                bestValueAction = valueAction
        return bestValueAction

    def getRandomAction(self):
        possibleActions = self.world.getPossibleActions()
        random.shuffle(possibleActions)
        return possibleActions[0]

    def getPossibleValueActions(self):
        possibleActions = self.world.getPossibleActions()
        valueActions = []
        for possibleAction in possibleActions:
            possibleState = self.world.getState(possibleAction)
            value = self.getValue(possibleState)
            valueActions.append((value, possibleAction))
        return valueActions

    # Act according to the learned policy without exploring or learning anything.
    def solveGreedily(self, limit):
        self.loadGreedyConfiguration()
        return self.solve(limit)

    def train(self, limit):
        self.loadTrainConfiguration()
        return self.solve(limit)

    def solve(self, limit):
        for i in range(0, limit):
            if self.world.hasEnded():
                return i
            self.iteration()
        if self.world.hasEnded():
            return limit
        return None

    def loadGreedyConfiguration(self):
        self.explorationMethod = 'greedy'
        self.learn = False

    def loadTrainConfiguration(self):
        self.explorationMethod = 'epsilonGreedy'
        self.epsilon = 0.2
        self.gamma = 0.9
        self.learn = True

if __name__ == '__main__':
    pass
