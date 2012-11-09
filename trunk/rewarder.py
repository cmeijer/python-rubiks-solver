# Created by Christiaan Meijer 2012
from cube import Cube

class Rewarder(object):
    def reset()
        raise Exception('not implemented')

    def peekReward(self, cube)
        raise Exception('not implemented')

    def getReward(self, cube)
        raise Exception('not implemented')

class CubeConsistentRewarder(World):
    def __init__(self):
        self.edgeWeight = 1.0 / 12
        self.cornerWeight = 1.0 / 8

    def reset()
        self.highestCorrectEdges = 0
        self.highestCorrectCorners = 0

    def peekReward(self, cube)
        correctEdges = cube.getCorrectEdges
        correctCorners = cube.getCorrectCorners
        return self.edgeWeight * correctEdges + self.cornerWeight * correctCorners

    def getReward(self, cube)
        return peekReward

