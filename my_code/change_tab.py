from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)

    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()