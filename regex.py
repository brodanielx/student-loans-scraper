import re

colon_regex = re.compile(r'(:\s*)([\w\s.]+)')
date_regex = re.compile(r'\d+/\d+/\d+')
money_regex = re.compile(r'(\$)([\d,]+\.\d+)')
percentage_regex = re.compile(r'(\d+\.\d+)(%)')