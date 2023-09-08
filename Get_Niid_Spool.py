# Import the required modules
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import os
from pathlib import Path

from test import change_sheet_name


# Main Function


def get_niid_spool(start_date,end_date):

    downloads_path = Path.home() / "Downloads"
    directory_path = downloads_path
    file_name = "NIID Spool.xlsx"
    file_path = os.path.join(directory_path, file_name)
    # Provide the email and password
    email = "mayowa_admin"
    password = "Gbohunmi17"

    # start_date = "01-Sep-2023"
    # end_date = "30-Sep-2023"

    options = webdriver.ChromeOptions()
    # options.add_argument("download.default_directory=C:/Downloads")
    # prefs = {'download.default_directory': 'C:\\Users\\ICT001\\PycharmProjects\\A&G Software'}
    # options.add_experimental_option('prefs', prefs)
    # options.add_argument("--headless=new")
    # options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(options=options, service=service)
    # driver.set_window_size(1920, 1080)

    # Send a get request to the url
    driver.get("https://aginsuranceapplications.com/card/Index.aspx")
    time.sleep(0.2)
    # https: // auth.geeksforgeeks.org /

    # Finds the input box by name in DOM tree to send both
    # the provided email and password in it.
    username = driver.find_element(by="xpath",
                                   value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[1]')
    username.send_keys(email)
    keycode = driver.find_element(by="xpath",
                                  value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[2]')
    keycode.send_keys(password)

    # Find the signin button and click on it.
    driver.find_element(by="xpath", value='//div/input[3]').click()
    time.sleep(0.2)

    # Find the Utility  button and click on it.
    driver.find_element(
        by="xpath", value='//div[@class="menu-list"]/ul/ul/div[6]/div/li/a').click()
    time.sleep(0.5)

    # Find the Update Policy button and click on it.
    driver.find_element(
        by="xpath", value='//div[@class="menu-list"]/ul/ul/div[6]/div[2]/ul/li[3]').click()
    time.sleep(0.5)

    # Find the Search by option and click on it.
    driver.find_element(
        by="xpath",
        value='//div[@class="col-md-12"]/select').click()
    time.sleep(0.2)

    # Find the fetch by policy button and click on it.
    driver.find_element(
        by="xpath",
        value='//div[@class="col-md-12"]/select/option[5]').click()
    time.sleep(0.5)

    # Finds the input box by name in DOM tree to send
    # the provided start date to it
    policy_number = driver.find_element(
        by="xpath",
        value='//div[@class="row"][3]/div/input')
    policy_number.send_keys(start_date)
    time.sleep(0.5)
    # Finds the input box by name in DOM tree to send
    # the provided end date to it
    policy_number = driver.find_element(
        by="xpath",
        value='//div[@class="row"][3]/div[2]/input')
    policy_number.send_keys(end_date)
    time.sleep(0.5)

    # Find the Spool button and click on it.
    driver.find_element(
        by="xpath",
        value='//div[@class="row"][4]/input').click()
    time.sleep(2)

    try:
      while not os.path.isfile(file_path):
        time.sleep(5)
        print(f"The file '{file_name}' does not exists in the directory '{directory_path}'.")
    except Exception as e:
        print(e)


    time.sleep(5)

    time.sleep(5)










