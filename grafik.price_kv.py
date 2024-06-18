import pandas as pd
import matplotlib.pyplot as plt

file_path = 'prices.csv'
data = pd.read_csv(file_path)

prices = data['Price']
plt.hist(prices, bins=10, edgecolor='black')

plt.title('Гистограмма цен на аренду квартир в Перми')
plt.xlabel('Цена (в рублях)')
plt.ylabel('Количество объявлений')
plt.grid(True)
plt.show()

