# TabNine::sem

import re

s = "The quick brown fox jumped over the lazy dog."
match1 = re.findall(r'\.', s)
print(match1)

match2 = re.findall(r'[abc]', s)
print(match2)

match3 = re.findall(r'[^abc]', s)
print(match3)

str1 = "Geeksforgeeks.com"

match4 = re.findall(r'^Geeks', str1)
print(match4)

match4 = re.findall(r'com$', str1)
print(match4)

match5 = re.findall(r'g|G', str1)
print(match5)
print(type(match5))

str2 = "missisippi"
match6 = re.findall(r'is*', str2)
print(match6)


str3 = "asljdfablskdjflsjdlfabbbbbbbbbbsdlfjlababab"
match7 = re.findall(r'ab*', str3)
print(match7)
match7 = re.findall(r'ab+', str3)
print(match7)
match7 = re.findall(r'ab?', str3)
print(match7)

match7 = re.findall(r'b{3,6}', str3)
print(match7)

str3 = "dopedonedozedogedote"
match7 = re.findall(r'do*e', str3)
print(match7)


