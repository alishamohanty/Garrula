from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

file=open("output.txt","r")
f=file.read()
print("last post was on " +f)
print("today is "+str(datetime.date.today()))
file.close()

if f == str(datetime.date.today()):
    print("Already Posted For The Day")
else :
    #acc login info
    uname = 'phantomfive11@gmail.com'
    upass = '<enter-passwd-here>'           #ONLY ENTER PASSWORD WHILE TESTING THIS , DO NOT COMMIT BY MISTAKE EVEN WITH THE ORIGINAL PASSWORD IN CODE

    #launch firefox
    driver = webdriver.Firefox()
    driver.get("https://www.twitter.com/login")
    wait = WebDriverWait(driver, 10)

    #enter email
    time.sleep(5)
    user = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")))
    user.clear()
    user.send_keys(uname)

    #enter password
    time.sleep(5)
    passw = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")))
    passw.clear()
    passw.send_keys(upass)

    #press login button
    time.sleep(5)
    el=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
    el.click()


    #write in text-box
    time.sleep(5)
    el = driver.find_element_by_id('tweet-box-home-timeline')
    el.send_keys("File write test")  #Todo: Pass string from APIs here
    time.sleep(5)
    el = driver.find_element_by_class_name('tweet-action')
    el.click()
    file=open("output.txt","w")
    file.write(str(datetime.date.today()))
    file.close()
    print("Success")


