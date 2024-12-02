# from email import message
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# driver = webdriver.Chrome()

# driver.get('https://www.scopus.com/search/form.uri?display=basic#basic')
# time.sleep(2)

# signin_button = driver.find_element(By.ID, "signin_link_move")
# signin_button.click()
# time.sleep(3)

# accept_cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
# accept_cookie.click()
# time.sleep(1)

# email_input= driver.find_element(By.ID, "bdd-email")
# email_input.send_keys("6633038121@student.chula.ac.th")
# continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
# continue_button.click()
# time.sleep(5)

# password_input = driver.find_element(By.ID, "bdd-password")
# password_input.send_keys("kenpav-babwE3-nosrys")
# login_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
# login_button.click()
# time.sleep(5)

# search_box = driver.find_element(By.CLASS_NAME, "styleguide-input-module___SqPU")
# search_box.send_keys("Ai")
# time.sleep(2)
# search_box.send_keys(Keys.RETURN)
# time.sleep(5)

# doc_buttons = driver.find_elements(By.CLASS_NAME, "Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__ZS4lL Button-module__hK_LA Button-module__qDdAl Button-module__rTQlw")

# for i in range(0,9):
#     doc_buttons[i].click()
#     time.sleep(5)
#     driver.back()
#     time.sleep(5)
#     doc_buttons = driver.find_elements(By.CLASS_NAME, "Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__ZS4lL Button-module__hK_LA Button-module__qDdAl Button-module__rTQlw")

# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

def scopus_search_and_navigate():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    
    try:
        # Navigate to Scopus search page
        driver.get('https://www.scopus.com/search/form.uri?display=basic#basic')
        
        # Wait and click sign-in button
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin_link_move"))
        )
        signin_button.click()
        
        # Accept cookies
        accept_cookie = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_cookie.click()
        
        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bdd-email"))
        )
        email_input.send_keys("6633038121@student.chula.ac.th")
        
        # Click continue
        continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
        continue_button.click()
        
        # Enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bdd-password"))
        )
        password_input.send_keys("kenpav-babwE3-nosrys")
        
        # Click login
        login_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
        login_button.click()
        
        time.sleep(5)
        
        # Wait for search input to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "styleguide-input-module___SqPU"))
        )

        # Enter search term
        search_box.send_keys("Ai")

        # Find and click the search button explicitly
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search_button.click()

        time.sleep(5)
        
        # Wait for search results
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "TableItems-module__UF1E0"))
        )
        
        # Find all table rows
        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "TableItems-module__UF1E0"))
        )
        
        # Iterate through first 9 rows
        for i in range(min(9, len(table_rows))):
            try:
                # Refresh the rows to avoid stale element exception
                table_rows = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "TableItems-module__UF1E0"))
                )
                
                # Find the link within the current row
                link = table_rows[i].find_element(
                    By.CLASS_NAME, 
                    "Button-module__f8gtt.Button-module__rphhF.Button-module__VBKvn.Button-module__ZS4lL.Button-module__hK_LA.Button-module__qDdAl.Button-module__rTQlw"
                )
                
                # Wait for link to be clickable and click
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(link)
                ).click()
                
                # Wait for page to load
                time.sleep(5)
                
                # Navigate back
                driver.back()
                
                # Wait after navigating back
                time.sleep(5)
            
            except Exception as e:
                print(f"Error processing row {i}: {e}")
                break
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Always close the browser
        driver.quit()

# Run the function
scopus_search_and_navigate()



#! update now!
#  cannot click into foreach research