from bs4 import BeautifulSoup
from pprint import pprint
import re

from regex import colon_regex, date_regex



def handle_loan_status_uls(uls, data):
    for ul in uls:
        handle_loan_status_ul(ul, data)

def handle_loan_status_ul(ul, data):
    li = ul.find("li")
    match_object = colon_regex.search(li.text)
    data_str = match_object.group(2).title()
    data['Loan Status'].append(data_str)