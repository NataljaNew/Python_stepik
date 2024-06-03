import re
text = input()

result1 = re.findall(r'7-\d\d\d-\d\d\d-\d\d-\d\d', text)
result2 = re.findall(r'8-\d\d\d-\d\d\d\d-\d\d\d\d', text)
for r in result1+result2:
    print (r)
