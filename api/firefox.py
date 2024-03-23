from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def firefox():
    options = Options()
    options.add_argument("--headless")

    with Display():
        print("Abriendo el navegador Firefox")
        browser = webdriver.Firefox(options=options)
        browser.set_window_size(1120, 550)

        url = "https://tailwindcomponents.com/cheatsheet/"
        browser.get(url)

        title = browser.title
        print(title)
        browser.quit()
