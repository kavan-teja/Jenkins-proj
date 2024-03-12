from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize the browser
driver = webdriver.Chrome(r"C:\Users\tejak\Downloads\chromedriver.exe")

# Load the HTML file
driver.get(r"C:\Users\tejak\OneDrive\Documents\6th sem\file\file1.html")
time.sleep(3)
# Define explicit wait
wait = WebDriverWait(driver, 10)

# Interaction with elements
name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
name_input.send_keys("kavan")
time.sleep(2)
address_textarea = driver.find_element(By.ID, "address")
address_textarea.send_keys("Vijayanagar,Bangalore.")
time.sleep(2)
subscribe_checkbox = driver.find_element(By.ID, "subscribe")
subscribe_checkbox.click()
time.sleep(2)
gender_radio = driver.find_element(By.ID, "male")
gender_radio.click()
time.sleep(2)
country_dropdown = driver.find_element(By.ID, "country")
country_dropdown.send_keys("India")
time.sleep(2)
# Submit the form
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()
time.sleep(2)
# Wait for the alert message
wait.until(EC.alert_is_present())

# Print a confirmation message
print("Form submitted successfully!")
time.sleep(10)
# Close the browser
driver.quit()
