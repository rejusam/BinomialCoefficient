import numpy as np
from decimal import *
import scipy.special
from scipy.special import factorial
import pandas as pd
from math import e
from math import pi
import matplotlib.pyplot as plt
import seaborn as sns


getcontext().prec = 1000

n = 9000
c = []
for i in range(0,n+1):
    a = sum(scipy.special.comb(Decimal(i), (r), exact=True)*pow(-1, r)/Decimal(factorial(r, exact=True)) for r in range(i+1))
    c.append(a)



df_dist = {'i':range(0, n+1), 'sum': c}

df = pd.DataFrame(df_dist)
df = df.set_index('i')
df.to_csv('tiju_summation_9000.csv', index=True)


