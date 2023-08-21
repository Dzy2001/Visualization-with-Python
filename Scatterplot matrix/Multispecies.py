import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import palettable
from sklearn import datasets
import seaborn as sns

iris = datasets.load_iris()
x, y = iris.data, iris.target
y1 = np.array(['setosa' if i == 0 else 'versicolor' if i == 1 else 'virginica' for i in y])
columns = ['sepal length(cm)', 'sepal width(cm)', 'petal length(cm)', 'petal width(cm)', 'class']
pd_iris = pd.DataFrame(np.hstack((x, y1.reshape(150, 1))), columns = columns)

pd_iris['sepal length(cm)'] = pd_iris['sepal length(cm)'].astype('float64')
pd_iris['sepal width(cm)'] = pd_iris['sepal width(cm)'].astype('float64')
pd_iris['petal length(cm)'] = pd_iris['petal length(cm)'].astype('float64')
pd_iris['petal width(cm)'] = pd_iris['petal width(cm)'].astype('float64')

#g = sns.pairplot(pd_iris)
#g.fig.set_size_inches(12, 12)
#sns.set(style = 'whitegrid', font_scale = 1.5)
#plt.savefig('scatterplot matrix.png', dpi = 250)

#g = sns.pairplot(pd_iris, hue = 'class')
#g.fig.set_size_inches(12, 12)
#sns.set(style = 'whitegrid', font_scale = 1.5)
#plt.savefig('plus categorical variables.png', dpi = 250)

#g = sns.pairplot(pd_iris, hue = 'class', kind = 'reg')   # 默认为scatter reg加上趋势线
#g.fig.set_size_inches(12, 12)
#sns.set(style = 'white', font_scale = 1.5)
#plt.savefig('non-diagonal scatterplot plus trendline.png', dpi = 250)

#g = sns.pairplot(pd_iris, hue = 'class', diag_kind = 'hist')
#g.fig.set_size_inches(12, 12)
#sns.set(style = 'whitegrid', font_scale = 1.5)
#plt.savefig('replacement of graphic types on the diagonal.png', dpi = 250)

g = sns.PairGrid(pd_iris, hue = 'class')
g.fig.set_size_inches(12, 12)
g = g.map_upper(sns.scatterplot)
g = g.map_lower(sns.kdeplot, colors = "C0")
g = g.map_diag(sns.kdeplot, lw = 2)
g = g.add_legend()
sns.set(style = 'whitegrid', font_scale = 1.5)
plt.savefig('Diagonal up, diagonal down, and diagonal plotting of different types of diagrams.png', dpi = 250)
