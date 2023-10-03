from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)

    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()