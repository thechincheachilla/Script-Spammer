from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

import time
import random

def main():
    CONTACT = "https://www.facebook.com/messages/t/ID_GOES_HERE" # Change the numbers to the ID
    SCRIPT =  "script.txt"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options) 

    driver.get("https://facebook.com")
    # Credentials in file, formatted: username,password
    credentials = open("credentials.txt", "r").readline().split(",") 
    user = credentials[0]
    password = credentials[1]
    for char in user:
        driver.find_element_by_id("email").send_keys(char)
        time.sleep(random.uniform(0.02, 0.2))
    time.sleep(2)
    for char in password:
        driver.find_element_by_id("pass").send_keys(char)
        time.sleep(random.uniform(0.02, 0.2))
    time.sleep(2)
    driver.find_element_by_id("u_0_b").click()
    time.sleep(2)
    driver.get(CONTACT)
    time.sleep(5)

    with open(SCRIPT) as file:
        lines = file.read().splitlines()
    for line in lines:
        if line != '':
            words = line.split(' ')
            for word in words:
                for char in word:
                    driver.switch_to_active_element().send_keys(char)
                    time.sleep(random.uniform(0.01, 0.2))
                driver.switch_to_active_element().send_keys(Keys.RETURN);
                time.sleep(0.25)

if __name__ == "__main__":
    main()
