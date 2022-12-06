from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button.click()

    time.sleep(1)

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)

    field = browser.find_element(By.ID, "answer")
    field.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()