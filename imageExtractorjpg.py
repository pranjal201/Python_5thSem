# TabNine::sem
import re
# url = "<html><head></head><body><img src='www.geeksforgeeks.org/sample/62.jpg'</body></html> <html><head></head><body><img src='www.geeksforgeeks.org/sample/99.jpg'</body></html>"
url = "<html><head></head><body><img src='www.geeksforgeeks.org/sample/99.jpg'</body></html>"

pattern = re.compile(r'www\.[a-zA-Z0-9]+\.[a-z]+/[a-z]+/[a-zA-Z0-9]+\.(jpg)')

matches = pattern.finditer(url)

for match in matches:
   link = match.group()

print(link)
