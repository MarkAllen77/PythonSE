import os.path
import time

import cv2 as cv
import pyautogui
import numpy as np

import threading

from datetime import datetime

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

from page import ClassGoogle


class MyClasss:
    def __init__(self):
        self.x = 55

    @staticmethod
    def loopprint():
        for i in range(5):
            print(i)


class PythonSE:
    def __init__(self):
        cservice = webdriver.ChromeService(executable_path='./chromedriver.exe')
        # driver = webdriver.Chrome(service=cService)

        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=cservice, options=chrome_options)

    def HandleInputandRadio(self):
        # dd/mm/YY H:M:S
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
        print("[Start Execution]", dt_string)

        url = "https://demoqa.com/automation-practice-form"
        self.driver.get(url)

        # ----- How to handle Inputbox & RadioButtons -----
        firstnameinput = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
        lastnameinput = self.driver.find_element(By.XPATH, "//input[@id='lastName']")

        print(firstnameinput.is_displayed())
        print(firstnameinput.is_enabled())
        print("Current value: ", firstnameinput.get_attribute("value"))

        firstnameinput.send_keys("John")
        lastnameinput.send_keys("Doe")

        print("Updated value: ", firstnameinput.get_attribute("value"))

        gendermalelabel = self.driver.find_element(By.XPATH, "//label[text() = 'Male']")
        genderfemalelabel = self.driver.find_element(By.XPATH, "//label[text() = 'Female']")
        gendermaleradiobutton = self.driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
        genderfemaleradiobutton = self.driver.find_element(By.XPATH, "//input[@id='gender-radio-2']")

        print("Radiobutton", gendermaleradiobutton.is_selected())
        gendermalelabel.click()
        print(gendermaleradiobutton.is_selected())
        print(genderfemaleradiobutton.is_selected())
        genderfemalelabel.click()
        print(genderfemaleradiobutton.is_selected())

        # ----- How to handle Checkboxes -----
        hobbiessportslabel = self.driver.find_element(By.XPATH, "//label[text() = 'Sports']")
        hobbiessportscheckbox = self.driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-1']")
        hobbiesreadinglabel = self.driver.find_element(By.XPATH, "//label[text() = 'Reading']")
        hobbiesreadingcheckbox = self.driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-2']")

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
            self.driver.find_element(By.XPATH, box).click()

    def HandleDropdown(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        countrydropdown = self.driver.find_element(By.XPATH, "//select[@id='country']/option[text()='Canada']")
        countrydropdown.click()

        countrydropdownobject = Select(self.driver.find_element(By.XPATH, "//select[@id='country']"))
        time.sleep(1)
        countrydropdownobject.select_by_index(3)  # germany
        time.sleep(1)
        countrydropdownobject.select_by_visible_text("India")
        time.sleep(1)
        countrydropdownobject.select_by_value('usa')

        print("Numer of options: ", len(countrydropdownobject.options))
        print("Current value: ", countrydropdownobject.first_selected_option.text)

        countrydropdownoptions = self.driver.find_elements(By.XPATH, "//select[@id='country']/option")
        time.sleep(1)
        countrydropdownoptions[5].click()  # australia

    def HandleMultiDropdown(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        colorslabel = self.driver.find_element(By.XPATH, "//label[contains(.,'Colors')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", colorslabel)

        colorsdropdown = self.driver.find_element(By.XPATH, "//select[@id='colors']/option[text()='Red']")
        colorsdropdown.click()

        colorsdropdownobject = Select(self.driver.find_element(By.XPATH, "//select[@id='colors']"))
        time.sleep(1)
        colorsdropdownobject.select_by_index(1)  # blue
        time.sleep(1)
        colorsdropdownobject.select_by_visible_text("Green")
        time.sleep(1)
        colorsdropdownobject.select_by_value('white')

        print("Numer of options: ", len(colorsdropdownobject.options))

        for colors in colorsdropdownobject.all_selected_options:
            print("Value: ", colors.text)

    def HandleBootstrapDropdown(self):
        url = "https://www.jquery-az.com/boots/demo.php?ex=63.0_2"
        self.driver.get(url)

        outputbutton = self.driver.find_element(By.XPATH, "//button")
        outputoption = self.driver.find_elements(By.XPATH, "//ul//li//label//input")

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

    def HandleAutoSuggestion(self):
        url = "https://www.redbus.in/"
        self.driver.get(url)

        frominput = self.driver.find_element(By.XPATH, "//input[@id='src']")
        frominput.send_keys("Delhi")

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(@class,'sc-iwsKbI')]/div/text[1]")))

        autodropdownoptions = self.driver.find_elements(By.XPATH, "//li[contains(@class,'sc-iwsKbI')]/div/text[1]")

        print("Number of options:", len(autodropdownoptions))

        for option in autodropdownoptions:
            value = option.text
            print(value)

            if value == "RK Ashram":
                option.click()
                break

    def HandleHiddenItems(self):
        url = "https://opensource-demo.orangehrmlive.com/"
        self.driver.get(url)

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@name='username']")))

        usernameinput = self.driver.find_element(By.XPATH, "//input[@name='username']")
        passwordinput = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # submitbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        usernameinput.send_keys("Admin")
        passwordinput.send_keys("admin123")

    def HandleDialogAlerts(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        alert = Alert(self.driver)

        alertbutton = self.driver.find_element(By.XPATH, "//button[text()='Alert']")
        confirmbutton = self.driver.find_element(By.XPATH, "//button[text()='Confirm Box']")
        promptbutton = self.driver.find_element(By.XPATH, "//button[text()='Prompt']")
        promptmessage = self.driver.find_element(By.XPATH, "//p[@id='demo']")

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

    def HandleFramesiFrames(self):
        url = "https://ui.vision/demo/webtest/frames/"
        self.driver.get(url)

        framewindow = self.driver.find_elements(By.XPATH, "//frame")
        print("Number of frames: ", len(framewindow))

        # approach 1: using locator
        self.driver.switch_to.default_content()
        frame1 = self.driver.find_element(By.XPATH, "//frame[@src='frame_1.html']")
        self.driver.switch_to.frame(frame1)
        frameinput = self.driver.find_element(By.XPATH, "//input[@name='mytext1']")
        frameinput.send_keys("This is frame 1")

        # approach 2: using index
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        frame5input = self.driver.find_element(By.XPATH, "//input[@name='mytext5']")
        frame5input.send_keys("This is frame 5")

        # nested
        self.driver.switch_to.default_content()
        frame3 = self.driver.find_element(By.XPATH, "//frame[@src='frame_3.html']")
        self.driver.switch_to.frame(frame3)
        frame3input = self.driver.find_element(By.XPATH, "//input[@name='mytext3']")
        frame3input.send_keys('This is frame 3')

        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe')
        self.driver.switch_to.frame(iframe)
        frame3radio = self.driver.find_element(By.XPATH, "//div[@id='i5']/div[3]/div")
        self.driver.execute_script("arguments[0].scrollIntoView()", frame3radio)
        time.sleep(2)
        frame3radio.click()

    def HandleWebTablePagination(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        tablelabel = self.driver.find_element(By.XPATH, "//h2[text()='Pagination Table']")
        self.driver.execute_script("arguments[0].scrollIntoView()", tablelabel)

        paginationtable = self.driver.find_element(By.XPATH, "//table[@id='productTable']")
        columns = paginationtable.find_elements(By.CSS_SELECTOR, "thead tr th")
        rows = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr")

        rowscells = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr td")

        print('Number of columns: ', len(columns))
        print('Number of rows: ', len(rows))

        # select checkbox
        matchedrow = self.driver.find_element(By.XPATH, "//td[text()='Product 2']//following-sibling::td//input")
        matchedrow.click()

        self.selectProduct("Product 4")
        self.selectProduct("Product 5")

        rowarray = []
        index = 0

        for elements in rowscells:
            rowarray.append(elements.text)
            index += 1
            if index == 4:
                print(rowarray)
                index = 0

        pages = self.driver.find_elements(By.XPATH, "//ul[@id='pagination']//li//a")
        for page in pages:
            print(page.text)
            page.click()

            rows = paginationtable.find_elements(By.CSS_SELECTOR, "tbody tr")
            for elements in rows:
                print(elements.text)

    def selectProduct(self, productname):
        matchedrow = self.driver.find_element(By.XPATH, "//td[text()='" + productname + "']//following-sibling::td//input")
        matchedrow.click()

    def HandleDatePickers(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        colorslabel = self.driver.find_element(By.XPATH, "//label[text()='Colors:']")
        self.driver.execute_script("arguments[0].scrollIntoView()", colorslabel)

        # direct type date
        datepicker = self.driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()
        datepicker.send_keys('12/12/2023')
        action = ActionChains(self.driver)
        action.key_down(Keys.TAB).perform()
        action.key_up(Keys.TAB).perform()
        time.sleep(2)

        # using date picker
        datestring = '3/15/2024'
        datestringsplit = datestring.split('/')
        monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                     "December"]

        month = monthname[int(datestringsplit[0]) - 1]
        day = datestringsplit[1]
        year = datestringsplit[2]

        datepicker.click()
        while True:
            displayedyear = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            displayedmonth = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            if displayedyear == year and displayedmonth == month:
                break
            self.driver.find_element(By.XPATH, "//span[text()='Next']").click()

        self.driver.find_element(By.XPATH, "//a[@class='ui-state-default'][text()='" + day + "']").click()
        action.key_down(Keys.TAB).perform()

        time.sleep(2)

    def HandleMouseActions(self):
        url = "https://demo.opencart.com/"
        self.driver.get(url)

        # -----How to handle Mouse Hover-----
        desktopslabel = self.driver.find_element(By.XPATH, "//a[text()='Desktops']")
        maclabel = self.driver.find_element(By.XPATH, "//a[text()='Mac (1)']")

        action = ActionChains(self.driver)
        action.move_to_element(desktopslabel).perform()
        action.move_to_element(maclabel).perform()

        time.sleep(2)

        # -----How to handle Mouse Right Click-----
        self.driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

        buttonrightclick = self.driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        action.context_click(buttonrightclick).perform()
        time.sleep(1)

        pastecontext = self.driver.find_element(By.XPATH, "//span[text()='Paste']")
        action.move_to_element(pastecontext).perform()

        time.sleep(2)

        # -----How to handle Mouse Double Click-----
        self.driver.get('https://testautomationpractice.blogspot.com/')

        buttondoubleclick = self.driver.find_element(By.XPATH, "//button[text()='Copy Text']")
        action.double_click(buttondoubleclick).perform()

        field1 = self.driver.find_element(By.XPATH, "//input[@id='field1']").get_attribute("value")
        print("Text is: ", field1)

        field2 = self.driver.find_element(By.XPATH, "//input[@id='field2']").get_attribute("value")
        print("Text is: ", field2)

        # -----How to handle Mouse Drag and Drop-----
        draggable = self.driver.find_element(By.XPATH, "//div[@id='draggable']")
        droppable = self.driver.find_element(By.XPATH, "//div[@id='droppable']")

        action.drag_and_drop(draggable, droppable).perform()

    def HandleKeyboardActions(self):
        url = "https://gotranscript.com/text-compare/"
        self.driver.get(url)

        fromtextarea = self.driver.find_element(By.XPATH, "//textarea[@name='text1']")
        totextarea = self.driver.find_element(By.XPATH, "//textarea[@name='text2']")
        buttoncompare = self.driver.find_element(By.XPATH, "//button[@id='recaptcha']")

        fromtextarea.send_keys("Hello World was here")
        fromtextarea.click()

        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL) \
            .send_keys('a') \
            .send_keys('c') \
            .perform()

        totextarea.click()
        action.key_down(Keys.CONTROL) \
            .send_keys('v') \
            .perform()

        buttoncompare.click()

        time.sleep(2)

    def HandleUploadFiles(self):
        url = "https://www.foundit.in/"
        self.driver.get(url)

        try:
            time.sleep(2)
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.presence_of_element_located((By.XPATH, "//i[@class='mqfihd-upload']")))

        except TimeoutException as ex:
            print("-- [TIMEOUT] --")
            print(ex)

        url = "https://davidwalsh.name/demo/multiple-file-upload.php"
        self.driver.get(url)

        nofileslabel = self.driver.find_element(By.XPATH, "//ul[@id='fileList']/li")
        print("\"No Files Selcted = \"", nofileslabel.text)

        filestouploadbutton = self.driver.find_element(By.XPATH, "//input[@id='filesToUpload']")
        filestouploadbutton.send_keys("C:/Temp/sample1.txt \n C:/Temp/sample2.txt")

        filename1 = self.driver.find_element(By.XPATH, "//ul[@id='fileList']/li[1]")
        filename2 = self.driver.find_element(By.XPATH, "//ul[@id='fileList']/li[2]")

        print("\"sample1.txt\"= ", filename1.text)
        print("\"sample2.txt\"= ", filename2.text)

    def HandlePagesWindows(self):
        url = "https://opensource-demo.orangehrmlive.com/"
        self.driver.get(url)

        originalwindow = self.driver.current_window_handle
        print(self.driver.title)

        self.driver.switch_to.new_window('tab')
        self.driver.get("https://www.orangehrm.com/")
        tabwindow = self.driver.current_window_handle
        print(self.driver.title)

        self.driver.switch_to.new_window('window')
        self.driver.get("https://www.google.com/")
        newwindow = self.driver.current_window_handle
        print(self.driver.title)
        time.sleep(2)
        self.driver.close()

        print("Original Window: ", originalwindow)
        print("Tab Window: ", tabwindow)
        print("New Window: ", newwindow)

        totalwindows = self.driver.window_handles
        print("Number of Window(s): ", len(totalwindows))

        self.driver.switch_to.window(tabwindow)
        time.sleep(1)
        self.driver.close()

        self.driver.switch_to.window(originalwindow)
        time.sleep(2)

    def HandleMultiplePagesWindows(self):
        url = "https://opensource-demo.orangehrmlive.com/"
        self.driver.get(url)

        # Original Window
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        originalwindow = self.driver.current_window_handle
        print(self.driver.title)

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//a[text()='OrangeHRM, Inc']")))

        orangelink = self.driver.find_element(By.XPATH, "//a[text()='OrangeHRM, Inc']")
        orangelink.click()

        # New Tab
        openwindows = self.driver.window_handles
        self.driver.switch_to.window(openwindows[1])

        tabwindow = self.driver.current_window_handle
        print(self.driver.title)

        # New Window
        self.driver.switch_to.new_window('window')
        self.driver.get("https://www.google.com")
        newwindow = self.driver.current_window_handle
        print(self.driver.title)
        time.sleep(2)

        print("Original Window: ", originalwindow)
        print("Tab Window: ", tabwindow)
        print("New Window: ", newwindow)

        totalwindows = self.driver.window_handles
        print("Number of Window(s): ", len(totalwindows))

        self.driver.switch_to.window(originalwindow)
        usernameinput = self.driver.find_element(By.XPATH, "//input[@name='username']")
        usernameinput.send_keys("username123")
        time.sleep(3)

        self.driver.switch_to.window(tabwindow)
        usernameinput = self.driver.find_element(By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']")
        usernameinput.send_keys("username123@gmail.com")
        time.sleep(3)
        self.driver.close()
        time.sleep(3)

        self.driver.switch_to.window(newwindow)
        usernameinput = self.driver.find_element(By.XPATH, "//textarea[@name='q']")
        usernameinput.send_keys("python 3")
        time.sleep(3)
        self.driver.close()

        self.driver.switch_to.window(originalwindow)

    def HandleCaptureScreen(self):
        url = "https://testautomationpractice.blogspot.com/"
        self.driver.get(url)

        now = datetime.now()
        dt_string = now.strftime("%m%d%Y_%I%M%S")

        if not os.path.exists("./captures"):
            os.makedirs("./captures")
            print("Directory created")
        else:
            print("Directory already exists")

        savefile = "./captures/window_" + dt_string + ".png"
        print(savefile)
        self.driver.save_screenshot(savefile)

        savefile = "./captures/element_" + dt_string + ".png"
        droppablelement = self.driver.find_element(By.XPATH, "//div[@id='droppable']")
        droppablelement.screenshot(savefile)

    def HandleUsingClass(self):
        # class within same file
        myclassinstance = MyClasss()
        print(myclassinstance.x)
        myclassinstance.loopprint()

        # class from external file
        classgoogleinstance = ClassGoogle(self.driver)
        classgoogleinstance.openPage("https://www.google.com")
        classgoogleinstance.enterSearchInput("python 3")
        time.sleep(2)

    def Screen(self):
        url = "https://www.google.com/"
        self.driver.get(url)

        self.driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("selenium python video capture")
        time.sleep(1)
        action = ActionChains(self.driver)
        action.key_down(Keys.ESCAPE)
        action.key_down(Keys.ENTER)
        action.perform()
        time.sleep(2)

    def ExecutionEnd(self):
        time.sleep(3)
        self.driver.quit()

        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %I:%M:%S")
        print("[End Execution  ]", dt_string)


def Recorder():
    # (width,height)
    screen_size = pyautogui.size()

    # initialize the object
    video = cv.VideoWriter('./recording/VideoSE.avi', cv.VideoWriter.fourcc(*'MJPG'), 20, screen_size)

    print("Recording.....")
    while recorderstatus:
        # click screenshot
        screen_shot_img = pyautogui.screenshot()

        # convert into array
        frame = np.array(screen_shot_img)

        # change from BGR to RGB
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # write frame
        video.write(frame)

        # display the live recording
        # cv.imshow("Recording Frame(Minimize it)", frame)
        # if cv.waitKey(1) == ord("q"):
        #     break

    cv.destroyAllWindows()
    video.release()


PythonSEInstance = PythonSE()


def CoreFunctions():
    PythonSEInstance.HandleInputandRadio()
    PythonSEInstance.HandleDropdown()
    PythonSEInstance.HandleMultiDropdown()
    PythonSEInstance.HandleBootstrapDropdown()
    PythonSEInstance.HandleAutoSuggestion()
    PythonSEInstance.HandleHiddenItems()
    PythonSEInstance.HandleDialogAlerts()
    PythonSEInstance.HandleFramesiFrames()
    PythonSEInstance.HandleWebTablePagination()
    PythonSEInstance.HandleDatePickers()
    PythonSEInstance.HandleMouseActions()
    PythonSEInstance.HandleKeyboardActions()
    PythonSEInstance.HandleUploadFiles()
    PythonSEInstance.HandlePagesWindows()
    PythonSEInstance.HandleMultiplePagesWindows()
    PythonSEInstance.HandleCaptureScreen()
    PythonSEInstance.HandleUsingClass()
    PythonSEInstance.ExecutionEnd()


recorderstatus = True
thread1 = threading.Thread(target=Recorder)
thread2 = threading.Thread(target=CoreFunctions)


def StartTest():
    thread1.start()
    thread2.start()

    thread2.join()

    global recorderstatus
    recorderstatus = False


StartTest()
