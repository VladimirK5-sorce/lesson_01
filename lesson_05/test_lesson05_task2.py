from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        initial_url = "https://httpbin.qa-territory.online/forms/post"
        driver.get(initial_url)

        name_input = driver.find_element(By.NAME, "custname")
        name_input.send_keys("Владимир")

        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        assert driver.current_url != initial_url, (
            f"URL не изменился и остался {initial_url}"
        )
    finally:
        driver.quit()
