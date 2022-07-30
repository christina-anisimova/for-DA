
import requests
from tqdm.auto import tqdm
import pandas as pd

sber = '3529'
page = 1
num_per_page = 100
moscow = 1
url = f'https://api.hh.ru/vacancies?employer_id={sber}&page={page}&per_page={num_per_page}&area={moscow}'

url = f'https://api.hh.ru/vacancies'
params = {
    'employer_id':sber,
    'page':page,
    'per_page':num_per_page,
    'area':moscow,
}
res = requests.get(url, params=params)

res.json()


res = requests.get(url)
print(res)


vacancies = res.json()
num_pages = vacancies.get('pages')
num_pages


vacancies.keys()

vacancies.get('items')[0]

v = vacancies.get('items')

v[0].get('')

vacancies = res.json()
num_pages = vacancies.get('pages')
vacancy_ids = [el.get('id') for el in vacancies.get('items')]

#ошибка

vacancies.keys()

vnum  = vacancies.get('pages')


all_vacancy_ids= []
for i in tqdm(range(vnum)):
    url = f'https://api.hh.ru/vacancies?employer_id={sber}&page={i}&per_page={num_per_page}&area={moscow}'
    res = requests.get(url)
    vacancies = res.json()
    vacancy_ids = [el.get('id') for el in vacancies.get('items')]
    all_vacancy_ids.extend(vacancy_ids)

#ошибка