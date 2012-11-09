# Created by Christiaan Meijer 2012
import numpy
import unittest

class Cube(object):
    def __init__(self):
        self.state = numpy.array([numpy.zeros([3,3]) + i for i in range(0,6)], int) # top, front, right, back, left, bottom
        self.actions = ['+top', '-top', '+front', '-front', '+right', '-right', '+back', '-back', '+left', '-left', '+bottom', '-bottom']
        self.colorTranslations = ['r', 'b', 'w', 'g', 'y', 'o']

    def getActions(self):
        return list(self.actions)

    def performAction(self, action):
        if action == '+top':
            self.turnTopClockwise()
            return
        if action == '-top':
            self.turnTopAntiClockwise()
            return
        if action == '+front':
            self.rotateState('forward')
            self.turnTopClockwise()
            self.rotateState('backward')
            return
        if action == '-front':
            self.rotateState('forward')
            self.turnTopAntiClockwise()
            self.rotateState('backward')
            return
        if action == '+left':
            self.rotateState('rollright')
            self.turnTopClockwise()
            self.rotateState('rollleft')
            return
        if action == '-left':
            self.rotateState('rollright')
            self.turnTopAntiClockwise()
            self.rotateState('rollleft')
            return
        if action == '+right':
            self.rotateState('rollleft')
            self.turnTopClockwise()
            self.rotateState('rollright')
            return
        if action == '-right':
            self.rotateState('rollleft')
            self.turnTopAntiClockwise()
            self.rotateState('rollright')
            return
        if action == '+back':
            self.rotateState('backward')
            self.turnTopClockwise()
            self.rotateState('forward')
            return
        if action == '-back':
            self.rotateState('backward')
            self.turnTopAntiClockwise()
            self.rotateState('forward')
            return
        if action == '+bottom':
            self.rotateState('backward')
            self.rotateState('backward')
            self.turnTopClockwise()
            self.rotateState('backward')
            self.rotateState('backward')
            return
        if action == '-bottom':
            self.rotateState('backward')
            self.rotateState('backward')
            self.turnTopAntiClockwise()
            self.rotateState('backward')
            self.rotateState('backward')
            return
        raise Exception("Unrecognized action '{0}'".format(action))

    def turnTopClockwise(self):
        top = turnSurfaceClockwise(self.state[0])
        middle = shiftRow(0, self.state[1:5], 1)
        bottom = self.state[5]
        self.state = numpy.array([top, middle[0], middle[1], middle[2], middle[3], bottom], int)

    def turnTopAntiClockwise(self):
        self.turnTopClockwise()
        self.turnTopClockwise()
        self.turnTopClockwise()        

    def isSolved(self):
        for surface in self.state:
            color = surface[1][1]
            for row in surface:
                for cell in row:
                    if cell != color:
                        return False
        return True

    def getCopy(self):
        copy = Cube()
        copy.state = numpy.array(self.state, int)
        return copy

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        rep = ''
        space = '       '
        for i in range(0,3):
            rep += space + self.stateRowToString(self.state[0][i]) + '\n'
        rep += '\n'
        for i in range(0,3):
            s = ''
            for j in range(1,5):
                s += self.stateRowToString(self.state[j][i]) + ' '
            rep += s + '\n'
        rep += '\n'
        for i in range(0,3):
            rep+= space + self.stateRowToString(self.state[5][i]) + '\n'
        return rep

    def stateRowToString(self, stateRow):
        s = ''
        for i in range(0,3):
            s += self.colorTranslations[stateRow[i]] + ' '
        return s

    def rotateState(self, direction):
        if direction == 'forward':      # over the left-right axis
            oldState0 = self.state[0].copy()
            self.state[0] = self.state[2]
            self.state[2] = self.state[5]
            self.state[5] = turnSurfaceClockwise(turnSurfaceClockwise(self.state[4]))
            self.state[4] = turnSurfaceClockwise(turnSurfaceClockwise(oldState0))
            self.state[1] = turnSurfaceAntiClockwise(self.state[1])
            self.state[3] = turnSurfaceClockwise(self.state[3])
            return
        if direction == 'backward':     # over the left-right axis
            self.rotateState('forward')
            self.rotateState('forward')
            self.rotateState('forward')
            return
        if direction == 'left':         # over the top-bottom axis
            oldState1 = self.state[1].copy()
            self.state[0] = turnSurfaceClockwise(self.state[0])
            self.state[1] = self.state[2]
            self.state[2] = self.state[3]
            self.state[3] = self.state[4]
            self.state[4] = oldState1
            self.state[5] = turnSurfaceAntiClockwise(self.state[5])
            return
        if direction == 'right':        # over the top-bottom axis
            self.rotateState('left')
            self.rotateState('left')
            self.rotateState('left')
            return
        if direction == 'rollleft':     # over the front-back axis
            self.rotateState('backward')
            self.rotateState('left')
            self.rotateState('forward')
            return
        if direction == 'rollright':    # over the front-back axis
            self.rotateState('backward')
            self.rotateState('right')
            self.rotateState('forward')
            return
        raise Exception("Unrecognized direction '{0}'".format(direction))

    def getStandardizedBinaryState(self):
        symmetries = map(lambda x : x.getBinaryState(), self.getSymmetries())
        symmetryDictionary = {}
        for symmetry in symmetries:
            symmetryDictionary[`symmetry`] = symmetry
        symmetryRepresentations = list(symmetries)
        symmetryRepresentations.sort()
        return symmetryRepresentations[-1]

    def getBinaryState(self):
        featureVector = []
        for color in range(0,6):
            for side in range(0,6):
                sideList = [item for sublist in self.state[side] for item in sublist]
                featureVector.extend(map(lambda x : x == color and 1.0 or 0.0, sideList))
        return featureVector

    def getSymmetries(self): #TODO make it return a bunch of symmetries instead of just the identity
        return [self]

