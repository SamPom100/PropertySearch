from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#SETUP
chromedriver = "/chromedriver"
option = webdriver.ChromeOptions() #option.add_argument("--headless")
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
s = Service(chromedriver)
browser = webdriver.Chrome(service=s, options=option) #self.browser = webdriver.Safari()

class By:
    """Set of supported locator strategies."""
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

browser.get("https://mytax.illinois.gov/?link=TaxLienReg")
time.sleep(2)


def lienSearch(houseNumber, streetName, city, zipCode):
    #INDIVIDUAL SEARCH
    individualButton = browser.find_element(By.ID, "caption_Dc-6")
    individualButton.click()

    #INPUT DATA
    time.sleep(2)
    browser.find_element(By.NAME, "Dc-v").send_keys(houseNumber + " " + streetName)
    browser.find_element(By.NAME, "Dc-w").send_keys(city)
    browser.find_element(By.NAME, "Dc-y").send_keys(zipCode)

    ddelement = browser.find_element(By.XPATH, "//input[@name='Dc-z']")
    ddelement.send_keys("Cook")
    ddelement.send_keys(Keys.ENTER)

    time.sleep(0.5)

    ddelement = browser.find_element(By.XPATH, "//input[@name='Dc-x']")
    ddelement.send_keys("Illinois")
    ddelement.send_keys(Keys.ENTER)

    #ENTER BUTTON
    time.sleep(1)
    enterButton = browser.find_element(By.ID, "Dc-j")
    enterButton.click()

    #LIENS FOUND?
    time.sleep(1)
    try:
        result = browser.find_element(By.ID, "caption2_Dc-w1")
        print(result.text)
        print("No lien found!")
    except:
        print("Lien found!")
