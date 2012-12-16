# Created by David Adler on Wed, 30 May 2012 (MIT)

import math
import random
import string
import time
import unittest

class NN:
  def __init__(self, NI, NH, NO, randomSeed = None):
    if randomSeed != None:
        random.seed(randomSeed)

    self.verbose = False

    # number of nodes in layers
    self.ni = NI + 1 # +1 for bias
    self.nh = NH
    self.no = NO
    
    # initialize node-activations
    self.ai, self.ah, self.ao = [],[], []
    self.ai = [1.0]*self.ni
    self.ah = [1.0]*self.nh
    self.ao = [1.0]*self.no

    # create node weight matrices
    self.wi = makeMatrix (self.ni, self.nh) # weights from input to hidden
    self.wo = makeMatrix (self.nh, self.no) # weights from hidden to output
    # initialize node weights to random vals
    randomizeMatrix ( self.wi, -0.2, 0.2 )
    randomizeMatrix ( self.wo, -2.0, 2.0 )
    # create last change in weights matrices for momentum
    self.ci = makeMatrix (self.ni, self.nh)
    self.co = makeMatrix (self.nh, self.no)
    
  def runNN (self, inputs):
    if len(inputs) != self.ni-1:
      print 'incorrect number of inputs'
    
    for i in range(self.ni-1):
      self.ai[i] = inputs[i]
      
    for j in range(self.nh):
      sum = 0.0
      for i in range(self.ni):
        sum +=( self.ai[i] * self.wi[i][j] )
      self.ah[j] = sigmoid (sum)
    
    for k in range(self.no):
      sum = 0.0
      for j in range(self.nh):        
        sum +=( self.ah[j] * self.wo[j][k] )
      self.ao[k] = sigmoid(sum) # This sigmoid has to go.
      
    return self.ao
  
  def backPropagate (self, targets, N, M):
    # http://www.youtube.com/watch?v=aVId8KMsdUU&feature=BFa&list=LLldMCkmXl4j9_v0HeKdNcRA    
    output_deltas = self.getOutputDeltas(targets)   
    self.updateOutputWeights(output_deltas, N, M)
    hidden_deltas = self.getHiddenDeltas(output_deltas)    
    self.updateInputWeights(hidden_deltas, N, M)    

  def getOutputDeltas(self, targets):
    # calc output deltas
    # we want to find the instantaneous rate of change of ( error with respect to weight from node j to node k)
    # output_delta is defined as an attribute of each ouput node. It is not the final rate we need.
    # To get the final rate we must multiply the delta by the activation of the hidden layer node in question.
    # This multiplication is done according to the chain rule as we are taking the derivative of the activation 
    # function of the ouput node.
    # dE/dw[j][k] = (t[k] - ao[k]) * s'( SUM( w[j][k]*ah[j] ) ) * ah[j]
    output_deltas = [0.0] * self.no
    for k in range(self.no):
      error = targets[k] - self.ao[k] 
      output_deltas[k] =  error * dsigmoid(self.ao[k]) # this dsigmoid can probably go        
    return output_deltas
  
  def updateOutputWeights(self, output_deltas, N, M):
    for j in range(self.nh):
      for k in range(self.no):
        # output_deltas[k] * self.ah[j] is the full derivative of dError/dweight[j][k]
        change = output_deltas[k] * self.ah[j]
        self.wo[j][k] += N*change + M*self.co[j][k]
        self.co[j][k] = change

  def getHiddenDeltas(self, output_deltas):
    hidden_deltas = [0.0] * self.nh
    for j in range(self.nh):
      error = 0.0
      for k in range(self.no):
        error += output_deltas[k] * self.wo[j][k]
      hidden_deltas[j] = error * dsigmoid(self.ah[j])
    return hidden_deltas

  def updateInputWeights(self, hidden_deltas, N, M):
    for i in range (self.ni):
      for j in range (self.nh):
        change = hidden_deltas[j] * self.ai[i]
        self.wi[i][j] += N*change + M*self.ci[i][j]
        self.ci[i][j] = change
 
  def weights(self):
    print 'Input weights:'
    for i in range(self.ni):
      print self.wi[i]
    print
    print 'Output weights:'
    for j in range(self.nh):
      print self.wo[j]
    print ''
  
  def test(self, patterns):
    for p in patterns:
      inputs = p[0]
      #print 'Inputs:-->', self.runNN(inputs), '\tTarget', p[1]
  
  def train (self, patterns, max_iterations = 1000, N=0.5, M=0.1):
    for i in range(max_iterations):
      for p in patterns:
        inputs = p[0]
        targets = p[1]
        self.runNN(inputs)
        self.backPropagate(targets, N, M)
      #if i % 50 == 0 and self.verbose:
        #print 'Combined error', error
    if self.verbose:    
        self.test(patterns)
    

def sigmoid (x):  
  return math.tanh(x)

# the derivative of the sigmoid function in terms of output
def dsigmoid (y):
  tanhy = math.tanh(y)
  return 1 - (tanhy * tanhy)

def makeMatrix ( I, J, fill=0.0):
  m = []
  for i in range(I):
    m.append([fill]*J)
  return m
  
def randomizeMatrix ( matrix, a, b):
  for i in range ( len (matrix) ):
    for j in range ( len (matrix[0]) ):
      matrix[i][j] = random.uniform(a,b)

#*************************************************************************
class NNTests(unittest.TestCase):
  def test_simpleNetwork_correctOutput(self):
    # Arrange
    instance = [1.0]
    hiddenInputs = 1.0 + 1.0 # instance input + hidden threshold
    hiddenOutput = math.tanh(hiddenInputs)
    outputInput = hiddenOutput
    outputOutput = math.tanh(hiddenOutput)
    target = [outputOutput]

    # Act
    output = self.nn.runNN(instance)

    # Assert
    self.assertEqual(output, target)

  def test_simpleNetwork_correctOutputDeltas(self):
    # Arrange
    instance = [1.0]
    target = [0.0]
    pat = [instance, target]
    learningRate = 1.0
    inertia = 0.0

    Oj = 1.0
    dk = -1.0 * dsigmoid(1.0)
    expected = [dk * Oj]

    # Act    
    deltas = self.nn.getOutputDeltas(target)
    print deltas

    # Assert
    self.assertEqual(deltas, expected)

  def setUp(self):
    self.nn = NN(1,1,1)
    self.nn.wi = makeMatrix (self.nn.ni, self.nn.nh, fill = 1.0)
    self.nn.wo = makeMatrix (self.nn.nh, self.nn.no, fill = 1.0)


def main ():
  pat = [
      [[0,0], [1]],
      [[0,1], [0.9]],
      [[1,0], [0.3]],
      [[1,1], [0]]
  ]
  myNN = NN ( 2, 6, 1)
  myNN.train(pat)

  n = 9*6*6
  pat = [[n*[0], [0.9]]]
  myNN = NN ( n, 6, 1)
  myNN.verbose = True
  myNN.train(pat)

def speedTest():
    lowerBound = -5
    upperBound = 5
    size = 1000000
    test = [lowerBound + i/(upperBound - lowerBound) for i in range(size)]
    functions = [sigmoid, dsigmoid]
    
    for function in functions:
        print function.__name__
        start = time.time()
        for i in test:
            function(i)
        end = time.time()
        elapsed = end - start
        print elapsed

if __name__ == "__main__":
  unittest.main()