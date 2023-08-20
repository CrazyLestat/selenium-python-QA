#TEST CASE
# Open Web Browser
# Open URL https://opensource-demo.orangehrmlive.com
# Enter username (Admin)
# Enter Password (admin123)
# Capture title of the homepage (actual title)
# Verifit title of the page OrangeHRM (expected)
# Close browser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,"username"))
        )
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

    act_title = driver.find_element(By.TAG_NAME,'h6')
    exp_title = "Dashboard"

    if act_title==exp_title:
        print("Login Test Passes")
    else:
        print("Login Test Failed")

    sleep(30)

finally:

# driver.find_element(By.CLASS_NAME,"oxd-input--active").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

# act_title = driver.title
# exp_title = "OrangeHRM"

# if act_title==exp_title:
#     print("Login Test Passes")
# else:
#     print("Login Test Failed")
    driver.close()
    