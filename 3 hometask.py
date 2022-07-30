!pip install yfinance requests

import requests
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from tqdm.auto import tqdm

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Проанализировать имеющиеся данные.
#Определить базовую формулу цены на условиях FCA (цена на заводе). То есть как бы выглядела цена на исторических данных.
#Отобразить на графике.
#Сделать расчет возможной цены по формуле для каждого из клиентов на условиях DDP (цена с доставкой). Записать все в один эксель файл, на разных листах. Каждый лист - название клиента.
#Предложить формулу цены каждому из клиентов на условиях DDP (цена с доставкой).
#Создать директорию «для клиентов» и в ней сложить файлы с расчетами.
#Каждый клиент - отдельный файл (любой из docx, xlsx, pptx, pdf) с именем клиента…

customers = {
    'Monty':{
        'location':'EU',
        'volumes':200,
        'formula':'moving_average'
    },

    'Triangle':{
        'location':'CN',
        'volumes': 30,
        'formula': 'monthly'
    },
    'Stone':{
        'location':'EU',
        'volumes': 150,
        'formula': 'moving_average'
    },
    'Poly':{
        'location':'EU',
        'volumes': 70,
        'formula': 'monthly'
    }
}



year = '2022'
month = '05'
url = f"https://www.lgm.gov.my/webv2api/api/rubberprice/month={month}&year={year}"
res = requests.get(url)
rj = res.json()
df = pd.json_normalize(rj)
df.head()

df_dict = {}
for ticker in tqdm(['CL=F','USDRUB=X', 'EURUSD=X', 'EURRUB=X']):
    df = yf.download(ticker)
    df = df.Close.copy()
    df = df.resample('M').mean()
    df_dict[ticker] = df

main_df = pd.concat(df_dict.values(), axis=1)
main_df.columns = ['CRUDE_OIL_USD','USDRUB', 'EURUSD', 'EURRUB']
main_df = main_df.loc['2019-06-30':'2022-06-30'].copy()
main_df['MWP_PRICE_EUR'] = main_df.CRUDE_OIL_USD * 16 * (1/main_df.EURUSD) + 400
main_df['MWP_PRICE_USD'] = main_df.CRUDE_OIL_USD * 16 + 400 * main_df.EURUSD
main_df['MWP_PRICE_EUR_EU'] = main_df['MWP_PRICE_EUR'] + EU_LOGISTIC_COST_EUR
main_df['MWP_PRICE_USD_CN'] = main_df['MWP_PRICE_USD'] + CN_LOGISTIC_COST_USD
main_df['MWP_PRICE_EUR_EU_MA'] = main_df.MWP_PRICE_EUR_EU.rolling(window=3).mean()


from pylab import rcParams
rcParams['figure.figsize'] = 15,7

discounts = {100: 0.01, 300: 0.05, 301: 0.1}

