import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
pim = driver.find_element(By.XPATH,"//span[text()='PIM']")
pim.click()
time.sleep(5)
emp_list = driver.find_element(By.XPATH,"//a[text()='Employee List']")
emp_list.click()
time.sleep(5)
add_btn = driver.find_element(By.XPATH,"(//button[@type='button'])[3]")
add_btn.click()
time.sleep(5)
fname = driver.find_element(By.XPATH,"//input[@name='firstName']")
fname.send_keys("asha")
lname = driver.find_element(By.XPATH, "//input[@name='lastName']")
lname.send_keys("banu")
save = driver.find_element(By.XPATH,"//button[@type='submit']")
save.click()
time.sleep(5)
add_emp = driver.find_element(By.XPATH,"//a[text()='Add Employee']")
add_emp.click()
time.sleep(5)








