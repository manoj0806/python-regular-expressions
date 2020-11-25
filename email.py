import re
hand = open('sample.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9.-]+@[A-Za-z-]+\.\w+', line)
    if len(x)>0:
        print(x)