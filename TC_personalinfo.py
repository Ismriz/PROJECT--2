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
emp_list = driver.find_element(By.XPATH,"//a[text()='Employee List']")
emp_list.click()
add_emp = driver.find_element(By.XPATH,"//a[text()='Add Employee']")
add_emp.click()
fname = driver.find_element(By.XPATH,"//input[@name='firstName']")
fname.send_keys("asha")
lname = driver.find_element(By.XPATH, "//input[@name='lastName']")
lname.send_keys("banu")
save = driver.find_element(By.XPATH,"//button[@type='submit']")
save.click()
def Update_personal_info():


    emp_id = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
    emp_id.send_keys('0289')
    driver_license_no = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]")
    driver_license_no.send_keys('00661537')
    license_expiry_date = driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]")
    license_expiry_date.send_keys('2022-08-03')
    nationality = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
    nationality.send_keys("Indian")
    marital_status = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    marital_status.send_keys("Married")
    gender = driver.find_element(By.XPATH,"//label[text()='Gender']")
    gender.send_keys("Female")

Update_personal_info()




