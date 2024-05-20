import pandas as pd
from datetime import datetime
# Считываем данные из базы данных или файла
data = pd.read_csv('data.csv')
# Преобразуем дату из строки в формат datetime
data['date'] = pd.to_datetime(data['date'])
# Фильтруем данные по определенным условиям
filtered_data = data[data['product'] == 'Product A']
# Группируем данные по дате
grouped_data = filtered_data.groupby('date').sum()
# Сохраняем результат в новый файл
grouped_data.to_csv('result.csv')
