# Created by Christiaan Meijer 2012
from valueFunction import NNValueFunction
from world import CubeWorld
import unittest
import random
from learner import Learner
import time
import cPickle
random.seed(0)

class Validator(object):
    def __init__(self):
        self.validationSetSize = 100
        self.maxActionsPerTrial = 100
        self.validationSetPath = 'data/validationSet.pck'
    
    def getSuccessRate(self, results):
        if len(results) == 0:
            return 0.0
        noneCount = 0.0
        for result in results:
            if result == None:  
                noneCount += 1
        return 1.0 - (noneCount / len(results))

    def validate(self, learner):
        fail = 0
        success = 0
        validationSet = self.getValidationSet()
        print 'Starting validation.'
        count = 0
        for instance in validationSet:
            learner.world = instance
            result = learner.solveGreedily(self.maxActionsPerTrial)
            if result == None:
                fail += 1
            else:
                success += 1

            ratio = 1.0 * success / (fail + success)

            count += 1
            if count%1 == 0:
                print 'Success rate is {} after {} instances.'.format(ratio, count)
        print ratio

    def getValidationSet(self):
        try:        
            validationSet = self.loadValidationSet()[0:self.validationSetSize]
        except:
            print 'Failed to load validation set.'
            validationSet = self.generateValidationSet()
        return validationSet

    def generateValidationSet(self):
        print 'Generating validation set.'
        validationSet = []
        for i in range(0, self.validationSetSize):
            validationSet.append(self.generateRandomWorld())
            if i%100 == 0:
                print 'Generated {} instances.'.format(i)
        self.saveValidationSet(validationSet)        
        return validationSet

    def generateRandomWorld(self):
        world = CubeWorld(random = True)        
        return world

    def saveValidationSet(self, validationSet):
        print 'Saving validation set.'
        f = open(self.validationSetPath, 'w')
        cPickle.dump(validationSet, f)

    def loadValidationSet(self):
        print 'Loading validation set.'
        f = open(self.validationSetPath, 'r')            
        validationSet = cPickle.load(f)
        f.close()
        return validationSet
#*******************************************************************************

class Test(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    # unittest.main()
    validator = Validator()
    validator.validate(Learner())
    

