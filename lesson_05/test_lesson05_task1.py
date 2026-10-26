from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    # Настройка, чтобы игнорировать ошибки сертификатов безопасности
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    base_url = "https://qa-territory.online"
    driver.get(base_url)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    expected_url = f"{base_url}/forms/post"
    assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, но получили {driver.current_url}"

    driver.back()

    assert driver.current_url == f"{base_url}/", f"Ожидался возврат на {base_url}/, но получили {driver.current_url}"

    driver.quit()
