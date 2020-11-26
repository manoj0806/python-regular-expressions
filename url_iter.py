import re

pattern = re.compile(r'https?://(www.)?\w+\.\w+')
with open("sample.txt") as fh:
    content = fh.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
