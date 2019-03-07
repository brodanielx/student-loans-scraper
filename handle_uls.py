from bs4 import BeautifulSoup
from pprint import pprint
import re

from create_dictionary import create_data_dictionary
from loan_status import handle_loan_status_uls
from regex import colon_regex, date_regex


def handle_uls(uls_dict):
    loan_status_uls = uls_dict['Loan Status'] 
    disbursement_uls = uls_dict['Disbursement']
    interest_rate_uls = uls_dict['Interest Rate']
    loan_balance_uls = uls_dict['Loan Balance']
    payment_uls = uls_dict['Payment']
    due_date_uls = uls_dict['Due Date']

    data = create_data_dictionary()

    handle_loan_status_uls(loan_status_uls, data)
    handle_disbursement_uls(disbursement_uls, data)


def handle_disbursement_uls(uls, data):
    for ul in uls:
        handle_disbursement_ul(ul, data)
    pprint(data, indent=2)

def handle_disbursement_ul(ul, data):
    lis = ul.find_all("li")

    disbursement_date_match_object = date_regex.search(lis[0].text)
    data['Disbursement Date'].append(disbursement_date_match_object.group())

    loan_program_match_object = colon_regex.search(lis[1].text)
    data['Loan Program'].append(loan_program_match_object.group(2).title())

    owner_match_object = colon_regex.search(lis[2].text)
    data['Owner'].append(owner_match_object.group(2).title())

    guarantor_match_object = colon_regex.search(lis[3].text)
    data['Guarantor'].append(guarantor_match_object.group(2).title())

    school_match_object = colon_regex.search(lis[4].text)
    data['School'].append(school_match_object.group(2).title())

    out_of_school_date_match_object = date_regex.search(lis[5].text)
    data['Out of School Date'].append(out_of_school_date_match_object.group())
