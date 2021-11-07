import re

rand_str = """https://www.youtube.com
http://www.google.com"""


regex = re.compile(r"(https?://([\w.]+))")

print(re.findall(regex, rand_str))
rand_str = re.sub(regex, r"<a href='\1'>\2</a>\n", rand_str)

print(rand_str)
