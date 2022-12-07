import pandas as pd
import numpy as  np 
import os 
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r"C:\adv analytics\Datasets")
house=pd.read_csv('Housing.csv')
print(house.info)
print(house.shape)
house['price'].mean()
house['price'].median()
house['price'].mode()
house['price'].quantile(q=.25)
house['price'].quantile(q=[.25,.50,.75])
house['price'].plot(kind='box')
plt.show()
#on price
#skew
from scipy.stats import skew
skew(house['price'])
house['price'].skew()
#kurtosis
from scipy.stats import kurtosis
kurtosis(house['price'],fisher=True)
house['price'].kurtosis()
#histogram
house['price'].plot(kind='hist',bins=8)
plt.show() 

#--seaborn
sns.histplot(data=house,x='price',bins=8)
plt.title('histogram')
plt.show()
#2
#scatter plot
sns.scatterplot(data=house,x='lotsize',y='price',hue='airco')
plt.xlabel('lotsize')
plt.ylabel('price')
plt.title('lotsize')
plt.show()
#3-----
#display boxplot
#1
sns.boxplot(data=house,x='lotsize',y='price')
plt.show()
#2
sns

