import re

rand_str = "412-555-1212 412-555-1213 412-555-1214"

regex = re.compile("412-([\d\-]*)")

for i in re.findall(regex, rand_str):
    print(i)


