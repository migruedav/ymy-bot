from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver


def pru():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--user-data-dir=/root/code/ymy-bot")
        options.binary_location = "/root/code/ymy-bot"

        driver = webdriver.Chrome(options=options)
        driver.get("https://ip.oxylabs.io/location")
        location = driver.find_element(by="tag name", value="body").text

        return location
    except Exception as e:
        return str(e)
