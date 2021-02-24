# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:12:18 2021

@author: roger
"""
import numpy as np


# X=np.asarray([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
# y=np.asarray([1,1,-1,-1,-1])
# y=y.reshape(-1,1)
X=np.asarray([[-1,1],[1,-1],[1,1],[2,2]])
y=np.asarray([1,1,-1,-1,])
y=y.reshape(-1,1)

mistakes=0
thetas=[]



        
# empezando en x1 to converge
# status=False
# while status==False:
#     for t in range(10):
#         for i in range(X.shape[0]):
        
#             sign=y[i]*(theta.dot(X[i,:]))
#             if sign <= 0:
#                 mistakes+=1
#                 theta=theta+(y[i]*X[i,:])
#                 thetas.append(theta)
            
#             predictions=theta.dot(X.T)
#             status= ((y*predictions.T)>0).all()
        
# # emepzando en x2 to converge
# status=False
# while status==False:
#     for t in range(10):
#         for i in range(1,X.shape[0]):
        
#             sign=y[i]*(theta.dot(X[i,:]))
#             if sign <= 0:
#                 mistakes+=1
#                 theta=theta+(y[i]*X[i,:])
#                 thetas.append(theta)
            
#             predictions=theta.dot(X.T)
#             status= ((y*predictions.T)>0).all()


# TO MATCH NUMBER OF MISTAKES 

# adding column of 1's
X=np.concatenate((X,np.ones((X.shape[0],1))),axis=1)
theta=np.ones((1,3))

# x1
status=False
while status==False:
    for t in range(10):
        for i in range(X.shape[0]):
        
            sign=y[i]*(theta.dot(X[i,:]))
            if sign <= 0:
                mistakes+=1
                theta=theta+(y[i]*X[i,:])
                thetas.append(theta)
            predictions=theta.dot(X.T)
            status= ((y*predictions.T)>0).all()

# INITIAL THETAS THAT DONT CAUSE MISTAKES FOR AN EPOCH

# X=np.asarray([[-1,1],[1,-1],[1,1],[2,2]])
# y=np.asarray([1,1,-1,-1,])
# y=y.reshape(-1,1)
# theta=np.zeros((1,3))
# mistakes=0
# thetas=[]
# status=False
# while status==False:
#     for t in range(10):
#         for i in range(X.shape[0]):

#             sign=y[i]*(theta.dot(X[i,:]))
#             if sign <= 0:
#                 mistakes+=1
#                 theta=theta+(y[i]*X[i,:])
#                 thetas.append(theta)

#             predictions=theta.dot(X.T)
#             status= ((y*predictions.T)>0).all()
import matplotlib.pyplot as plt
plt.plot(X[:,0],X[:,1],"x")
plt.plot(X.dot(theta.T),"--")

print(mistakes)
print(thetas)