from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    firstname = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    firstname.send_keys("Artem")

    lastname = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    lastname.send_keys("Revin")

    email = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    email.send_keys("artiesy@mail.ru")

    file = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()