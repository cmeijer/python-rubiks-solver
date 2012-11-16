# Created by Christiaan Meijer 2012
from cube import Cube
from rewarder import ValueDifferentialRewarder
from rewarder import AllOrNothingRewarder
import random as randomGenerator

class World(object):
    def __init__(self, difficulty = None, random = False):
        raise Exception('not implemented')

    def getPossibleActions(self):
        raise Exception('not implemented')

    def performActionAndReceiveReward(self, action):
        raise Exception('not implemented')

    def hasEnded(self):
        raise Exception('not implemented')

    def getState(self, action = None):
        raise Exception('not implemented')

class CubeWorld(World):
    def __init__(self, difficulty = None, random = False):
        if random:
            difficulty = 50
        
        self.cube = Cube()
        self.rewarder = AllOrNothingRewarder()

        if difficulty != None:
            for i in range(0, difficulty):
                possibleActions = self.getPossibleActions()
                randomGenerator.shuffle(possibleActions)
                self.performActionAndReceiveReward(possibleActions[0])

        self.rewarder.reset(self.cube)

    def getPossibleActions(self):
        return self.cube.getActions()

    def performActionAndReceiveReward(self, action):
        self.cube.performAction(action)
        return self.rewarder.getReward(self.cube)

    def hasEnded(self):
        return self.cube.isSolved()

    def getState(self, action = None):
        if action == None:
            return self.cube.getStandardizedBinaryState()
        else:
            copy = self.cube.getCopy()
            copy.performAction(action)
            return copy.getStandardizedBinaryState()
