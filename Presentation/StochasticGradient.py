import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets.samples_generator import make_blobs

X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.75)
for l in range(100,1,-1):
    clf = SGDClassifier(loss="perceptron", alpha=0.01, max_iter=101-l, fit_intercept=True)
    clf.fit(X, Y)

    xx = np.linspace(-1, 5, 10)
    yy = np.linspace(-1, 5, 10)

    X1, X2 = np.meshgrid(xx, yy)
    Z = np.empty(X1.shape)
    for (i, j), val in np.ndenumerate(X1):
        x1 = val
        x2 = X2[i, j]
        p = clf.decision_function([[x1, x2]])
        Z[i, j] = p[0]
    levels = [0.0]
    linestyles = ['solid']
    colors = [(0,0,0,(100-l)/100.0)]
    plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired,
            edgecolor='black', s=20)

plt.show()