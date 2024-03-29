# 3. Попробуйте ответить на вопросы:
# Сколько вакансий, которые вам нравятся?
# За какие периоды эти вакансии?
# Сколько вакансий с такими позициями, на которых вы работаете?
# Сколько вакансий для аналитика данных?
# Сколько вакансий для аналитика данных с использованием Python?


!pip install wget
!wget https://raw.githubusercontent.com/da-python/python-for-data-analytics/main/Lesson1/hometask/vacancy.csv.zip
!unzip vacancy.csv.zip

import csv
import sys
from collections import Counter, defaultdict

file_path = 'vacancy.csv'
vacs = list(csv.DictReader(open(file_path)))

#Вакансии, которые нравятся
[x.get('vactitle') for x in vacs if x.get('vactitle').lower(). find('аналитик') > -1]

# сколько вакансий, которые нравятся
len([x.get('vactitle') for x in vacs if x.get('vactitle').lower(). find('аналитик') > -1])

# за какой период вакансии, которые нравятся (вывела уникальные значения)
set([(x.get('created_at'), x.get('updated_at')) for x in vacs if x.get('vactitle').lower(). find('аналитик') > -1])

# Сколько вакансий для аналитика данных?
len([x.get('vactitle') for x in vacs if x.get('vactitle').lower(). find('аналитик данных') > -1])

# Сколько вакансий с такими позициями, на которых вы работаете?
len([x.get('vactitle') for x in vacs if x.get('vactitle').lower(). find('главный специалист') > -1])

# Сколько вакансий для аналитика данных с использованием Python?

len([(x.get('vactitle'), x.get('vacdescription')) for x in vacs if (x.get('vactitle').lower(). find('аналитик данных') > -1)
                                                                if (x.get('vacdescription')).lower(). find('python')])

