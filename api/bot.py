# import random
# import time
# from selenium import webdriver
# from seleniumwire import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService


# def bot():
#     try:
#         paises = []

#         for i in range(70):
#             paises.append("mx")
#         for i in range(15):
#             paises.append("us")
#         for i in range(5):
#             paises.append("es")

#         paises.extend(["ar", "co", "pe", "cl", "br", "ec", "gt", "cu", "do", "bo"])

#         pais = random.choice(paises)
#         print(pais)
#         proxy_options = {
#             "proxy": {
#                 "http": f"http://customer-migruedav-cc-{pais}-sessid-0404864332-sesstime-10:Migruedav1234@pr.oxylabs.io:7777",
#                 "https": f"https://customer-migruedav-cc-{pais}-sessid-0404864332-sesstime-10:Migruedav1234@pr.oxylabs.io:7777",
#                 "no_proxy": "localhost,127.0.0.1",
#             },
#             "verify_ssl": False,  # Desactivar la verificación SSL
#             "suppress_connection_errors": False,  # Mostrar errores de conexión
#         }

#         options = Options()
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         prefs = {
#             "profile.managed_default_content_settings.images": 2,  # Bloquear imágenes
#             "profile.default_content_setting_values.css": 2,  # Bloquear CSS
#         }
#         options.add_experimental_option("prefs", prefs)

#         driver = webdriver.Chrome(
#             service=ChromeService(ChromeDriverManager().install()),
#             seleniumwire_options=proxy_options,
#             chrome_options=options,
#         )

#         driver.get("https://www.youmainlyyou.com/")

#         random_time = random.randint(5, 40)
#         print("time", random_time)
#         time.sleep(random_time)
#         arts = driver.find_elements(by="css selector", value="a:has(img):has(h3)")
#         cats = [
#             "Wellbeing & Health",
#             "Allure & Grooming",
#             "Taste",
#             "Style",
#             "Bon Voyage",
#             "Awareness",
#             "Gadgets",
#             "Furnishing",
#         ]
#         cat = driver.find_element(by="link text", value=random.choice(cats))
#         print("cat", cat.text)
#         cat.click()
#         random_time = random.randint(5, 20)
#         print("time", random_time)
#         time.sleep(random_time)
#         arts = driver.find_elements(by="css selector", value="a:has(img):has(h3)")
#         art = random.choice(arts)
#         art.click()
#         random_time = random.randint(5, 40)
#         print("time", random_time)
#         time.sleep(random_time)
#         driver.quit()

#         return "Ok"

#     except Exception as e:
#         print(e)
#         return "Error"
