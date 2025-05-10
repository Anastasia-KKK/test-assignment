from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

title = driver.title
if "Example" in title:
    print("Заголовок содержит слово Example")
else:
    print("Заголовок не содержит слово Example")

try:
    link = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.iana.org/domains/example"]')
    print("Найден элемент со ссылкой 'More information'")
except:
    print("Элемент со ссылкой не найден")
    driver.quit()
    exit()

try:
    link.click()
    print("Клик по ссылке выполнен")
except:
    print("Не удалось кликнуть по ссылке")
    driver.quit()
    exit()

time.sleep(2)

expected_url = "https://www.iana.org/help/example-domains"
current_url = driver.current_url

if current_url == expected_url:
    print("Перенаправление на страницу выполнено успешно:", current_url)
else:
    print(f"Перенаправление не удалось. Ожидаемый результат: {expected_url}, Фактический результат: {current_url}")

driver.quit
print("Тест завершен")

