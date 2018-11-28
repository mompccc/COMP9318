import pandas as pd
import numpy as np

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
    print(data, labels, weights)
    data = np.insert(data, 0, np.ones(data.shape[0]), axis=-1)
    for i in range(num_epochs):
    	h_t = 1/(1+np.exp(-1.0*np.dot(data, weights)))
    	grads = np.array([(labels-h_t) * data[:, j] for j in range(len(weights))]).transpose((1,0))
    	grads = np.sum(grads, axis=0)
    	w = weights - learning_rate*grads
    return w