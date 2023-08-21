import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x1 = np.arange(-5, 5, 0.1)
x2 = np.arange(-5, 5, 0.1)
X1, X2 = np.meshgrid(x1, x2)

def aim():
    return np.sin(X1 + X2) + np.power((X1 - X2), 2) - 1.5*X1 + 2.5*X2 + 1
        
if __name__ == "__main__":
    Z = aim()
    fig = plt.figure(figsize = (12, 12))
    ax = Axes3D(fig)
    surf = ax.plot_surface(X1, X2, Z, cmap = cm.coolwarm, label = "Mocormick")
    plt.savefig('Mocormick.png', dpi = 250)
