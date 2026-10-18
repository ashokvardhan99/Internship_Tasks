# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
# 20 Validating the Phone Number

import re
regex_pattern = r"^[789]\d{9}$"

for _ in range(int(input())):
        print("YES" if (re.match(regex_pattern, input())) else "NO")
