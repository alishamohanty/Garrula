from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import datetime
import wikiquotes
from chuck import ChuckNorris
import random

options = Options()
options.set_headless(headless=True)
st=random.randint(0,1)
def post(st):
    n=random.randint(0,2)
    if st is 0:
        t=tags1(n)
        rt=str((wikiquotes.quote_of_the_day("english")[0]))
        #print(rt+t)
        return (rt+t)

    else:
        t=tags2(n)
        cn=ChuckNorris()
        data=str(cn.random())
        while len(data)>270:
            data=cn.random()
        #print(data+t)
        return (data+t)
def tags2(n):
    if n is 0:
        return ("#jokeoftheday")
    elif n is 1:
        return ("#funmood")
    else:
        return ("#instaquote")
def tags1(n):
    if n is 0:
        return ("#wisdom")
    elif n is 1:
        return("#positivity")
    else:
        return ("#lifelesson")

data1=post(st)
print(data1)

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
    upass = '<enter-passwd-here>'           #pseudopassword in place , replace with correct password for testing

    #launch firefox
    driver = webdriver.Firefox(firefox_options=options)
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
    el.send_keys(data1)  #Todo: Pass string from APIs here
    time.sleep(5)
    el = driver.find_element_by_class_name('tweet-action')
    el.click()
    file=open("output.txt","w")
    file.write(str(datetime.date.today()))
    file.close()
    print("Success")
    driver.close()


