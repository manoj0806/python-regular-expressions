import re
hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\d{3}\s\w+\s[A-Za-z.,]*\s[A-Za-z]+\s[A-Z]+\s\d{0,6}', line)
    if len(x)>0:
        print(x[0])

