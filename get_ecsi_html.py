from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pprint import pprint

from credentials import ECSI_ACCOUNT_NUMBER, ECSI_PIN
from ecsi_constants import (
    balance_and_billing_link_text,
    current_account_balance_link_text,
    login_button_name,
    pin_input_name,
    student_id_input_name
)

url = "https://www.ecsi.net/cgi-bin/bcgi.exe?blogm3"
driver = webdriver.Chrome()
driver.get(url)

student_id_input = driver.find_element_by_name(student_id_input_name)
student_id_input.send_keys(ECSI_ACCOUNT_NUMBER)

pin_input = driver.find_element_by_name(pin_input_name)
pin_input.send_keys(ECSI_PIN)

login_button = driver.find_element_by_name(login_button_name)
login_button.click()

balance_and_billing_link = driver.find_element_by_link_text(balance_and_billing_link_text)
balance_and_billing_link.click()

current_account_balance_link = driver.find_element_by_link_text(current_account_balance_link_text)
current_account_balance_link.click()

