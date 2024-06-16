# -*- coding: utf-8 -*-
"""Apple Quality EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sLfXg8MeasJWKkQqXy_PKjJLtJWUPkuk
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/apple_quality.csv')
data.head()

# @title Quality

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('Quality').size().plot(kind='bar', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Sweetness

from matplotlib import pyplot as plt
data['Sweetness'].plot(kind='hist', bins=20, title='Sweetness')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Weight

from matplotlib import pyplot as plt
data['Weight'].plot(kind='hist', bins=20, title='Weight')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Size

from matplotlib import pyplot as plt
data['Size'].plot(kind='hist', bins=20, title='Size')
plt.gca().spines[['top', 'right',]].set_visible(False)

sns.barplot(x="Ripeness", y="Sweetness", data=data)

from matplotlib import pyplot as plt
data.plot(kind='scatter', x='Weight', y='Sweetness', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
data.plot(kind='scatter', x='Sweetness', y='Crunchiness', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

import matplotlib.pyplot as plt
plt.scatter(data['A_id'], data['Size'], c=data['Sweetness'], cmap='viridis')
plt.xlabel('Time')
plt.ylabel('Size')
_ = plt.title('Sweetness vs Size over time')

sns.scatterplot(data=data, x="Crunchiness", y="Juiciness", hue="Size")

