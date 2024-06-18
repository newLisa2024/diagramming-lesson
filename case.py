from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

url = "https://perm.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"
driver.get(url)

try:
    # Открываем страницу с объявлениями на Циан
    driver.get("https://perm.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/")

    # Даем странице время на загрузку
    time.sleep(5)

    # Ищем элементы, содержащие цены
    prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

    # Сохраняем найденные цены в список
    price_list = []
    for price in prices:
        price_text = price.text.replace(' ₽/мес.', '').replace(' ', '')
        if price_text.isdigit():
            price_list.append(int(price_text))

    # Записываем цены в CSV файл
    with open('prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Записываем заголовок
        for price in price_list:
            writer.writerow([price])

    print("Цены успешно сохранены в файл prices.csv")

finally:
    # Закрываем браузер
    driver.quit()

    # Выводим цены
    print(price_list)
