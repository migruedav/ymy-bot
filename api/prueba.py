# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# def prueba():

#     options = Options()
#     options.add_argument("--headless")  # Run Chrome in headless mode
#     options.add_argument("--no-sandbox")  # Bypass Chrome's sandboxing
#     options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
#     options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
#     options.add_argument("--remote-debugging-port=9222")  # Optional for debugging

#     # Ensure the path to ChromeDriver matches your environment
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()), options=options
#     )

#     print("ya pasó el driver")

#     driver.get("https://www.youmainlyyou.com")
#     print(driver.title)

#     driver.quit()

#     return {"ada": "TPEC"}
