import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 13).until(
        es.text_to_be_present_in_element((By.ID, 'price'), '100')
        )

browser.find_element(By.ID, 'book').click()

x = browser.find_element(By.ID, 'input_value').text
result = calc(x)

browser.find_element(By.CLASS_NAME, 'form-control').send_keys(result)
browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


time.sleep(5)




