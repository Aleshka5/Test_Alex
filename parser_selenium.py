from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import numpy as np

from solve_authentication import get_chromedriver

def parse_the_cite(base_url, proxy_ip, proxy_port, use_new_proxi = False):
    """
    This parser works with website Ralph Lauren.
    It task is - get all HTML documents from the website.

    :param url: - website url, which we parse
    :return: - None. All data saves to folder "template"

    """
    if not os.path.exists('templates'):
        os.makedirs("templates")

    # Index of the first element for the request
    i = 0 # You can use 0 - 32 - 64 - 96 or 128 value to start function for different pages if you need

    pagination_size = 32 # The number of items, which renders on the website
    count_items = 142    # The number of all items on the website
    while i < count_items:

        # Decrease of pagination size for the last request
        if i + pagination_size > count_items:
            pagination_size -= i + pagination_size - count_items

        # Try request using Selenium
        try:
            if not use_new_proxi:
                # Proxy authentication
                driver = get_chromedriver(use_proxy=True)
            else:
                path = os.path.dirname(os.path.abspath(__file__))
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(f"--proxy-server={proxy_ip}:{proxy_port}")
                driver = driver = webdriver.Chrome(service=Service(os.path.join(path, 'chromedriver')),
                                                    options=chrome_options)

            url = base_url + f'?sw1=sw-cache-me&webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts&start={i}&sz={pagination_size}'
            print(url)
            # Get the website
            driver.get(url)


            # Scroll down to see the footer
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(webdriver.common.by.By.CLASS_NAME,'footer-container')).perform()
            time.sleep(1)

            # Create a folder if not exists
            if not os.path.exists('templates'):
                os.makedirs("templates")

            # Save a website page source
            #with open(f'templates/page{i}_{i + pagination_size}.html','w',encoding='utf-8') as file:
            #    file.write(driver.page_source)
            driver.close()

            # Preparing for new request
            i += pagination_size
            print(f'Done {i} out of {count_items}.')

            # if we have next request, please wait for a while
            if i < count_items:
                sleeping_time = round(0.2 + np.random.sample(), 2)
                print(f'Waiting time for the next request: {sleeping_time} min')
                time.sleep(sleeping_time*60)

        except Exception as _ex: # If we get incorrect data from website
            print('Try again...')
            # Close the last session
            driver.close()

            # Waiting time for the next request
            if i < count_items:
                sleeping_time = round(0.7 + np.random.sample(), 2)
                print(f'Waiting time for the next request: {sleeping_time} min')
                time.sleep(sleeping_time * 60)

if __name__ == '__main__':
    proxy_host = '135.181.14.45'
    proxy_port = '5959'
    parse_the_cite(base_url='https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204',proxy_ip=proxy_host,proxy_port=proxy_port,use_new_proxi = True)