from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pru():
    try:
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.get("https://redis.com/")

        return driver.title
    except Exception as e:
        return str(e)
