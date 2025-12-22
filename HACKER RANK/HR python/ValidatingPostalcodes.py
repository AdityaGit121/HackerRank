regex_integer_in_range = r'^[1-9][0-9]{5}$'   # 6-digit number, not starting with 0
regex_alternating_repetitive_digit_pair = r'(?=(\d)\d\1)'  # alternating repetitive digit pairs

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
       and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)