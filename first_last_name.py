import re
hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^[A-Z].*\s[A-Z][a-z]+', line)
    if len(x)>0:
        print(x)