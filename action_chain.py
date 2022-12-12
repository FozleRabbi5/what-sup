from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "D:\Drive I\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element(By.ID,"bigCookie")

print(cookie.text)

# action = ActionChains(driver)
# action.click()



