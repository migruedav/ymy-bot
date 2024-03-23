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

        # Asumiendo que la ubicación se muestra en el cuerpo de la página
        location = driver.find_element_by_tag_name("body").text

        return location
    except Exception as e:
        return str(e)
