import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams["font.family"] = "FangSong"
matplotlib.rcParams["font.size"] = 15

labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
labels1 = ['Frogs', 'Hogs', 'Dogs']
labels2 = ['J-20', 'F-22', 'F-35', 'Su-57', 'J-35', 'F/A-18E/F']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) 

fig, ax = plt.subplots(1, 3, figsize = (16, 8))

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax[0].pie(vals.sum(axis = 1), labels = labels1, radius = 1, colors = outer_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[0].pie(vals.flatten(), labels = labels2, radius = 1-size, colors = inner_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[0].set(aspect = 'equal', title='Pie plot with `ax.pie`')

ax[1].pie(vals.sum(axis = 1), labels = labels1, radius = 1, colors = outer_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[1].pie(vals.flatten(), labels = labels2, radius = 1-size, colors = inner_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[1].set(aspect = 'equal', title='Pie plot with `ax.pie`')

ax[2].pie(vals.sum(axis = 1), labels = labels1, radius = 1, colors = outer_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[2].pie(vals.flatten(), labels = labels2, radius = 1-size, colors = inner_colors, wedgeprops = dict(width = size, edgecolor = 'w'))

ax[2].set(aspect = 'equal', title='Pie plot with `ax.pie`')

plt.savefig('Multiple ring pie charts.png', dpi = 250)
