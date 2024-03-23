from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def prueba():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youmainlyyou.com/")

    return {"ada": "TPEC"}


prueba()
