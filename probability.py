import pandas as pd
import numpy as np 
X1=np.array(['A','A','A','B','B','B','C','C'])
X2=np.array(['P','Q','P','Q','P','P','Q','Q'])


##crosstab
pd.crosstab(index=X1,columns=X2)
##joint probability distribution
pd.crosstab(index=X1,columns=X2,normalize='all',margins=True)
##Conditional Probability Distribution for Rows
pd.crosstab(index=X1,columns=X2,normalize='index',margins=True)
#conditional Probabilty Distribution for columns 
pd.crosstab(index=X1,columns=X2,normalize='columns',margins=True)



######cars93
import os
os.chdir(r'C:\adv analytics\Datasets')
cars93=pd.read_csv('Cars93.csv')
##1 --a-----probability distribution by Type
cars93['Type'].value_counts(normalize=True)
#-----b----probability Distribution by AirBags
cars93['AirBags'].value_counts(normalize=True)
#2  join probability by type------------
pd.crosstab(cars93['Type'], cars93['AirBags'],normalize='all',margins=True)
# join probability by AirBags-----
pd.crosstab(cars93['Type'], cars93['AirBags'],normalize='columns',margins=True)