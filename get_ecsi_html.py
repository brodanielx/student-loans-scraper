from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

from credentials import ECSI_ACCOUNT_NUMBER, ECSI_PIN
from ecsi_constants import (
    balance_and_billing_link_text,
    current_account_balance_link_text,
    login_button_name,
    pin_input_name,
    student_id_input_name
)


def get_ecsi_html():
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

    return driver.page_source


def get_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'summary': 'Current Account Balance'})
    return table

def get_data_frame_from_html_table(table):
    data = pd.read_html(table)
    print(data)




if __name__ == '__main__':
    html = get_ecsi_html()
    table = get_table(html)
    get_data_frame_from_html_table(table)