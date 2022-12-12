from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


path = "D:\Drive I\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.techwithtim.net/")


# search = driver.find_element("name","s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

main = driver.find_element("id","main")
print(main.text)

# print(driver.page_source)
# time.sleep(10)

# print(driver.title)
