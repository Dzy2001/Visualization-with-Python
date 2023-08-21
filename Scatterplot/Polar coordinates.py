import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

#fig = plt.figure(figsize = (12, 12))
#ax = fig.add_subplot(projection='polar')
#c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
#plt.savefig('polar coordinates.png', dpi = 250)

fig = plt.figure(figsize = (12, 12))
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
plt.savefig('polar coordinates.png', dpi = 250)
