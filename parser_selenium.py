from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import numpy as np

from solve_auntithication import get_chromedriver

def parse_the_cite(base_url):
    """
    Этот парсер работает напрямую с сайтом.
    Его задача - получить все нужные HTML документы из интернета.

    :param url: - url сайта, который мы парсим
    :return: - None. Все данные сохраняются в папку template

    """
    if not os.path.exists('templates'):
        os.makedirs("templates")

    i = 0 # Индекс стартового элемента для запроса
    pagination_size = 32 # Колличество выводимых элементов на сайт
    count_items = 134 # Всго страниц на сайте
    while i < count_items:
        # Уменьшение пагинации для последнего запроса
        if i + pagination_size > count_items:
            pagination_size -= i + pagination_size - count_items

        # Поптыка запроса
        try:
            # Аутентификация proxy
            driver = get_chromedriver(use_proxy=True)
            url = base_url+f'?sw1=sw-cache-me&webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts&start={i}&sz={pagination_size}'
            # Заходим на сайт
            driver.get(url)

            # Листаем его до footer
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(webdriver.common.by.By.CLASS_NAME,'footer-container')).perform()
            time.sleep(1)            

            # Сохраняем страницу
            with open(f'templates/page{i}_{i + pagination_size}.html','w',encoding='utf-8') as file:
                file.write(driver.page_source)
            driver.close()

            # Подготовка к новому запросу
            i += pagination_size
            print(f'Готово {i} из {count_items}.')            
            # Ожидание, чтобы не нагружать сайт
            if i < count_items:
                sleeping_time = round(0.5 + np.random.sample(), 2)
                print(f'Время ожидания до следующего запроса: {sleeping_time} мин')
                time.sleep(sleeping_time*60)

        except Exception as _ex: # Если сайт заподозрил, что-то неладное
            print('Попробуем ещё раз...')
            # Закрываем прошлую сессию
            driver.close()

            # Ожидаем, чтобы не нагружать сайт            
            if i < count_items:
                sleeping_time = round(0.5 + np.random.sample(), 2)
                print(f'Время ожидания до следующего запроса: {sleeping_time} мин')
                time.sleep(sleeping_time * 60)

if __name__ == '__main__':
    parse_the_cite('https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204')
