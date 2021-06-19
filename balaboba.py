import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write(user_text):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get('https://yandex.ru/lab/yalm?style=0')

    ActionChains(driver).click(driver.find_element_by_xpath('//*[@id="app"]/div/div/button/span')).perform()
    search = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/span/span[2]/textarea')
    search.send_keys(user_text)
    search.send_keys(Keys.ENTER)

    added_text = "\n\nНапиши ещё что-нибудь или нажми кнопку сверху, чтобы вернуться назад (ну или /start)"
    try:
        error = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/p'))
        )
        return error.text + added_text

    except Exception:
        try:
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/span[2]'))
            )
            return f'{user_text} {result.text} {added_text}'
        except Exception:
            return "Произошла неизвестная ошибка! Попробуй ещё раз"

    finally:
        driver.quit()

