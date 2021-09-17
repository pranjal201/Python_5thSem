# TabNine::sem

import re
test = "food foobar fork found"
match1 = re.findall(r'(?:f*)d', test)
print(match1)
