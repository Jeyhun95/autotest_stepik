from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  math

value = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

 #   browser.find_element(By.LINK_TEXT, value).click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
'''
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for element in elements:
        element.send_keys("Ляляля")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
# не забываем оставить пустую строку в конце файла