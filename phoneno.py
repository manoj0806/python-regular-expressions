import re
hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\d{3}.\d{3}.\d{4}', line)
    if len(x)>0:
        print(x)