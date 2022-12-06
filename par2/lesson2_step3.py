from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    num1 = browser.find_element(By.ID, "num1")
    num1 = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)

    sum = num1 + num2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()