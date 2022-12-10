from scipy.stats import binom 
import numpy as np
#1
binom.pmf(k=5, n=40, p=0.25)

#2
ks =np.arange(0,11)
s=0
for i in ks:
    s=s+binom.pmf(k=i, n=40, p=0.25)
print(s) 
#or
binom.cdf(k=10, n=40, p=0.25)

#3

binom.sf(k=19, n=40, p=0.25)
#4
binom.stats(n=40,p=0.25)


#------------------- 20 worker -----
#1-----a

binom.pmf(k=5,n=20,p=0.15)
#b
binom.sf(k=12,n=20,p=0.15)
#c
binom.cdf(k=10,n=20,p=0.15)

#2----------------disorder ----------
#a
binom.pmf(0,20,.35)
#b
binom.pmf(10,20,.35)
#c
binom.cdf(k=10,n=20,p=.35)
#d
binom.sf(13,20,.35)
#poisson
#example
from scipy.stats import poisson
#a
poisson.pmf(5,12)
#b
poisson.cdf(12,12)
#c
poisson.sf(14,12)
#d
ks=np.arange(10,16)
s=0
for i in ks:
    s=s+poisson.pmf(i,12)
print(s)

#or
poisson.cdf(15,12)-poisson.cdf(9,12)    

#poisson  distribution    
#1---a
poisson.sf(70, 56)
#b
poisson.cdf(19,56)
#2 a---
poisson.sf(5, 4)
#--b
poisson.cdf(2, 4)
#normalization 

from scipy.stats import norm
#example---1
norm.cdf(58,64,4)
#example--2
norm.sf(200,180,30)

#question 
#1
norm.ppf(.95,100,15)
#2
#a
norm.sf(2000,1678,500)
#b
norm.ppf(.9,1678,500)
#c
norm.cdf(1900,1678, 500)-norm.cdf(1000,1678,500)

#example 3
#a
norm.ppf(.98,313,57)
#b
norm.ppf(.90,93,22)
#c
pa=norm.sf(450,313,57)
pb=norm.sf(150,93,22)
pa+pb-pa*pb
