from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(2)
    confirm = browser.switch_to.alert.accept()
    time.sleep(1)

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, "[name=text]")
    field.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()