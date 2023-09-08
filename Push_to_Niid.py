from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


def Push_to_Niid():
    # Provide the email and password
    email = 'ag.vera'
    password = 'insurance'
    comapny_email = 'info@aginsuranceplc.com'


    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(options=options, service=service)
    # driver.set_window_size(1920, 1080)

    #driver.find_element(by="id", value="file-upload").send_keys("C:/Users/ICT001/Downloads/selenium-snapshot.PNG")
    # Send a get request to the url
    driver.get('https://niid.org/default.aspx')
    time.sleep(0.2)
    # Finds the input box by name in DOM tree to send both
    # the provided email and password in it.
    username = driver.find_element(by="xpath",
                                   value='//div[@id="MainContent_UpdatePanel1"]/table/tbody/tr[2]/td[2]/span/input')
    username.send_keys(email)
    keycode = driver.find_element(by="xpath",
                                  value='//input[@class="riTextBox riEnabled Textbox_Large"]')
    keycode.send_keys(password)
    time.sleep(0.8)

    # Find the Login button and click on it.
    driver.find_element(
        by="xpath", value='//div[@id="MainContent_UpdatePanel1"]/table/tbody/tr[7]/td/a/input').click()
    time.sleep(0.8)

    # Find upload button and click on it
    driver.find_element(by="xpath", value='//form/table/tbody/tr[5]/td[2]/div/div/a[2]').click()
    time.sleep(0.8)

    # Checking for the alert and clicking on it
    alert = driver.switch_to.alert
    alert.accept()

    # Find select button and click on it
    driver.find_element(by="xpath", value='//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[6]/td/table/tbody/tr[4]/td[2]/select').click()
    time.sleep(0.8)

    # Find select button and click on it
    driver.find_element(by="xpath",
                        value='//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[6]/td/table/tbody/tr[4]/td[2]/select/option[2]').click()
    time.sleep(0.8)


    #Uploading the file
    time.sleep(0.8)
    driver.find_element(by="xpath", value="//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[7]/td[2]/div/ul/li/span/input[3]").send_keys("C:/Users/ICT001/Downloads/NIID Spool.xlsx")
    time.sleep(5)

    #Upload button
    driver.find_element(by="xpath", value="//form/table/tbody/tr[7]/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[9]/TD[2]/span/input").click()
    cssValue = driver.find_element(
        by="xpath", value='//div[@id="MainContent_UpdateProgress1"]').value_of_css_property('display')
    print(cssValue)

    while cssValue == 'block':
        cssValue = driver.find_element(
            by="xpath", value='//div[@id="MainContent_UpdateProgress1"]').value_of_css_property('display')
        print(cssValue)
        print('Loading...')
        time.sleep(5)
        if cssValue == 'none':
            print("Done Loading✅")

    errmessage = driver.find_element(by="xpath", value='//span[@id="MainContent_lblErrorMessage"]')
    time.sleep(2)
    return errmessage.text





