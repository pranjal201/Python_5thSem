# TabNine::sem
from random import choice
import re
import string
test = "dog dope doze done dose doge"


pattern1 = re.compile(r'do.e')
matches = pattern1.finditer(test)

for match in matches:
    print(match.span(), match.group())

pattern2 = re.compile(r'doge$')
matches = pattern2.finditer(test)
for match in matches:
    print(match.span(), match.group())

test2 = test.replace(' ', str(choice(string.digits)))


pattern3 = re.compile(r'\d')
match2 = pattern3.finditer(test2)
for match in match2:
    print(match.span(), match.group())

pattern3 = re.compile(r'\D')
match2 = pattern3.finditer(test2)
for match in match2:
    print(match.span(), match.group())


