from bs4 import BeautifulSoup
from pprint import pprint
import re

from regex import money_regex


def handle_loan_balance_uls(uls, data):
    for ul in uls:
        handle_loan_balance_ul(ul, data)

def handle_loan_balance_ul(ul, data):
    lis = ul.find_all("li")

    for i, li in enumerate(lis):
        match_object = money_regex.search(li.text)
        string_with_no_comma = match_object.group(2).replace(',','')
        float_value = float(string_with_no_comma)

        if i == 0:
            data['original_balance'].append(float_value)
        elif i == 1:
            data['unpaid_interest'].append(float_value)
        elif i == 2:
            data['principal_balance'].append(float_value)