import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors, datasets

iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target

a = [0,1,2,3,11,5,6,7,8,9,10]

a = np.delete(a,3)

print(a)

def ONN(X,y,u):
    """Classifies by the nearest training object

    Keyword arguments:
    X -- training sample
    y -- classes of training samples
    u -- object to classify
    """
    return y[np.argmin([(x[0]-u[0])**2 + (x[1]-u[1])**2 for x in X])]

def KNN(X,y,u,k):
    """Classifies by K nearest training object

    Keyword arguments:
    X -- training sample
    y -- classes of training samples
    u -- object to classify
    k -- number of near object to classify
    """
    L = [(x[0]-u[0])**2 + (x[1]-u[1])**2 for x in X]
    L,y = zip(*sorted(zip(L, y)))
    l = []
    for i in range(0,k):
        l.append(y[i])
    u, c = np.unique(l, return_counts=True)
    return u[np.argmax(c)]


def LOOforKNN(X,y):
    diff = len(X)
    gk = 0
    kvarray = []
    u = [[],0]
    for k in range(1,len(X)):
        cd = 0
        for i in range(1,len(X)):
            u[0] = X[i]
            u[1] = y[i]
            Xt = np.delete(X,i,0)
            yt = np.delete(y,i)
            if(KNN(Xt,yt,u[0],k)!=u[1]):
                cd = cd+1
        if(diff>cd):
            diff = cd
            gk = k
        kvarray.append(cd)
    return gk,kvarray

gk,ga = LOOforKNN(X,y)
print(gk)

plt.plot([x for x in range(1,len(X))], ga, 'ro')
plt.axis([0, len(X)+1, 0, ga[np.argmax(ga)]+1])
plt.show()