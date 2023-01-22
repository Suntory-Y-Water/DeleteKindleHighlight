import time
import pyautogui as pgui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Move constants to the top of the file
USER_DIR = "C:\\ChromeData\\Google\\Chrome\\User Data"
PROFILE_DIR = "Profile 1"
URL = "https://read.amazon.co.jp/notebook"

HIGHLIGHT_DELETE_BUTTON = "/html/body/div[3]/div/div[1]/div/ul/li[3]/span/a"
MEMO_DELETE_BUTTON = "/html/body/div[3]/div/div[1]/div/ul/li[4]/span/a"
HIGHLIGHT_POPUP = "/html/body/div[4]/div/div/div[2]/span[2]/span/span/input"
MEMO_POPUP = "/html/body/div[6]/div/div/div[2]/span[2]/span/span/input"

# Use a more descriptive variable name
page_count = 1

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + USER_DIR)
options.add_argument("profile-directory=" + PROFILE_DIR)
service = ChromeService(executable_path="C:\\Users\\NOkud\\bin\\chromedriver\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

# Use a more descriptive variable name
IMPLICIT_WAIT_TIME = 5

# Set implicit wait time for the specified driver
driver.implicitly_wait(IMPLICIT_WAIT_TIME)

# Navigate to the specified URL
driver.get(URL)

# Handle the alert for selecting the book to delete highlights from
pgui.alert()

while True:

    # Use a more descriptive variable name
    OPTION_BUTTON = "/html/body/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div[3]/div[{}]/div/div[1]/div[2]/span/a".format(page_count)

    try:
        # Click on the option button
        element = driver.find_element(By.XPATH, OPTION_BUTTON)
        driver.execute_script("arguments[0].click();", element)

        # Delete highlight
        if driver.find_element(By.XPATH, HIGHLIGHT_DELETE_BUTTON):
            driver.find_element(By.XPATH, HIGHLIGHT_DELETE_BUTTON).click()
            time.sleep(1)

            # Confirm deletion in the popup
            driver.find_element(By.XPATH, HIGHLIGHT_POPUP).click()
        else:
            driver.find_element(By.XPATH, MEMO_DELETE_BUTTON).click()
            time.sleep(1)
            # Confirm deletion in the popup
            driver.find_element(By.XPATH, MEMO_POPUP).click()
    except:
        print("Error occurred")
    
    page_count += 1
    time.sleep(1)

    if page_count == 10:
        print("Exiting")
        driver.quit()
        break