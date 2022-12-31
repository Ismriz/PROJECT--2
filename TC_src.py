import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

username = driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("admin123")
login = driver.find_element(By.XPATH,"//button[@type='submit']")
login.click()
search = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search.click()
