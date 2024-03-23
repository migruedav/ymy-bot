from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def prueba():

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.example.com")
