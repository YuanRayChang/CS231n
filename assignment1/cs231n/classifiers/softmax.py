import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  num_train = X.shape[0]
  num_class = W.shape[1]
  for i in range(num_train):
        score = X[i].dot(W)
        score -= np.max(score)
        correct_class_score = score[y[i]]
        Prob = np.exp(correct_class_score)/np.sum(np.exp(score))
        loss += -np.log(Prob)
        for j in range(num_class):
            if j==y[i]:
                dW[:, y[i]] += -X[i]*(1-Prob)
            else:
                dW[:, j] += X[i]*np.exp(score[j])/np.sum(np.exp(score))
  loss /= num_train
  loss += reg*np.sum(W*W)
  dW /= num_train
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  num_train = X.shape[0]
  num_class = W.shape[1]
  
  score = np.matmul(X, W)
  # https://stackoverflow.com/questions/26333005/numpy-subtract-every-row-of-matrix-by-vector
  score = score.T
  score -= np.amax(score, axis=0)  
  score = score.T
  #
  
  correct_class_score = score[np.arange(num_train), y]
  Prob_c = np.exp(correct_class_score)/np.sum(np.exp(score), axis=1)
  loss = np.sum(-np.log(Prob_c))
    
  # for dW  
  Prob = np.exp(score).T/np.sum(np.exp(score), axis=1)
  Prob = Prob.T

  #binary = np.zeros(Prob.shape)
  #binary[np.arange(num_train), y] = 1
  #Prob -= binary
  binary = Prob
  binary[np.arange(num_train), y] -= 1

  dW = np.matmul(X.T, binary)    
         
  loss /= num_train
  loss += reg*np.sum(W*W)
  dW /= num_train
  dW += 2*reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

