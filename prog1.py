import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os
os.chdir(r'C:\adv analytics\Datasets')
cars93=pd.read_csv('Cars93.csv')
print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
print(cars93.info)
cars93['Price'].mean()
cars93['Price'].median()
cars93['Price'].mode()
cars93['Price'].quantile(q=.25)
cars93['Price'].quantile(q=[.25,.50,.75])
cars93['Price'].plot(kind='box')
plt.show()

cars93['Price'].std()
#varience
cars93['Price'].var()
#cofficent of varrition 
cv=cars93['Price'].std()/cars93['Price'].mean()
print(cv)
#skewness
from scipy.stats import skew
skew(cars93['Price'])
cars93['Price'].skew()
#kurtosis
from scipy.stats import kurtosis
kurtosis(cars93['Price'],fisher=True)
cars93['Price'].kurtosis()