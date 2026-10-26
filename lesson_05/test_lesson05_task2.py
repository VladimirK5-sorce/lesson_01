from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    initial_url = "https://qa-territory.online"
    driver.get(initial_url)

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Владимир")

    submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
    submit_button.click()

    assert driver.current_url != initial_url, (
        f"URL не изменился и остался {initial_url}"
    )

    driver.quit()
