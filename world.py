# Created by Christiaan Meijer 2012
from cube import Cube

class World(object):
    def getPossibleActions(self):
        raise Exception('not implemented')

    def performActionAndReceiveReward(self, action):
        raise Exception('not implemented')

    def getState(self, action = None):
        raise Exception('not implemented')

class CubeWorld(World):
    def __init__(self):
        self.cube = Cube()

    def getPossibleActions(self):
        return self.cube.getActions()

    def performActionAndReceiveReward(self, action):
        self.cube.performAction(action)
        if self.cube.isSolved():
            return 1.0
        else:
            return 0.0

    def hasEnded(self):
        #print self.cube
        return self.cube.isSolved()

    def getState(self, action = None):
        if action == None:
            return self.cube.getStandardizedBinaryState()
        else:
            copy = self.cube.getCopy()
            copy.performAction(action)
            return copy.getStandardizedBinaryState()
