import time
from datetime import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

cService = webdriver.ChromeService(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=cService)


def HandleInputandRadio():
    # dd/mm/YY H:M:S
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
    print("[Start Execution]", dt_string)

    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)

    # ----- How to handle Inputbox & RadioButtons -----
    firstnameinput = driver.find_element(By.XPATH, "//input[@id='firstName']")
    lastnameinput = driver.find_element(By.XPATH, "//input[@id='lastName']")

    print(firstnameinput.is_displayed())
    print(firstnameinput.is_enabled())
    print("Current value: ", firstnameinput.get_attribute("value"))

    firstnameinput.send_keys("John")
    lastnameinput.send_keys("Doe")

    print("Updated value: ", firstnameinput.get_attribute("value"))

    gendermalelabel = driver.find_element(By.XPATH, "//label[text() = 'Male']")
    genderfemalelabel = driver.find_element(By.XPATH, "//label[text() = 'Female']")
    gendermaleradiobutton = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
    genderfemaleradiobutton = driver.find_element(By.XPATH, "//input[@id='gender-radio-2']")

    print("Radiobutton", gendermaleradiobutton.is_selected())
    gendermalelabel.click()
    print(gendermaleradiobutton.is_selected())
    print(genderfemaleradiobutton.is_selected())
    genderfemalelabel.click()
    print(genderfemaleradiobutton.is_selected())

    # ----- How to handle Checkboxes -----
    hobbiessportslabel = driver.find_element(By.XPATH, "//label[text() = 'Sports']")
    hobbiessportscheckbox = driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-1']")
    hobbiesreadinglabel = driver.find_element(By.XPATH, "//label[text() = 'Reading']")
    hobbiesreadingcheckbox = driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-2']")

    print("Checkbox", hobbiessportscheckbox.is_selected())
    hobbiessportslabel.click()
    print(hobbiessportscheckbox.is_selected())
    print(hobbiesreadingcheckbox.is_selected())
    hobbiesreadinglabel.click()
    print(hobbiesreadingcheckbox.is_selected())

    time.sleep(2)
    hobbiescheckboxes = [
        "//label[text() = 'Sports']",
        "//label[text() = 'Reading']",
        "//label[text() = 'Music']",
    ]

    for box in hobbiescheckboxes:
        driver.find_element(By.XPATH, box).click()


def HandleDropdown():
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)


def ExecutionEnd():
    time.sleep(3)
    driver.close()
    driver.quit()

    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
    print("[End Execution  ]", dt_string)


def StartTest():
    HandleInputandRadio()
    HandleDropdown()
    ExecutionEnd()


StartTest()
