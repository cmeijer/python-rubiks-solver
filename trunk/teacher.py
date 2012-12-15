# Created by Christiaan Meijer 2012
from valueFunction import NNValueFunction
from world import CubeWorld
import unittest
import random
from learner import Learner
import time
random.seed(0)

class Teacher(object):
    def __init__(self):
        self.sampleSize = 100
        self.minimumSuccessRate = 0.85
        self.maximumSuccessRate = 0.95
        self.reportRateEveryTries = 250

    def teach(self, learner):
        maxDifficulty = 20
        difficulty = 0
        while(difficulty < maxDifficulty):
            isCurrentDifficultyTooEasy = False
            isCurrentDifficultyTooHard = False
            stepLimit = difficulty + 2
            startTime = time.time()
            tries = 0
            results = []
            while(isCurrentDifficultyTooEasy == False and isCurrentDifficultyTooHard == False):
                learner.world = self.getWorld(difficulty)
                results.append(learner.train(stepLimit))
                tries += 1  
                if len(results) >= self.sampleSize:
                    successRate = self.getSuccessRate(results[-self.sampleSize:])
                    isCurrentDifficultyTooEasy = successRate >= self.maximumSuccessRate
                    isCurrentDifficultyTooHard = successRate < self.minimumSuccessRate
                    timeTaken = time.time() - startTime
                    averageTimePerTry = timeTaken / tries
                    if tries%self.reportRateEveryTries == 0:
                        print 'After {:4.0f} tries at dif {:2.0f}, success rate = {:1.2f} and {:2.3f} s/try.'.format(tries, difficulty, successRate, averageTimePerTry)
                    if isCurrentDifficultyTooEasy:
                        print 'Dif {:2.0f} proved too easy (ratio {:1.2f}) after {:4.0f} tries at {:2.3f} s/try. Changed dif to {:2.0f}.'.format(difficulty, successRate, tries, averageTimePerTry, difficulty + 1)
                        difficulty += 1
                    if isCurrentDifficultyTooHard:
                        print 'Dif {:2.0f} proved too hard (ratio {:1.2f}) after {:4.0f} tries at {:2.3f} s/try. Changed dif to {:2.0f}.'.format(difficulty, successRate, tries, averageTimePerTry, difficulty - 1)
                        difficulty -= 1              

    def getWorld(self, difficulty):
        return CubeWorld(difficulty = difficulty)

    def getSuccessRate(self, results):
        if len(results) == 0:
            return 0.0
        noneCount = 0.0
        for result in results:
            if result == None:  
                noneCount += 1
        return 1.0 - (noneCount / len(results))

#*******************************************************************************

class Test(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher()

    def test_getSuccessRate_returnsCorrectRate(self):
        results = [1,2,3,4, None]
        rate = self.teacher.getSuccessRate(results)
        expectedRate = 0.8
        self.assertEqual(rate, expectedRate)

    def test_getSuccessRate_emptyResultsList_returnsZero(self):
        results = []
        rate = self.teacher.getSuccessRate(results)
        expectedRate = 0.0
        self.assertEqual(rate, expectedRate)

    def test_getSuccessRate_onlySuccesses_emptyResultsList_returnsOne(self):
        results = [1,2,3,4]
        rate = self.teacher.getSuccessRate(results)
        expectedRate = 1.0
        self.assertEqual(rate, expectedRate)

if __name__ == '__main__':
    # unittest.main()
    teacher = Teacher()
    teacher.teach(Learner())
    

