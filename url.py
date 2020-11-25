import re
hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('(https?://(www.)?\w+\.\w+)', line)
    if len(x)>0:
        print(x[0][0])