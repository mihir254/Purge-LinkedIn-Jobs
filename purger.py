import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

username = os.environ.get("LINKEDIN_USERNAME")
password = os.environ.get("LINKEDIN_PASSWORD")

if not username or not password:
    sys.exit("LinkedIn credentials are not set in the environment variables.")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
except Exception as e:
    sys.exit(f"Error opening Chrome: {str(e)}")

try:
    driver.get("https://www.linkedin.com")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "session_key")))
    driver.find_element(By.ID, "session_key").send_keys(username)
    driver.find_element(By.ID, "session_password").send_keys(password + Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "global-nav-typeahead")))
except Exception as e:
    driver.quit()
    sys.exit(f"Login failed: {str(e)}")

try:
    driver.get("https://www.linkedin.com/my-items/saved-jobs/?cardType=ARCHIVED")
    time.sleep(3)
except Exception as e:
    driver.quit()
    sys.exit(f"Failed to navigate to archived jobs: {str(e)}")

while True:
    try:
        options_buttons = driver.find_elements(By.CSS_SELECTOR, '.artdeco-dropdown__trigger.artdeco-button--circle')
        if options_buttons:
            options_buttons[0].click()
            time.sleep(1)
            remove_job_buttons = driver.find_elements(By.CSS_SELECTOR, '.artdeco-dropdown__item--is-dropdown .image-text-lockup__text')
            for button in remove_job_buttons:
                if button.text.strip() == "Remove job":
                    button.click()
                    break
            time.sleep(1)
    except Exception as e:
        print("No more jobs to delete or an error occurred:", str(e))
        break

driver.quit()