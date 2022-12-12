from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = "D:\DriveI\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.techwithtim.net/")



link = driver.find_element(By.LINK_TEXT,"Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menu-item-523"))
    )
    element1.click()
    driver.back()
    driver.back()
    driver.back()
finally:
    driver.quit()
