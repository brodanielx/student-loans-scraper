from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

from credentials import FEDLOAN_USERNAME, FEDLOAN_PASSWORD



def get_html():

    url = "https://myfedloan.org/"
    driver = webdriver.Chrome()
    # driver.implicitly_wait(30)
    driver.get(url)

    sign_in_button = driver.find_element_by_class_name("flyout-control")
    sign_in_button.click()

    username_input = driver.find_element_by_name("username")
    username_input.send_keys(FEDLOAN_USERNAME)

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(FEDLOAN_PASSWORD)

    sign_in_form_button = driver.find_element_by_name("signIn")
    sign_in_form_button.click()

    driver.implicitly_wait(30)
    loan_details_botton = driver.find_element_by_class_name("loanDetailsLink")
    loan_details_botton.click()

    links = driver.find_elements_by_tag_name("a")
    print_all_loan_details_url = "https://accountaccess.myfedloan.org/accountAccess/index.cfm?event=loan.getloanDetails&row=all&loanRegion=FD"
    print_all_loan_details_link = [link for link in links if link.get_attribute("href") == print_all_loan_details_url][0]
    print_all_loan_details_link.click()

    return driver.page_source


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    loan_header_divs = soup.find_all("div", class_="loanHeader")
    number_of_loans = len(loan_header_divs)

    loan_status_uls = soup.find_all("ul", title="Loan Status")
    disbursement_uls = soup.find_all("ul", title="Disbursement Information")  
    interest_rate_uls = soup.find_all("ul", title="Interest Rate Information")  
    loan_balance_uls = soup.find_all("ul", title="Loan Balance") 
    payment_uls = soup.find_all("ul", title="Payment Information") 
    due_date_uls = soup.find_all("ul", title="Due Date Information")

    handle_disbursement_ul(disbursement_uls[0])


def handle_disbursement_ul(ul):
    lis = ul.find_all("li")
    for li in lis:
        print(li.text)


def get_data():
    html = get_html()
    parse_html(html)


if __name__ == '__main__':
    get_data()