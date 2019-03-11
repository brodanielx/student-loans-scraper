from bs4 import BeautifulSoup
from pprint import pprint
import re

from regex import colon_regex, date_regex



def handle_disbursement_uls(uls, data):
    for ul in uls:
        handle_disbursement_ul(ul, data)

def handle_disbursement_ul(ul, data):
    lis = ul.find_all("li")

    disbursement_date_match_object = date_regex.search(lis[0].text)
    data['disbursement_date'].append(disbursement_date_match_object.group())

    loan_program_match_object = colon_regex.search(lis[1].text)
    data['loan_program'].append(loan_program_match_object.group(2).title())

    owner_match_object = colon_regex.search(lis[2].text)
    data['owner'].append(owner_match_object.group(2).title())

    guarantor_match_object = colon_regex.search(lis[3].text)
    data['guarantor'].append(guarantor_match_object.group(2).title())

    school_match_object = colon_regex.search(lis[4].text)
    data['school'].append(school_match_object.group(2).title())

    out_of_school_date_match_object = date_regex.search(lis[5].text)
    data['out_of_school_date'].append(out_of_school_date_match_object.group())
