import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import os
os.chdir(r'C:\adv analytics\Datasets')

cars93=pd.read_csv('Cars93.csv')
print(cars93.info())

#for type bar 
cts=cars93['Type'].value_counts()
cts.plot(kind='bar')
plt.show(cts)
#for airbags bar 
cts=cars93['AirBags'].value_counts()
cts.plot(kind='bar')
plt.show(cts)
#Matplotlib
plt.bar(cts.index,cts)
plt.show()

#seaborn
cts1=cts.reset_index()
cts1.columns=['Type','Count']
sns.barplot(data=cts1,x='Type',y='Count')
plt.show()
##Histogram
cars93['Price'].plot(kind='hist',bins=15)
plt.show()
## matplotlib
plt.hist(cars93['Price'],bins=15)
#seaborns
sns.histplot(data=cars93,x='Price',bins=8)
plt.show()
### density plot /distribution plot
cars93['Price'].plot(kind='kde')
plt.show()
#seaborn
sns.kdeplot(data=cars93,x='Price')
plt.show()
#Scaterr plot 
cars93.plot(kind='scatter', x='EngineSize',y='MPG.highway')
plt.title('scatter Plot')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')
plt.show()
#matplotlib
plt.scatter(cars93['EngineSize'],cars93['MPG.highway'])
plt.title('scatter Plot')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')
plt.show()


no_bags=cars93[cars93['AirBags']=='None']
plt.scatter(no_bags['EngineSize'],no_bags['MPG.highway'],label='No AirBags',c='red')
driver=cars93[cars93['AirBags']=='Driver only']
plt.scatter(no_bags['EngineSize'],no_bags['MPG.highway'],label='Driver Only')
d_p=cars93[cars93['AirBags']=='Driver & Passanger']
plt.scatter(d_p['EngineSize'],d_p['MPG.highway'],label='Driver & Passnager',color='magenta')
plt.legend(loc='best')
plt.title('scatter Plot')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')
plt.show()
#seaborn
sns.scatterplot(data=cars93, x='EngineSize',y='MPG.highway')
plt.title('scatter Plot')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')
plt.show()
#boxplot
cars93['Price'].plot(kind='box')
plt.title('Box Plot')
plt.show()
#seaborn
sns.boxplot(y='Price',data=cars93)
plt.show()

sns.boxplot(x='AirBags',y='Price',data=cars93)
plt.show()
##facet grid
g=sns.FacetGrid(cars93,col="AirBags")
g=g.map(plt.scatter,'EngineSize', 'MPG.highway')
plt.show()
#row wise
g=sns.FacetGrid(cars93,row="AirBags")
g=g.map(plt.scatter,'EngineSize', 'MPG.highway')
plt.show()
#subplot --tight---1*2 graph 
plt.subplot(1,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title('Historam')

plt.subplot(1,2,2)
sns.histplot(data=cars93,x='Price',bins=8)
plt.title('histogram')
plt.tight_layout()
plt.show()
#subplot 2*2

plt.subplot(2,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title('Historam')

plt.subplot(2,2,2)
sns.histplot(data=cars93,x='Price',bins=8)
plt.title('histogram')

plt.subplot(2,2,3)
sns.scatterplot(data=cars93, x='EngineSize',y='MPG.highway')
plt.title('scatter Plot')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')

plt.subplot(2,2,4)
cts=cars93['AirBags'].value_counts()
cts.plot(kind='bar')
plt.tight_layout()
plt.show()
#joint plot
sns.jointplot(data=cars93,x='EngineSize',y='MPG.highway')
plt.ylabel('Milage on Highway')
plt.xlabel('Engine size')
plt.show()
#agregation by group by 
# by matplolib
cts=cars93.groupby('AirBags')['Price'].mean()
plt.bar(cts.index,cts)
plt.ylabel('mean.price')
plt.show()
#by seaborn
cts=cars93.groupby('AirBags')['Price'].mean()
cts1=cts.reset_index()
sns.barplot(x='AirBags',y='Price',data=cars93)
plt.show()