def turnSurfaceClockwise(surface):    
    return numpy.array([reverse(surface[:,0]), reverse(surface[:,1]), reverse(surface[:,2])])

def reverse(sequence):
    l = list(sequence)
    l.reverse()
    return l

def turnSurfaceAntiClockwise(surface):    
    return turnSurfaceClockwise(turnSurfaceClockwise(turnSurfaceClockwise(surface)))

def shiftRow(rowNumber, surfaces, bias): # shift row to the left by bias
    newSurfaces = []
    for s in range(0,4):
        newSurface = []
        for r in range(0,3):
            newRow = []
            for c in range(0,3):
                if r == rowNumber:
                    newRow.append(surfaces[(s+bias)%4][r,c])
                else:
                    newRow.append(surfaces[s][r,c])
            newSurface.append(newRow)
        newSurfaces.append(newSurface)
    return newSurfaces

#*******************************************************************************

class CubeTest(unittest.TestCase):
    def setUp(self):
        self.c = Cube()

    def test_longSequence(self):
        # Arrange
        import random
        random.seed(0) #Seed should always be 0
        actions = 10 * self.c.getActions()
        random.shuffle(actions)
        expected = numpy.array([[[2, 4, 5],  [3, 0, 3],  [0, 5, 5]],
                     [[1, 0, 3],  [5, 1, 1],  [5, 4, 2]],
                     [[4, 1, 1],  [0, 2, 4],  [0, 1, 4]],
                     [[4, 2, 2],  [1, 3, 0],  [0, 5, 5]],
                     [[1, 0, 0],  [2, 4, 4],  [3, 5, 3]],
                     [[3, 2, 1],  [3, 5, 3],  [2, 2, 4]]])

        # Act
        for action in actions:
            self.c.performAction(action)

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_newCubeIsNotSolvedAfter1Move(self):
        # Arrange
        action = self.c.getActions()[1]

        # Act
        self.c.performAction(action)

        # Assert
        self.assertFalse(self.c.isSolved())

    def test_newCubeIsSolved(self):
        # Assert
        self.assertTrue(self.c.isSolved())

if __name__ == '__main__':
    unittest.main()
