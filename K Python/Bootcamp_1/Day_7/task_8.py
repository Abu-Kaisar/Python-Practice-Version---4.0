import re

rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"


regex = re.compile(r"[\w.+-]*@[\w.+-]*\.[\w.]*")
match = re.findall(regex, rand_str)
print(match)
