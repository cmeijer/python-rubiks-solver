# Created by Christiaan Meijer
from NN import NN
import unittest
import cPickle

class ValueFunction(object):
    def __init__(self, inputNodes, path = None):
        raise Exception('Not implemented')

    def get(self, inputs):
        raise Exception('Not implemented')

    def set(self, inputs, value):
        raise Exception('Not implemented')

    def reset(self):
        raise Exception('Not implemented')

class NNValueFunction(object):
    def __init__(self, inputNodes, path = None):
        self.inputNodes = inputNodes
        self.hiddenNodes = 20
        self.outputNodes = 1
        if path == None:
            self.path = 'data/valueFunction_{}i{}h{}o.pck'.format(self.inputNodes, self.hiddenNodes, self.outputNodes)
        else:
            self.path = path
        try:
            f = open(self.path, 'r')            
            self.nn = cPickle.load(f)
            f.close()
        except:
            self.reset()
        self.nn.verbose = True
        self.N = 0.01
        self.M = 0.01
        self.data = []
        self.maxDataSize = 4 # Number of set() instances that are remembered and trained on.

    def get(self, inputs):
        return self.nn.runNN(inputs)[0]

    def set(self, inputs, value):
        self.data.append([inputs, [value]])
        if len(self.data) > self.maxDataSize:
            self.data = self.data[-self.maxDataSize:]
        self.nn.train(self.data, max_iterations = 4, N=self.N, M=self.M)

    def __del__(self):
        print 'Writing neural net to {}.'.format(self.path)
        f = open(self.path, 'w')
        cPickle.dump(self.nn, f)
        print 'Neural net written.'

    def reset(self):
        self.nn = NN(self.inputNodes, self.hiddenNodes, self.outputNodes)

class HashTableValueFunction(object):
    def __init__(self, inputNodes, path = 'valueFunction.pck'):
        self.reset()

    def get(self, inputs):
        representation = `inputs`
        if representation in self.table:
            return self.table[representation]
        return 0.0

    def set(self, inputs, value):
        representation = `inputs`
        self.table[representation] = value

    def reset(self):
        self.table = {}

#*************************************************************************
class VFTest(unittest.TestCase):
    def setUp(self):
        from cube import Cube
        self.c = Cube()
        self.b = self.c.getBinaryState()
        self.c.performAction(self.c.getActions()[0])
        self.d = self.c.getBinaryState()
        self.c.performAction(self.c.getActions()[0])
        self.e = self.c.getBinaryState()
        self.nnvf = NNValueFunction(len(self.b))

    def test(self):
        for i in range(0,1000):
            print `self.nnvf.get(self.b)` + ' : ' + `self.nnvf.get(self.d)` + ' : ' + `self.nnvf.get(self.e)`
            self.nnvf.set(self.b, 0.9)
            self.nnvf.set(self.d, 0.7)
            self.nnvf.set(self.e, 0.2)

if __name__ == '__main__':
    unittest.main()
