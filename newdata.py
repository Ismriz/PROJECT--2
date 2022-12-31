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
pim = driver.find_element(By.XPATH,"//span[text()='PIM']")
pim.click()
time.sleep(5)
add = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
add.click()
create_log = driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
create_log.click()
time.sleep(5)
usr = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
usr.send_keys("Ismail")
time.sleep(5)
status = driver.find_element(By.XPATH,"//label[text()='Status']")
status.click()
pswd = driver.find_element(By.XPATH,"(//input[@type='password'])[1]")
pswd.send_keys("Masha53@")
cnfrm_pswd = driver.find_element(By.XPATH,"(//input[@type='password'])[2]")
cnfrm_pswd.send_keys("Masha53@")
time.sleep(5)
button = driver.find_element(By.XPATH,"//button[@type='submit']")
button.click()
time.sleep(10)
driver.close()






