# Created by Christiaan Meijer 2012
from cube import Cube

class Rewarder(object):
    def reset(self):
        raise Exception('not implemented')

    def peekReward(self, cube):
        raise Exception('not implemented')

    def getReward(self, cube):
        raise Exception('not implemented')

class ValueDifferentialRewarder(Rewarder):
    def __init__(self):
        self.lastValue = None;
        self.edgeWeight = 1.0 / 12
        self.cornerWeight = 1.0 / 8

    def reset(self, cube):
        self.lastValue = self.getValue(cube)

    def peekReward(self, cube):
        value = self.getValue(cube)
        return value - self.lastValue

    def getReward(self, cube):
        if self.lastValue == None:
            return None

        value = self.getValue(cube)
        improvement = value - self.lastValue
        lastValue = value
        return improvement

    def getValue(self, cube):
        correctEdges = cube.getCorrectEdges()
        correctCorners = cube.getCorrectCorners()
        return self.edgeWeight * correctEdges + self.cornerWeight * correctCorners

class AllOrNothingRewarder(Rewarder):
    def __init__(self):
        pass

    def reset(self, cube):
        pass

    def peekReward(self, cube):
        return self.getValue(cube)

    def getReward(self, cube):
        return self.getValue(cube)

    def getValue(self, cube):
        if cube.isSolved():
            return 1.0
        else:
            return 0.0
