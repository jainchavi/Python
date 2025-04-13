import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

#reding the datasets
df = pd.read_csv('Play_Store_2.csv')
print(df.head(3))

#checking the shape
print(df.shape)


#checking the data types of the columns of the datasets
print(df.info)


#statistical summary
print(df.describe(include='all'))

#observation of data ----graphs
sns.histplot(data = df , x='Rating')
plt.show()

sns.boxplot(data = df , x='Rating')
plt.show()