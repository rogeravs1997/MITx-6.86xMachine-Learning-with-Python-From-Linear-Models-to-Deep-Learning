import numpy as np
y=np.array([2,2.7,-0.7,2])
X=np.array([[1,0,1],[1,1,1],[1,1,-1],[-1,1,1]])
theta=np.array([0,1,2])

y.shape=(-1,1)
theta.shape=(-1,1)

preds=X.dot(theta)

def hinge_loss(X,y,theta):
    preds=X.dot(theta)
    z=y-preds
    
    loss=0
    
    for i in z:
        if i >= 1:
            loss+=0
        else:
            loss+=(1-i)
    
    return loss

hingeLoss=hinge_loss(X, y, theta)

def SEL(X,y,theta):
    preds=X.dot(theta)
    z=y-preds
    
    loss=(sum(z**2)/2)
    
    return loss

SELLoss=SEL(X, y, theta)
    
    