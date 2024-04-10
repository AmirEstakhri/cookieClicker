from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())


cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Navigate to the website
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
datause = driver.find_element(By.CLASS_NAME, 'fc-button-label')
datause.click()

# Wait for the language selection element to be present
spreche1 = "//*[contains(text(), 'English')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, spreche1)))

# Click on the language selection element
spreche = driver.find_element(By.XPATH, spreche1)
spreche.click()
time.sleep(15)

# Find and click on the cookie button 
cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break


                