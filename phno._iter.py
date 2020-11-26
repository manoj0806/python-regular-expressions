import re
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
with open('sample.txt') as fh:
    content=fh.read()
    data = pattern.finditer(content)
    for i in data:
        print(i)
