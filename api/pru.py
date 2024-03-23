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

        pais = "ar"

        proxy_options = {
            "proxy": {
                "http": f"http://customer-migruedav-cc-{pais}-sessid-0404864332-sesstime-10:Migruedav1234@pr.oxylabs.io:7777",
                "https": f"https://customer-migruedav-cc-{pais}-sessid-0404864332-sesstime-10:Migruedav1234@pr.oxylabs.io:7777",
                "no_proxy": "localhost,127.0.0.1",
            },
            "verify_ssl": False,
            "suppress_connection_errors": False,
        }

        # driver = webdriver.Chrome(options=options, seleniumwire_options=proxy_options)
        driver = webdriver.Chrome(options=options)
        driver.get("https://ip.oxylabs.io/location")
        location = driver.find_element(by="tag name", value="body").text

        return location
    except Exception as e:
        return str(e)
