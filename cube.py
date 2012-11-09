# Created by Christiaan Meijer 2012
import numpy
import unittest
import sys
import time
import copy

class Cube(object):
    def __init__(self):
        self.state = [[[k for i in range(0,3)] for j in range(0,3)] for k in range(0,6)]
        self.actions = ['+top', '-top', '+front', '-front', '+right', '-right', '+back', '-back', '+left', '-left', '+bottom', '-bottom']
        self.colorTranslations = ['r', 'b', 'w', 'g', 'y', 'o']
        self.directions = ['forward', 'backward', 'left', 'right', 'rollleft', 'rollright']

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
            transformation = [[[[0, 0, 0], [0, 0, 1], [0, 0, 2]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[1, 2, 2], [1, 1, 2], [1, 0, 2]]], [[[1, 0, 0], [1, 0, 1], [5, 0, 0]], [[1, 1, 0], [1, 1, 1], [5, 0, 1]], [[1, 2, 0], [1, 2, 1], [5, 0, 2]]], [[[2, 2, 0], [2, 1, 0], [2, 0, 0]], [[2, 2, 1], [2, 1, 1], [2, 0, 1]], [[2, 2, 2], [2, 1, 2], [2, 0, 2]]], [[[0, 2, 0], [3, 0, 1], [3, 0, 2]], [[0, 2, 1], [3, 1, 1], [3, 1, 2]], [[0, 2, 2], [3, 2, 1], [3, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [4, 0, 2]], [[4, 1, 0], [4, 1, 1], [4, 1, 2]], [[4, 2, 0], [4, 2, 1], [4, 2, 2]]], [[[3, 2, 0], [3, 1, 0], [3, 0, 0]], [[5, 1, 0], [5, 1, 1], [5, 1, 2]], [[5, 2, 0], [5, 2, 1], [5, 2, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '-front':
            transformation = [[[[0, 0, 0], [0, 0, 1], [0, 0, 2]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[3, 0, 0], [3, 1, 0], [3, 2, 0]]], [[[1, 0, 0], [1, 0, 1], [0, 2, 2]], [[1, 1, 0], [1, 1, 1], [0, 2, 1]], [[1, 2, 0], [1, 2, 1], [0, 2, 0]]], [[[2, 0, 2], [2, 1, 2], [2, 2, 2]], [[2, 0, 1], [2, 1, 1], [2, 2, 1]], [[2, 0, 0], [2, 1, 0], [2, 2, 0]]], [[[5, 0, 2], [3, 0, 1], [3, 0, 2]], [[5, 0, 1], [3, 1, 1], [3, 1, 2]], [[5, 0, 0], [3, 2, 1], [3, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [4, 0, 2]], [[4, 1, 0], [4, 1, 1], [4, 1, 2]], [[4, 2, 0], [4, 2, 1], [4, 2, 2]]], [[[1, 0, 2], [1, 1, 2], [1, 2, 2]], [[5, 1, 0], [5, 1, 1], [5, 1, 2]], [[5, 2, 0], [5, 2, 1], [5, 2, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '+left':
            transformation = [[[[4, 2, 2], [0, 0, 1], [0, 0, 2]], [[4, 1, 2], [0, 1, 1], [0, 1, 2]], [[4, 0, 2], [0, 2, 1], [0, 2, 2]]], [[[1, 2, 0], [1, 1, 0], [1, 0, 0]], [[1, 2, 1], [1, 1, 1], [1, 0, 1]], [[1, 2, 2], [1, 1, 2], [1, 0, 2]]], [[[0, 0, 0], [2, 0, 1], [2, 0, 2]], [[0, 1, 0], [2, 1, 1], [2, 1, 2]], [[0, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [3, 0, 2]], [[3, 1, 0], [3, 1, 1], [3, 1, 2]], [[3, 2, 0], [3, 2, 1], [3, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [5, 2, 0]], [[4, 1, 0], [4, 1, 1], [5, 1, 0]], [[4, 2, 0], [4, 2, 1], [5, 0, 0]]], [[[2, 0, 0], [5, 0, 1], [5, 0, 2]], [[2, 1, 0], [5, 1, 1], [5, 1, 2]], [[2, 2, 0], [5, 2, 1], [5, 2, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '-left':
            transformation = [[[[2, 0, 0], [0, 0, 1], [0, 0, 2]], [[2, 1, 0], [0, 1, 1], [0, 1, 2]], [[2, 2, 0], [0, 2, 1], [0, 2, 2]]], [[[1, 0, 2], [1, 1, 2], [1, 2, 2]], [[1, 0, 1], [1, 1, 1], [1, 2, 1]], [[1, 0, 0], [1, 1, 0], [1, 2, 0]]], [[[5, 0, 0], [2, 0, 1], [2, 0, 2]], [[5, 1, 0], [2, 1, 1], [2, 1, 2]], [[5, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [3, 0, 2]], [[3, 1, 0], [3, 1, 1], [3, 1, 2]], [[3, 2, 0], [3, 2, 1], [3, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [0, 2, 0]], [[4, 1, 0], [4, 1, 1], [0, 1, 0]], [[4, 2, 0], [4, 2, 1], [0, 0, 0]]], [[[4, 2, 2], [5, 0, 1], [5, 0, 2]], [[4, 1, 2], [5, 1, 1], [5, 1, 2]], [[4, 0, 2], [5, 2, 1], [5, 2, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '+right':
            transformation = [[[[0, 0, 0], [0, 0, 1], [2, 0, 2]], [[0, 1, 0], [0, 1, 1], [2, 1, 2]], [[0, 2, 0], [0, 2, 1], [2, 2, 2]]], [[[1, 0, 0], [1, 0, 1], [1, 0, 2]], [[1, 1, 0], [1, 1, 1], [1, 1, 2]], [[1, 2, 0], [1, 2, 1], [1, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [5, 0, 2]], [[2, 1, 0], [2, 1, 1], [5, 1, 2]], [[2, 2, 0], [2, 2, 1], [5, 2, 2]]], [[[3, 2, 0], [3, 1, 0], [3, 0, 0]], [[3, 2, 1], [3, 1, 1], [3, 0, 1]], [[3, 2, 2], [3, 1, 2], [3, 0, 2]]], [[[0, 2, 2], [4, 0, 1], [4, 0, 2]], [[0, 1, 2], [4, 1, 1], [4, 1, 2]], [[0, 0, 2], [4, 2, 1], [4, 2, 2]]], [[[5, 0, 0], [5, 0, 1], [4, 2, 0]], [[5, 1, 0], [5, 1, 1], [4, 1, 0]], [[5, 2, 0], [5, 2, 1], [4, 0, 0]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '-right':
            transformation = [[[[0, 0, 0], [0, 0, 1], [4, 2, 0]], [[0, 1, 0], [0, 1, 1], [4, 1, 0]], [[0, 2, 0], [0, 2, 1], [4, 0, 0]]], [[[1, 0, 0], [1, 0, 1], [1, 0, 2]], [[1, 1, 0], [1, 1, 1], [1, 1, 2]], [[1, 2, 0], [1, 2, 1], [1, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [0, 0, 2]], [[2, 1, 0], [2, 1, 1], [0, 1, 2]], [[2, 2, 0], [2, 2, 1], [0, 2, 2]]], [[[3, 0, 2], [3, 1, 2], [3, 2, 2]], [[3, 0, 1], [3, 1, 1], [3, 2, 1]], [[3, 0, 0], [3, 1, 0], [3, 2, 0]]], [[[5, 2, 2], [4, 0, 1], [4, 0, 2]], [[5, 1, 2], [4, 1, 1], [4, 1, 2]], [[5, 0, 2], [4, 2, 1], [4, 2, 2]]], [[[5, 0, 0], [5, 0, 1], [2, 0, 2]], [[5, 1, 0], [5, 1, 1], [2, 1, 2]], [[5, 2, 0], [5, 2, 1], [2, 2, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '+back':
            transformation = [[[[3, 0, 2], [3, 1, 2], [3, 2, 2]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[0, 2, 0], [0, 2, 1], [0, 2, 2]]], [[[0, 0, 2], [1, 0, 1], [1, 0, 2]], [[0, 0, 1], [1, 1, 1], [1, 1, 2]], [[0, 0, 0], [1, 2, 1], [1, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [2, 0, 2]], [[2, 1, 0], [2, 1, 1], [2, 1, 2]], [[2, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [5, 2, 2]], [[3, 1, 0], [3, 1, 1], [5, 2, 1]], [[3, 2, 0], [3, 2, 1], [5, 2, 0]]], [[[4, 2, 0], [4, 1, 0], [4, 0, 0]], [[4, 2, 1], [4, 1, 1], [4, 0, 1]], [[4, 2, 2], [4, 1, 2], [4, 0, 2]]], [[[5, 0, 0], [5, 0, 1], [5, 0, 2]], [[5, 1, 0], [5, 1, 1], [5, 1, 2]], [[1, 0, 0], [1, 1, 0], [1, 2, 0]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '-back':
            transformation = [[[[1, 2, 0], [1, 1, 0], [1, 0, 0]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[0, 2, 0], [0, 2, 1], [0, 2, 2]]], [[[5, 2, 0], [1, 0, 1], [1, 0, 2]], [[5, 2, 1], [1, 1, 1], [1, 1, 2]], [[5, 2, 2], [1, 2, 1], [1, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [2, 0, 2]], [[2, 1, 0], [2, 1, 1], [2, 1, 2]], [[2, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [0, 0, 0]], [[3, 1, 0], [3, 1, 1], [0, 0, 1]], [[3, 2, 0], [3, 2, 1], [0, 0, 2]]], [[[4, 0, 2], [4, 1, 2], [4, 2, 2]], [[4, 0, 1], [4, 1, 1], [4, 2, 1]], [[4, 0, 0], [4, 1, 0], [4, 2, 0]]], [[[5, 0, 0], [5, 0, 1], [5, 0, 2]], [[5, 1, 0], [5, 1, 1], [5, 1, 2]], [[3, 2, 2], [3, 1, 2], [3, 0, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '+bottom':
            transformation = [[[[0, 0, 0], [0, 0, 1], [0, 0, 2]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[0, 2, 0], [0, 2, 1], [0, 2, 2]]], [[[1, 0, 0], [1, 0, 1], [1, 0, 2]], [[1, 1, 0], [1, 1, 1], [1, 1, 2]], [[4, 2, 0], [4, 2, 1], [4, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [2, 0, 2]], [[2, 1, 0], [2, 1, 1], [2, 1, 2]], [[1, 2, 0], [1, 2, 1], [1, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [3, 0, 2]], [[3, 1, 0], [3, 1, 1], [3, 1, 2]], [[2, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [4, 0, 2]], [[4, 1, 0], [4, 1, 1], [4, 1, 2]], [[3, 2, 0], [3, 2, 1], [3, 2, 2]]], [[[5, 2, 0], [5, 1, 0], [5, 0, 0]], [[5, 2, 1], [5, 1, 1], [5, 0, 1]], [[5, 2, 2], [5, 1, 2], [5, 0, 2]]]]
            transformCubeState(self.state, transformation)
            return
        if action == '-bottom':
            transformation = [[[[0, 0, 0], [0, 0, 1], [0, 0, 2]], [[0, 1, 0], [0, 1, 1], [0, 1, 2]], [[0, 2, 0], [0, 2, 1], [0, 2, 2]]], [[[1, 0, 0], [1, 0, 1], [1, 0, 2]], [[1, 1, 0], [1, 1, 1], [1, 1, 2]], [[2, 2, 0], [2, 2, 1], [2, 2, 2]]], [[[2, 0, 0], [2, 0, 1], [2, 0, 2]], [[2, 1, 0], [2, 1, 1], [2, 1, 2]], [[3, 2, 0], [3, 2, 1], [3, 2, 2]]], [[[3, 0, 0], [3, 0, 1], [3, 0, 2]], [[3, 1, 0], [3, 1, 1], [3, 1, 2]], [[4, 2, 0], [4, 2, 1], [4, 2, 2]]], [[[4, 0, 0], [4, 0, 1], [4, 0, 2]], [[4, 1, 0], [4, 1, 1], [4, 1, 2]], [[1, 2, 0], [1, 2, 1], [1, 2, 2]]], [[[5, 0, 2], [5, 1, 2], [5, 2, 2]], [[5, 0, 1], [5, 1, 1], [5, 2, 1]], [[5, 0, 0], [5, 1, 0], [5, 2, 0]]]]
            transformCubeState(self.state, transformation)
            return
        raise Exception("Unrecognized action '{0}'".format(action))

    def turnTopClockwise(self):
        top = turnSurfaceClockwise(self.state[0])
        middle = shiftRow(0, self.state[1:5], 1)
        bottom = self.state[5]
        self.state = [top, middle[0], middle[1], middle[2], middle[3], bottom]

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
        cubeCopy = Cube()
        cubeCopy.state = copy.deepcopy(self.state)
        return cubeCopy

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
            if True:#stateRow[i] >= len(self.colorTranslations):
                s += '{:3.0f}'.format(stateRow[i]) + ' '
            else:
                s += self.colorTranslations[stateRow[i]] + ' '
        return s

    def rotateState(self, direction):
        if direction == 'forward':      # over the left-right axis
            oldState0 = copy.deepcopy(self.state[0])
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
            oldState1 = copy.deepcopy(self.state[1])
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
        symmetries = list(map(lambda x : x.getBinaryState(), self.getSymmetries()))

        # Early escape for special case to win performance.
        if len(symmetries) == 1:
            return symmetries[0]

        symmetryDictionary = {}
        for symmetry in symmetries:
            symmetryDictionary[`symmetry`] = symmetry
        symmetryRepresentations = list(symmetries)
        symmetryRepresentations.sort()
        return symmetryRepresentations[-1]

    def getBinaryState(self):
        featureVector = []
        for i in range(0,6):
            color = self.state[i][1][1] # The color of the middle face of the ith side.
            for side in range(0,6):
                sideList = [item for sublist in self.state[side] for item in sublist]
                featureVector.extend(map(lambda x : x == color and 1.0 or 0.0, sideList))
        return featureVector

    # A failed attempt to speed up the calculation of the binary state.
    def getBinaryState2(self):
        s = self.state
        return flatten([flatten([map(lambda x:x==c and 1.0 or 0.0, flatten(s[j])) for j in range(0,6)]) for c in range(0,6)])

    # A failed attempt to speed up the calculation of the binary state.
    def getBinaryState3(self):
        featureVector = []
        for i in range(0,6):
            color = self.state[i][1][1] # The color of the middle face of the ith side.
            for side in range(0,6):
                for row in range(0,3):
                    for cell in range(0,3):
                        if self.state[side][row][cell] == color:
                            value = 1.0
                        else:
                            value = 0.0
                        featureVector.append(value)
        return featureVector
    

    def getSymmetries(self): #TODO make it return a bunch of symmetries instead of just the identity
        return [self]

def flatten(enumeration):
    return [item for sublist in enumeration for item in sublist]

def transformCubeState(state, transformation):
    temp = copy.deepcopy(state)
    for surface in range(0, len(state)):
        for row in range(0, len(state[surface])):
            for cel in range(0, len(state[surface][row])):
                x = transformation[surface][row][cel]
                state[surface][row][cel] = temp[x[0]][x[1]][x[2]]
    return state

def turnSurfaceClockwise(surface):    
    return [reverse([surface[i][j] for i in range(0,3)]) for j in range(0,3)]

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
                    newRow.append(surfaces[(s+bias)%4][r][c])
                else:
                    newRow.append(surfaces[s][r][c])
            newSurface.append(newRow)
        newSurfaces.append(newSurface)
    return newSurfaces

#*******************************************************************************

class CubeStateTransitionsTest(unittest.TestCase):
    def setUp(self):
        self.c = Cube()
        self.c.state = [[[100*k+10*j+i for i in range(0,3)] for j in range(0,3)] for k in range(0,6)]

    def test_longSequence_correctState(self):
        # Arrange
        # Some long sequence of actions
        actions = ['+top', '-front', '-left', '+bottom', '-left', '+front', '-top', '-back', '-bottom', '-back', '-top', '+left', '+right', '+top', '+bottom', '+right', '+bottom', '-left', '-back', '+back', '-right', '-front', '-right', '+back', '-bottom', '-right', '-front', '-top', '+left', '-bottom', '+top', '+right', '+left', '+front', '+front', '+back']
        expected = numpy.array([[[0, 510, 322], [12, 11, 1], [202, 421, 500]], [[100, 301, 300], [21, 111, 221], [502, 112, 400]], [[22, 521, 220], [501, 211, 512], [302, 110, 20]], [[122, 401, 522], [321, 311, 312], [200, 10, 422]], [[420, 121, 402], [410, 411, 201], [120, 212, 320]], [[2, 412, 102], [210, 511, 101], [222, 310, 520]]])

        # Act
        for action in actions:
            self.c.performAction(action)

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_left_correctState(self):
        # Arrange        
        expected = numpy.array([[[20, 10, 0], [21, 11, 1], [22, 12, 2]], [[200, 201, 202], [210, 211, 212], [220, 221, 222]], [[300, 301, 302], [310, 311, 312], [320, 321, 322]], [[400, 401, 402], [410, 411, 412], [420, 421, 422]], [[100, 101, 102], [110, 111, 112], [120, 121, 122]], [[502, 512, 522], [501, 511, 521], [500, 510, 520]]])

        # Act
        self.c.rotateState('left')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_right_correctState(self):
        # Arrange        
        expected = numpy.array([[[2, 12, 22], [1, 11, 21], [0, 10, 20]], [[400, 401, 402], [410, 411, 412], [420, 421, 422]], [[100, 101, 102], [110, 111, 112], [120, 121, 122]], [[200, 201, 202], [210, 211, 212], [220, 221, 222]], [[300, 301, 302], [310, 311, 312], [320, 321, 322]], [[520, 510, 500], [521, 511, 501], [522, 512, 502]]])

        # Act
        self.c.rotateState('right')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_forward_correctState(self):
        # Arrange        
        expected = numpy.array([[[200, 201, 202], [210, 211, 212], [220, 221, 222]], [[102, 112, 122], [101, 111, 121], [100, 110, 120]], [[500, 501, 502], [510, 511, 512], [520, 521, 522]], [[320, 310, 300], [321, 311, 301], [322, 312, 302]], [[22, 21, 20], [12, 11, 10], [2, 1, 0]], [[422, 421, 420], [412, 411, 410], [402, 401, 400]]])

        # Act
        self.c.rotateState('forward')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_backward_correctState(self):
        # Arrange        
        expected = numpy.array([[[422, 421, 420], [412, 411, 410], [402, 401, 400]], [[120, 110, 100], [121, 111, 101], [122, 112, 102]], [[0, 1, 2], [10, 11, 12], [20, 21, 22]], [[302, 312, 322], [301, 311, 321], [300, 310, 320]], [[522, 521, 520], [512, 511, 510], [502, 501, 500]], [[200, 201, 202], [210, 211, 212], [220, 221, 222]]])

        # Act
        self.c.rotateState('backward')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_rollleft_correctState(self):
        # Arrange        
        expected = numpy.array([[[302, 312, 322], [301, 311, 321], [300, 310, 320]], [[2, 12, 22], [1, 11, 21], [0, 10, 20]], [[202, 212, 222], [201, 211, 221], [200, 210, 220]], [[502, 512, 522], [501, 511, 521], [500, 510, 520]], [[420, 410, 400], [421, 411, 401], [422, 412, 402]], [[102, 112, 122], [101, 111, 121], [100, 110, 120]]])

        # Act
        self.c.rotateState('rollleft')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

    def test_rotateState_rollright_correctState(self):
        # Arrange        
        expected = numpy.array([[[120, 110, 100], [121, 111, 101], [122, 112, 102]], [[520, 510, 500], [521, 511, 501], [522, 512, 502]], [[220, 210, 200], [221, 211, 201], [222, 212, 202]], [[20, 10, 0], [21, 11, 1], [22, 12, 2]], [[402, 412, 422], [401, 411, 421], [400, 410, 420]], [[320, 310, 300], [321, 311, 301], [322, 312, 302]]])

        # Act
        self.c.rotateState('rollright')

        # Assert
        difference = numpy.array(self.c.state) - expected
        self.assertTrue(numpy.linalg.norm(difference) == 0)

class CubeSanityTest(unittest.TestCase):
    def test_newCubeIsNotSolvedAfter1Move(self):
        # Arrange
        newCube = Cube()
        action = newCube.getActions()[1]

        # Act
        newCube.performAction(action)

        # Assert
        self.assertFalse(newCube.isSolved())

    def test_newCubeIsSolved(self):
        # Arrange
        newCube = Cube()

        # Assert
        self.assertTrue(newCube.isSolved())

class BinaryStateTester(unittest.TestCase):
    def test_getBinaryState_solvedCube_correctState(self):
        # Arrange
        cube = Cube()
        expectedState = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        # Act
        binaryState = cube.getBinaryState()

        # Assert
        self.assertEqual(binaryState, expectedState)

    def test_getBinaryState_solvedCube_correctState(self):
        # Arrange
        cube = Cube()
        # Some sequence of actions
        actions = ['+top', '-front', '-left', '+bottom', '-left', '+front']
        for action in actions:
            cube.performAction(action)
        expectedState = [0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0]

        # Act
        binaryState = cube.getBinaryState()

        # Assert
        self.assertEqual(binaryState, expectedState)

class SpeedTester(object):
    def __init__(self):
        self.cube = Cube()
        self.surface = self.cube.state[0]
        self.accuracy = 1.0

    def speedTest(self):        
        """self.componentSpeedTest(lambda : turnSurfaceClockwise(self.surface), 'turnSurfaceClockwise')
        self.componentSpeedTest(lambda : turnSurfaceAntiClockwise(self.surface), 'turnSurfaceAntiClockwise')
        for action in self.cube.actions:
            self.componentSpeedTest(lambda : self.cube.performAction(action), 'action_' + action)
        for direction in self.cube.directions:
            self.componentSpeedTest(lambda : self.cube.rotateState(direction), 'rotateState_' + direction)"""
        self.componentSpeedTest(lambda : self.cube.getStandardizedBinaryState(), 'getStandardizedBinaryState')
        self.componentSpeedTest(lambda : self.cube.getBinaryState(), 'getBinaryState')
        self.componentSpeedTest(lambda : self.cube.getBinaryState2(), 'getBinaryState2')
        self.componentSpeedTest(lambda : self.cube.getBinaryState3(), 'getBinaryState3')



    def componentSpeedTest(self, component, name):
        start = time.time()
        end = start
        taken = 0
        count = 0
        while(taken < self.accuracy):
            for i in range(0,5):
                component()
                count += 1
            end = time.time()
            taken = end - start
        mean = taken/count
        print '{:30} could run {:5.0f} times, on average {:1.6f} seconds'.format(name, count, mean)
        return mean

def main():
    cube = Cube()
    transformation = [[['' for i in range(0,3)] for j in range(0,3)] for k in range(0,6)]    
    for surface in range(0, len(cube.state)):
        for row in range(0, len(cube.state[surface])):
            for cel in range(0, len(cube.state[surface][row])):
                transformation[surface][row][cel] = [surface,row,cel]
    cube.state = transformation
    action = cube.actions[7]
    cube.performAction(action)
    transformation = cube.state
    print action
    print cube.state
    cube2 = Cube()
    cube2.state = [[[100*k+10*j+i for i in range(0,3)] for j in range(0,3)] for k in range(0,6)]
    cube2.rotateState('left')
    print cube2.state


if __name__ == '__main__':
    if 'speedtest' in sys.argv:
        st = SpeedTester()
        st.speedTest()
    else:
        if 'main' in sys.argv:
            main()
        else:
            unittest.main()
