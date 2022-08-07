% matplotlib
inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from tqdm.auto import tqdm
import os

!wget
https: // raw.githubusercontent.com / da - python / python -
for -data - analytics / main / Lesson4 / hometask / test_cluster.csv

df = pd.read_csv('test_cluster.csv', encoding='cp1251', sep=';')
df.head()

pd.set_option("display.max.columns", None)

df.info()

df.plot(x='age', y=['gender', 'city_type', 'min_cl_balance_1q'])
plt.show()

df.plot(x='age', y=['ml_balance']
plt.show()

# зависимость прибыли, получееной от клиента в кореляции с возрастом
exsample = df.set_index('age')['nbi']
exsample.head()

pd.isnull(df)

df.isnull().sum()

df.fillna(0)

df.dropna()

df.dropna(axis=1)

exsample.plot(kind='barh')
plt.show()

from pylab import rcParams

rcParams['figure.figsize'] = 9, 12
exsample.plot(kind='barh')
plt.show()

exsample.plot(kind='bar', logy=True)
plt.show()

# зависимость дохода клиента (income ) и все кредиты ( loan_balance_0m)
dohod = df.set_index('income')['dloan_balance_0m']
dohod.head()

rcParams['figure.figsize'] = 9, 12
dohod.plot(kind='barh')
plt.show()

# Гистограмма
rcParams['figure.figsize'] = 4.5, 5
plt.hist(dohod, ec='white', color='lightgrey')
plt.show()

plt.hist(dohod, bins=3, edgecolor='black')
plt.show()

# full_mob Длительность взаимоотношений с банком и td_balance_0m депозит

depozit = df.set_index('full_mob')['td_balance_0m']
depozit.head()

plt.hist(depozit, bins=3, edgecolor='black')
plt.show()

#  в зависимости от пола клиента gender баланс на счетах клиентов  avgtrx_to_balance


gender_balance = df.set_index('gender')['avgtrx_to_balance']
gender_balance.head()

plt.hist(gender_balance, bins=3, edgecolor='black')
plt.show()

rcParams['figure.figsize'] = 4.5, 5
plt.hist(gender_balance, ec='white', color='lightgrey')
plt.show()

# full_mob Длительность взаимоотношений с банком и casa_balance_0m счета

# full_mob Длительность взаимоотношений с банком и nbi доход от клиента