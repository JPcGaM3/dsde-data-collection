from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import os

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
        email_input.send_keys("6633038121@student.chula.ac.th")
        
        continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
        continue_button.click()
        
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bdd-password"))
        )
        password_input.send_keys("kenpav-babwE3-nosrys")
        
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
        
        # Correct all research on that page
        links_list = []
        link_elements = driver.find_elements(
            By.CLASS_NAME, 
            "Button-module__f8gtt.Button-module__rphhF.Button-module__VBKvn.Button-module__ZS4lL.Button-module__hK_LA.Button-module__qDdAl.Button-module__rTQlw"
        )
        
        for link_element in link_elements:
            link = link_element.get_attribute("href")
            if link:  
               links_list.append(link)

        for link in links_list :
            driver.get(link)
            time.sleep(5)
            driver.back()
            time.sleep(5)

        time.sleep(10)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

scopus_search_and_navigate()

#! update now!
# Go inside for each research page