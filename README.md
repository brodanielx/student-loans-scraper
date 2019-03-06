# student-loans-scraper


#ToDo
- use pd.DataFrame
- for each group of uls
    - data = handle_uls(usl, data)
        - data = handle_ul(ul, data)
            - match_object = get data w/ regex 
            - data['Loan Status'].append(match_object.group())
- handle_uls.py
    - handle_uls(uls_dict)
    - handle_###_uls(uls, data)
    - handle_###_ul(ul, data)
- create_dictionaries.py
    - create_data_dict()
        - data = {
            'Loan Status' : [],
            'Disbursement Data' : [],
            .
            .
            .
            'Days Delinquent' : []
        }
    - create_uls_dict()

