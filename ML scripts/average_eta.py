import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  


path = os.getcwd() + '/ex1data1.txt'  
data = pd.read_csv(path, header=None, names=['coulumn1', 'column2'])           #read data from the file 
data.head()                                                              

#cost function
def computeCost(X, y, theta):                                                   
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


# we need to insert a column of 1s at the beginning of the data frame in order to make the matrix operations work correctly 
data.insert(0, 'Ones', 1)  


# set X (training data) and y (target variable)
cols = data.shape[1]  
X = data.iloc[:,0:cols-1]  
y = data.iloc[:,cols-1:cols] 

X = np.matrix(X.values)  
y = np.matrix(y.values)  
theta = np.matrix(np.array([0,0]))  


#print('initial',computeCost(X, y, theta))

def gradientDescent(X, y, theta, alpha, iters):  
    temp = np.matrix(np.zeros(theta.shape))
    
    # .ravel() flattens a matrix into a 1-D array 
    # number of parameters = parameters
    parameters = int(theta.ravel().shape[1])                                   
    cost = np.zeros(iters)

    for i in range(iters):             
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


alpha = 0.02       #learning rate  
iters = 1000      #no. of iterations

#g is tha array containing the values of theta.
#cost is an array containing the cost function values after every iteration.  
g, cost = gradientDescent(X, y, theta, alpha, iters)        

#compute after optimization
#print('final',computeCost(X, y, g))                                          

#the given independent variable data scaled to plot a graph. 
x = np.linspace(data.Population.min(), data.Population.max(), 100)  
#regression equation 
f = g[0, 0] + (g[0, 1] * x) 
print(f)
'''
-----------------------------------------------
f is the estimated output. It has been evaluated 
such that the error is minimum. The minimization
(optimization) algo used is gradient descent. 
'''
