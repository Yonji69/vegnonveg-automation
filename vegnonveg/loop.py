from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = False
options.set_preference("dom.webnotifications.enabled", False)

service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://www.vegnonveg.com/")
    
    for _ in range(3):
        search_bar = driver.find_element(By.ID, "q")
        search_bar.send_keys("AIR JORDAN 3 RETRO TEX 'DARK DRIFTWOOD/SAIL-HEMP-VELVET BROWN'")
        search_bar.send_keys(Keys.RETURN)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'air-jordan-3-retro-tex-dark-driftwoodsail-hemp-velvet-brown-brown')]"))
        )
        
        product_link = driver.find_element(By.XPATH, "//a[contains(@href, 'air-jordan-3-retro-tex-dark-driftwoodsail-hemp-velvet-brown-brown')]")
        product_url = product_link.get_attribute("href")
        
        driver.execute_script(f"window.open('{product_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.select"))
        )
        
        size_dropdown = driver.find_element(By.CSS_SELECTOR, "div.select")
        size_dropdown.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu variant-dropdown']"))
        )
        
        size_option = driver.find_element(By.XPATH, "//li[@data-size='4']")
        size_option.click()
        
        time.sleep(10)  # Wait for 10 seconds before adding the product
        
        add_to_bag_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.w-100.add_to_bag")
        add_to_bag_button.click()
        
        time.sleep(5)  # Wait for 5 seconds after clicking "Add to Bag"
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
        driver.get("https://www.vegnonveg.com/")
        
        time.sleep(2)  # Wait before starting the next iteration

    driver.get("https://www.vegnonveg.com/cart")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.text-center .checkout"))
    )
    
    print("Navigated to the cart page with products.")

    time.sleep(20)

finally:
    driver.quit()
