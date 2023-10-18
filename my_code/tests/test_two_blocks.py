from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Jaikhun')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Jaikhun')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('Jaikhun@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.form-control.first').send_keys('Jaikhun')
        browser.find_element(By.CSS_SELECTOR, '.form-group.second_class').send_keys('Jaikhun')
        browser.find_element(By.CSS_SELECTOR, '.form-group.third_class').send_keys('Jaikhun@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()