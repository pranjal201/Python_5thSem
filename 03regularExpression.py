# TabNine::sem
import re

test = "123abcsjlfkjaabcsldfjlABC"

pattern = re.compile(r"abc")

matches = pattern.finditer(test)

for match in matches:
    print(match)

matches = pattern.findall(test)
for match in matches:
    print(match)

matches = re.match(r"123", test)
print(matches)

matches = pattern.search(test)
print(match)

# This is just a practise about the methods used in the regex module in python
# later in the next programming working on the finditer() method 
