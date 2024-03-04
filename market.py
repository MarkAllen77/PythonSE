import time
from datetime import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# dd/mm/YY H:M:S
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
print("[Start Execution]", dt_string)

sourceFile = "./source.txt"
outputFile = "./output.txt"
readSourceFile = open(sourceFile, "r")
writeOutputFile = open(outputFile, "a")

writeOutputFile.write("\r----- " + dt_string + " -----\r")

cService = webdriver.ChromeService(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=cService)

for perLine in readSourceFile:
    try:
        URL = "https://ph.investing.com/equities/" + perLine
        driver.get(URL)

        analystsTab = driver.find_element(By.XPATH, "//div[text()='Analysts']")
        actions = ActionChains(driver)
        actions.move_to_element(analystsTab).perform()
        analystsTab.click()

        analystsTarget = driver.find_elements(By.XPATH, '//div[text()="Analysts"]/../../following-sibling::div[1]//div[2]')
        value = analystsTarget[2].text

        if len(perLine) < 12:
            tabCharacter = "\t\t\t"
        else:
            tabCharacter = "\t\t"

        writeOutputFile.write("Analysts  : " + perLine.strip('\n') + tabCharacter + value + "\r")

    except NoSuchElementException:
        technicalTab = driver.find_element(By.XPATH, "//div[text()='Technical']")
        actions = ActionChains(driver)
        actions.move_to_element(technicalTab).perform()

        analystsTarget = driver.find_elements(By.XPATH, '//div[text()="Technical"]/../following-sibling::div[1]//div[2]')
        value = analystsTarget[2].text

        if len(perLine) < 12:
            tabCharacter = "\t\t\t"
        else:
            tabCharacter = "\t\t"

        writeOutputFile.write("Technical : " + perLine.strip('\n') + tabCharacter + value + "\r")

time.sleep(3)
driver.close()
driver.quit()

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
print("[End Execution  ]", dt_string)
