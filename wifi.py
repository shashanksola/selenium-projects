from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://hfw.vitap.ac.in:8090/httpclient.html")

time.sleep(2)
if (driver.title == "Connect to Wi-Fi"):
    try:

        # primaryButton = driver.find_element(By.ID, "primary-button")
        # primaryButton.send_keys(Keys.RETURN)
        driver.switch_to.window(driver.window_handles[1])
    except:
        print("Connect button doesn't exist")

try:
    advanced = driver.find_element(By.ID, "details-button")
    advanced.send_keys(Keys.RETURN)
except:
    print(driver.title)
    print("No Warning Page Detected")

try:
    link = driver.find_element(By.ID, "proceed-link")
    link.send_keys(Keys.RETURN)
except:
    print("Proceed Link Not Detected")


data = [['21BCE9XXX', 'UWDSUe3'],
        ['21BCE9XXX', 'UWDSUe3'],
        ['21BCE9XXX', 'UWDSUe3'],
        ['21BCE9XXX', 'UWDSUe3'],
        ['21BCE9XXX', 'UWDSUe3']]

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

for dat in data[:5]:
    try:
        u = dat[0]
        p = dat[1]
        username.clear()
        password.clear()

        username.send_keys(u)
        password.send_keys(p)

        loginbutton = driver.find_element(By.ID, "loginbutton")
        loginbutton.click()

        statusmessage = WebDriverWait(driver, 0.5).until(
            EC.presence_of_all_elements_located((By.ID, "statusmessage"))
        )
        print(statusmessage.text)
        if (statusmessage.text == ""):
            print("Sign in successfull")
            break
    except:
        print(u + " did not work")

time.sleep(10)
driver.quit()
