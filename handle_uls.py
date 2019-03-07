from bs4 import BeautifulSoup
from pprint import pprint
import re

from create_dictionary import create_data_dictionary
from disbursement import handle_disbursement_uls
from interest_rate import handle_interest_rate_uls
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
    handle_interest_rate_uls(interest_rate_uls, data)


