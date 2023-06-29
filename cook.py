from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#SETUP
chromedriver = "/chromedriver"
option = webdriver.ChromeOptions() #option.add_argument("--headless")
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
s = Service(chromedriver)
browser = webdriver.Chrome(service=s, options=option) #self.browser = webdriver.Safari()

class By:
    ID = "id"
    CLASS_NAME = "class name"
    NAME = "name"
    TAG_NAME = "tag name"

def propertySearch(houseNumber, streetName, city, zipCode, unitNum):

    browser.get("https://www.cookcountytreasurer.com/setsearchparameters.aspx")

    #OPEN WEBPAGE
    button = browser.find_element(By.ID, "ContentPlaceHolder1_ASPxTabControl1_T1T")
    time.sleep(1)
    button.click()

    browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtHouseNumber").send_keys(houseNumber)
    browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtStreetName").send_keys(streetName)
    browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtCity").send_keys(city)
    browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtZipCode").send_keys(zipCode)

    if unitNum != "":
        browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtUnit").send_keys(unitNum)

    #CONTINUE
    time.sleep(2)
    continueButton = browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_cmdContinue")
    continueButton.click()

    #VIEW PROPERTY TAX
    time.sleep(2)
    viewPropertyTaxButton = browser.find_element(By.ID, "ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_ListView1_lnkShowAddressSearchResults_0")
    viewPropertyTaxButton.click()

    #GET TOTAL BILLED
    time.sleep(2)
    billedSpan = browser.find_element(By.ID, "ContentPlaceHolder1_OverviewDataResultsSummary1_PaymentsOverviewSummaryControl1_lblPriorTotalAmountBilled")
    print("TOTAL TAX BILLED IN 2021: ", billedSpan.text, "\n\n")

    #GET EXEMPTIONS
    exemptionsSpan = browser.find_element(By.ID, "ContentPlaceHolder1_OverviewDataResultsSummary1_ExemptionHistoryOverviewSummaryControl1_panSearchResults")
    print("EXEMPTIONS: ", exemptionsSpan.text)