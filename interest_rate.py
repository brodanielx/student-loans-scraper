from bs4 import BeautifulSoup
from pprint import pprint
import re

from regex import colon_regex, date_regex, percentage_regex


def handle_interest_rate_uls(uls, data):
    for ul in uls:
        handle_interest_rate_ul(ul, data)
    # pprint(data, indent=2)

def handle_interest_rate_ul(ul, data):
    lis = ul.find_all("li")

    interest_rate_match_object = percentage_regex.search(lis[0].text)
    rate = float(interest_rate_match_object.group(1))
    data['Interest Rate'].append(rate)

    interest_rate_type_text = lis[1].text
    interest_rate_type_stripped = "".join(interest_rate_type_text.split()) 
    print(interest_rate_type_stripped)
    # interest_rate_type_match_object = colon_regex.search(interest_rate_type_stripped)
    # data['Interest Rate Type'].append(interest_rate_type_match_object.group(2).title())

