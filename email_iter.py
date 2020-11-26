import re
pattern = re.compile(r'[a-zA-Z0-9.-]+@[A-Za-z-]+\.\w+')
with open("sample.txt") as fh:
    content = fh.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
    