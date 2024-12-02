from email import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://www.scopus.com/search/form.uri?display=basic#basic')
time.sleep(2)

signin_button = driver.find_element(By.ID, "signin_link_move")
signin_button.click()
time.sleep(3)

accept_cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_cookie.click()
time.sleep(1)

email_input= driver.find_element(By.ID, "bdd-email")
email_input.send_keys("6633038121@student.chula.ac.th")
continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
continue_button.click()
time.sleep(5)

password_input = driver.find_element(By.ID, "bdd-password")
password_input.send_keys("kenpav-babwE3-nosrys")
login_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
login_button.click()
time.sleep(5)

search_box = driver.find_element(By.CLASS_NAME, "styleguide-input-module___SqPU")
search_box.send_keys("Ai")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(10)

driver.quit()