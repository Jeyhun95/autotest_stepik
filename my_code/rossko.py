from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://nsk.rossko.ru")

    hover = browser.find_element(By.CSS_SELECTOR, '.header-top__menu-inner > .header-top__menu-item:nth-child(3)')  # Наведение мыши
    ActionChains(driver).move_to_element(hover).perform()

 #   browser.find_element(By.CSS_SELECTOR, '.header-top__menu-inner > .header-top__menu-item:nth-child(3)')



finally:
    time.sleep(10)
    browser.quit()