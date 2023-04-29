import re
pattern1 = re.compile(r"[\w\- ]{1,20}")
pattern2 = re.compile(r"[\d]")
a = 'dЇ2'
print(pattern2.search(a))
print(bool(pattern1.fullmatch(a)) and not bool(pattern2.search(a)))