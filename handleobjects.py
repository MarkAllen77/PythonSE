import time
from datetime import datetime

from selenium import webdriver
# from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

    countrydropdown = driver.find_element(By.XPATH, "//select[@id='country']/option[text()='Canada']")
    countrydropdown.click()

    countrydropdownobject = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
    time.sleep(1)
    countrydropdownobject.select_by_index(3)    # germany
    time.sleep(1)
    countrydropdownobject.select_by_visible_text("India")
    time.sleep(1)
    countrydropdownobject.select_by_value('usa')

    print("Numer of options: ", len(countrydropdownobject.options))
    print("Current value: ", countrydropdownobject.first_selected_option.text)

    countrydropdownoptions = driver.find_elements(By.XPATH, "//select[@id='country']/option")
    time.sleep(1)
    countrydropdownoptions[5].click()   # australia


def HandleMultiDropdown():
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)

    colorslabel = driver.find_element(By.XPATH, "//label[contains(.,'Colors')]")
    driver.execute_script("arguments[0].scrollIntoView();", colorslabel)

    colorsdropdown = driver.find_element(By.XPATH, "//select[@id='colors']/option[text()='Red']")
    colorsdropdown.click()

    colorsdropdownobject = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
    time.sleep(1)
    colorsdropdownobject.select_by_index(1)    # blue
    time.sleep(1)
    colorsdropdownobject.select_by_visible_text("Green")
    time.sleep(1)
    colorsdropdownobject.select_by_value('white')

    print("Numer of options: ", len(colorsdropdownobject.options))

    for colors in colorsdropdownobject.all_selected_options:
        print("Value: ", colors.text)


def HandleBootstrapDropdown():
    url = "https://www.jquery-az.com/boots/demo.php?ex=63.0_2"
    driver.get(url)

    outputbutton = driver.find_element(By.XPATH, "//button")
    outputoption = driver.find_elements(By.XPATH, "//ul//li//label//input")

    print("Numer of options: ", len(outputoption))
    outputbutton.click()

    for item in outputoption:
        value = item.get_attribute("value")
        if value == "Angular" or value == "Java":
            print(item.get_attribute("value"))
            item.click()
            print(item.is_selected())

        if value == "HTML" or value == "CSS":
            print(item.get_attribute("value"))
            item.click()
            print(item.is_selected())


def HandleAutoSuggestion():
    url = "https://www.redbus.in/"
    driver.get(url)

    frominput = driver.find_element(By.XPATH, "//input[@id='src']")
    frominput.send_keys("Delhi")

    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(@class,'sc-iwsKbI')]/div/text[1]")))

    autodropdownoptions = driver.find_elements(By.XPATH, "//li[contains(@class,'sc-iwsKbI')]/div/text[1]")

    print("Number of options:", len(autodropdownoptions))

    for option in autodropdownoptions:
        value = option.text
        print(value)

        if value == "RK Ashram":
            option.click()
            break


def HandleHiddenItems():
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@name='username']")))

    usernameinput = driver.find_element(By.XPATH, "//input[@name='username']")
    passwordinput = driver.find_element(By.XPATH, "//input[@name='password']")
    # submitbutton = driver.find_element(By.XPATH, "//button[@type='submit']")

    usernameinput.send_keys("Admin")
    passwordinput.send_keys("admin123")


def HandleDialogAlerts():
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)

    alert = Alert(driver)

    alertbutton = driver.find_element(By.XPATH, "//button[text()='Alert']")
    confirmbutton = driver.find_element(By.XPATH, "//button[text()='Confirm Box']")
    promptbutton = driver.find_element(By.XPATH, "//button[text()='Prompt']")
    promptmessage = driver.find_element(By.XPATH, "//p[@id='demo']")

    alertbutton.click()
    time.sleep(2)
    print(alert.text)
    alert.accept()

    confirmbutton.click()
    time.sleep(2)
    print(alert.text)
    alert.dismiss()

    promptbutton.click()
    time.sleep(2)
    print(alert.text)
    alert.send_keys("Python3")
    alert.accept()
    time.sleep(2)
    value = promptmessage.get_attribute("textContent")
    print(value)


