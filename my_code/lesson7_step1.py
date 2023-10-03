from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)


    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()