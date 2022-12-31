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

def Drop_down():

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("Admin")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("admin123")
    login = driver.find_element(By.XPATH, "//button[@type='submit']")
    login.click()
    search = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    search.click()
    admin = driver.find_element(By.XPATH,"//span[text()='Admin']")
    admin.click()
    usr_mgmt = driver.find_element(By.XPATH,"//span[text()='User Management ']")
    usr_mgmt.click()
    usr = driver.find_element(By.XPATH,"//a[text()='Users']")
    usr.click()
    sys_usr = driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-up-fill']")
    sys_usr.click()
    driver.find_element(By.XPATH,"//label[text()='User Role']")
    element = driver.find_element(By.XPATH,"//label[text()='User Role']")
    drop = Select(element)
    drop.select_by_visible_text("Admin")
    drop.select_by_visible_text("ESS")
    element1 = driver.find_element(By.XPATH,"//label[text()='Status']")
    drop = Select(element1)
    drop.select_by_visible_text("Enabled")
    drop.select_by_visible_text("Disabled")

Drop_down()