''' This is another list panga'''

line = "Pra&n^ja@l P2arm39ar"
#Output : GeeksforGeeks

 
import re
pattern = re.compile(r'[a-zA-Z]*')
newline = pattern.finditer(line)
ep = ""
for new in newline:
    ep = ep + new.group()


print(ep)
