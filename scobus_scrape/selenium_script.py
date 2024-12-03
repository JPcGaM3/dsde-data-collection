from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import os
from data import _id, _pass

def scopus_search_and_navigate():

    driver = webdriver.Chrome()
    
    try:
        driver.get('https://www.scopus.com/search/form.uri?display=basic#basic')
        
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin_link_move"))
        )
        signin_button.click()
        
        accept_cookie = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_cookie.click()
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bdd-email"))
        )
        #enter your email
        #eg. email_input.send_keys("user@gmail.com")
        email_input.send_keys(_id)
        
        continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
        continue_button.click()
        
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bdd-password"))
        )
        #enter your password
        #eg. password_input.send_keys("123456")
        password_input.send_keys(_pass)
        
        login_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
        login_button.click()
        
        time.sleep(5)
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "styleguide-input-module___SqPU"))
        )

        search_box.send_keys("Ai")

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search_button.click()

        time.sleep(5)
        

        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        export_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Export']]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", export_button)
        driver.execute_script("arguments[0].click();", export_button)
        csv_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='CSV']]"))
        )
        csv_button.click()
        select_all_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Select all information']]"))
        )
        select_all_button.click()
        radio_label = driver.find_element(By.XPATH, "//label[.//span[text()='Documents']]")
        radio_label.click()
        input_from = driver.find_element(By.XPATH, "//input[@placeholder = 'From']")
        input_from.send_keys(1)
        input_to = driver.find_element(By.XPATH, "//input[@placeholder = 'To']")
        input_to.send_keys(2000)
        export_button2 = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[.//div[text()='Export']]]"))
        )
        export_button2.click()
        time.sleep(5) 

        WebDriverWait(driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, "//span[.//div[.//div[text()='Your CSV file was successfully exported.']]]"))
        )
        time.sleep(2)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

scopus_search_and_navigate()

#! update now!
# Go inside for each research page