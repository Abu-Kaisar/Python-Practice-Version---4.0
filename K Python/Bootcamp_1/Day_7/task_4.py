import re

rand_str = """<name>Life on Ruet</name>
<name>Life on Mars</name>"""

regex = re.compile("<name>.*?</name>")

print("Matches : ", len(re.findall(regex, rand_str)))

for i in re.findall(regex, rand_str):
    print(i)


