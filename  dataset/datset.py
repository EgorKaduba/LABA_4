import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, names=columns)

# Просмотр первых 5 строк
print(iris_data.head())

# Проверка на наличие пропусков
print(iris_data.isnull().sum())

# Визуализация
plt.figure(figsize=(12, 6))

# Диаграмма рассеяния между длиной и шириной лепестков
sns.scatterplot(data=iris_data, x='petal_length', y='petal_width', hue='species', palette='deep')

plt.title('Рассеяние длины и ширины лепестков ирисов')
plt.xlabel('Длина лепестка (см)')
plt.ylabel('Ширина лепестка (см)')
plt.legend(title='Вид ириса')
plt.show()

# Вычисление коэффициента корреляции
correlation = iris_data[['petal_length', 'petal_width']].corr().iloc[0, 1]
print(f'Коэффициент корреляции между длиной и шириной лепестков: {correlation}')

# Интерпретация результата
if correlation > 0:
    print("Существует положительная корреляция.")
elif correlation < 0:
    print("Существует отрицательная корреляция.")
else:
    print("Корреляции нет.")
