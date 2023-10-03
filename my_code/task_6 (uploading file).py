from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys('Jaikhun')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys('Israfilzade')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys('some@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element  = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()



finally:
    time.sleep(10)
    browser.quit()