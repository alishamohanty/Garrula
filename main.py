from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#acc login info
uname = 'phantomfive11@gmail.com'
upass = '<password-goes-here>'       #ONLY ENTER PASSWORD WHILE TESTING THIS , DO NOT COMMIT BY MISTAKE EVEN WITH THE ORIGINAL PASSWORD IN CODE

#launch firefox
driver = webdriver.Firefox()
driver.get("https://www.twitter.com")
wait = WebDriverWait(driver, 10)

#enter email
user = wait.until(EC.visibility_of_element_located((By.NAME, "session[username_or_email]")))
user.clear()
user.send_keys(uname)

#enter password
passw = wait.until(EC.visibility_of_element_located((By.NAME, "session[password]")))
passw.clear()
passw.send_keys(upass)

#press login button
el=driver.find_element_by_class_name('EdgeButton')
el.click()


#write in text-box
el = driver.find_element_by_id('tweet-box-home-timeline')
el.send_keys("Jai Matadi!")  #Todo: Pass string from APIs here
time.sleep(5)
el = driver.find_element_by_class_name('tweet-action')
el.click()
print("Success")