def HandleFramesiFrames():
    url = "https://ui.vision/demo/webtest/frames/"
    driver.get(url)

    framewindow = driver.find_elements(By.XPATH, "//frame")
    print("Number of frames: ", len(framewindow))

    # approach 1: using locator
    driver.switch_to.default_content()
    frame1 = driver.find_element(By.XPATH, "//frame[@src='frame_1.html']")
    driver.switch_to.frame(frame1)
    frameinput = driver.find_element(By.XPATH, "//input[@name='mytext1']")
    frameinput.send_keys("This is frame 1")

    # approach 2: using index
    driver.switch_to.default_content()
    driver.switch_to.frame(4)
    frame5input = driver.find_element(By.XPATH, "//input[@name='mytext5']")
    frame5input.send_keys("This is frame 5")

    # nested
    driver.switch_to.default_content()
    frame3 = driver.find_element(By.XPATH, "//frame[@src='frame_3.html']")
    driver.switch_to.frame(frame3)
    frame3input = driver.find_element(By.XPATH, "//input[@name='mytext3']")
    frame3input.send_keys('This is frame 3')

    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
    driver.switch_to.frame(iframe)
    frame3radio = driver.find_element(By.XPATH, "//div[@id='i5']/div[3]/div")
    driver.execute_script("arguments[0].scrollIntoView()", frame3radio)
    time.sleep(2)
    frame3radio.click()


def HandleWebTablePagination():
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)

    tablelabel = driver.find_element(By.XPATH, "//h2[text()='Pagination Table']")
    driver.execute_script("arguments[0].scrollIntoView()", tablelabel)

    paginationtable = driver.find_element(By.XPATH, "//table[@id='productTable']")
    columns = paginationtable.find_elements(By.CSS_SELECTOR, "thead tr th")
    rows = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr")

    rowscells = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr td")

    print('Number of columns: ', len(columns))
    print('Number of rows: ', len(rows))

    # select checkbox
    matchedrow = driver.find_element(By.XPATH, "//td[text()='Product 2']//following-sibling::td//input")
    matchedrow.click()

    selectProduct("Product 4")
    selectProduct("Product 5")

    rowarray = []
    index = 0

    for elements in rowscells:
        rowarray.append(elements.text)
        index += 1
        if index == 4:
            print(rowarray)
            index = 0

    pages = driver.find_elements(By.XPATH, "//ul[@id='pagination']//li//a")
    for page in pages:
        print(page.text)
        page.click()

        rows = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr")
        for elements in rows:
            print(elements.text)


def selectProduct(productname):
    matchedrow = driver.find_element(By.XPATH, "//td[text()='" + productname + "']//following-sibling::td//input")
    matchedrow.click()


def HandleDatePickers():
    url = "https://testautomationpractice.blogspot.com/"
    driver.get(url)
    
    colorslabel = driver.find_element(By.XPATH, "//label[text()='Colors:']")
    driver.execute_script("arguments[0].scrollIntoView()", colorslabel)

    # direct type date
    
    datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
    datepicker.click()
    datepicker.send_keys('12/12/2023')
    action = ActionChains(driver)
    action.key_down(Keys.TAB).perform()
    action.key_up(Keys.TAB).perform()
    time.sleep(2)

    # using date picker
    datestring = '3/15/2024'
    datestringsplit = datestring.split('/')
    monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    month = monthname[int(datestringsplit[0]) - 1]
    day = datestringsplit[1]
    year = datestringsplit[2]

    datepicker.click()
    while True:
        displayedyear = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        displayedmonth = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        if displayedyear == year and displayedmonth == month:
            break
        driver.find_element(By.XPATH, "//span[text()='Next']").click()

    driver.find_element(By.XPATH, "//a[@class='ui-state-default'][text()='" + day + "']").click()
    action.key_down(Keys.TAB).perform()

    time.sleep(2)


def ExecutionEnd():
    time.sleep(3)
    driver.close()
    driver.quit()

    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
    print("[End Execution  ]", dt_string)


def StartTest():
    # HandleInputandRadio()
    # HandleDropdown()
    # HandleMultiDropdown()
    # HandleBootstrapDropdown()
    # HandleAutoSuggestion()
    # HandleHiddenItems()
    # HandleDialogAlerts()
    # HandleFramesiFrames()
    # HandleWebTablePagination()
    HandleDatePickers()
    ExecutionEnd()


StartTest()
