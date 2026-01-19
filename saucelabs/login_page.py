from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    driver.implicitly_wait(10)
    driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.XPATH,"//a[@data-test='shopping-cart-link']").click()
    driver.find_element(By.CSS_SELECTOR,"#checkout").click()
    driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("rama")
    driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("rama")
    driver.find_element(By.NAME,"postalCode").send_keys("506132")
    driver.find_element(By.NAME,"continue").click()
    driver.find_element(By.CSS_SELECTOR,"#finish").click()
    success = driver.find_element(By.TAG_NAME,"h2")
    assert success.text == "Thank you for your order!", "not submitted successfully"
    time.sleep(10)
except:
    print("something went wrong and came to except block")