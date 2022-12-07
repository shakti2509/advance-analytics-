import pandas as pd
import numpy as np
import os
os.chdir(r"C:\adv analytics\Datasets")
cars93=pd.read_csv("Cars93.csv")
print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
print(cars93.info())
cars93['Price'].mean()
cars93['Price'].median()
cars93['Price'].quantile(q=0.25)
cars93['Price'].quantile(q=0.75)
cars93['Price'].quantile(q=[0.25,.50,.75])
