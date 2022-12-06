from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input.form-check-input#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "input.form-check-input#robotsRule")
    radiobutton.click() 
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()