import re

pattern = re.compile(r'\d{3}\s\w+\s[A-Za-z.,]*\s[A-Za-z]+\s[A-Z]+\s\d{0,6}')
with open("sample.txt") as fh:
    content = fh.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
