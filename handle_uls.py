from bs4 import BeautifulSoup
import re

colon_regex = re.compile(r'(:\s)([\w\s.]+)')

def handle_uls(uls_dict):
    loan_status_uls = uls_dict['Loan Status'] 
    disbursement_uls = uls_dict['Disbursement']
    interest_rate_uls = uls_dict['Interest Rate']
    loan_balance_uls = uls_dict['Loan Balance']
    payment_uls = uls_dict['Payment']
    due_date_uls = uls_dict['Due Date']

    # create_dictionaries.py => create_data_dict()
    data = {
        'Loan Status' : []
    }

    handle_loan_status_ul(loan_status_uls[0], data)


def handle_loan_status_uls(uls, data):
    for ul in uls:
        handle_loan_status_ul(ul, data)

def handle_loan_status_ul(ul, data):
    li = ul.find("li")
    match_object = colon_regex.search(li.text)
    data_str = match_object.group(2).title()
    data['Loan Status'].append(data_str)
    print(data)





def handle_disbursement_ul(ul):
    colon_regex = re.compile(r'(:\s)([\w\s.]+)')
    date_regex = re.compile(r'\d+/\d+/\d+')
    
    lis = ul.find_all("li")
    date_lis = [lis[0], lis[5]]
    text_lis = lis[1:5]

    for li in date_lis:
        match_object = date_regex.search(li.text)
        # print(li.text)
        print(match_object.group())

    for li in text_lis:
        match_object = colon_regex.search(li.text)
        # print(li.text)
        print(match_object.group(2).title())
