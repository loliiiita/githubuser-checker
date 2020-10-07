import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
chromePath = input("enter chromedriver if you're on linux, or chromedriver.exe if you're on windows: ")
driver = webdriver.Chrome(chromePath)
driver.get('https://github.com/join')

## setup to be allow our checks
username = driver.find_element_by_xpath('//*[@id="user_login"]')
username.send_keys('fjdslfjsldfjdslfkjsdlfkjdslf')
print("test is good!")
time.sleep(1)
soup = BeautifulSoup(driver.page_source, features="lxml")
items = soup.find_all('dd')
check_num = items[1]["id"].split('-')[2]
## setup complete
print("make sure you have put your usernames in usernames.txt, separated with new lines!")
to_check = open("usernames.txt","r").read().split('\n')
timeToSleep = input("time to wait inbetween attempts? (recommended minimum of 1) ")
userTime = int(timeToSleep)
for i in to_check:
    username.send_keys(i)
    time.sleep(userTime)
    check = driver.find_element_by_xpath(f'//*[@id="input-check-{check_num}"]')
    available = check.get_attribute("class")
    if available.lower() == "success":
        with open("can_take.txt", "a+") as f:
            f.write(i+'\n')
        print(f'{i} is not taken, adding to file')
    else:
        print(f'{i} is taken, moving on')
    username.clear()
#/signup_check/username?suggest_usernames=true
#//*[@id="user_login"]
#//*[@id="input-check-3252"]
