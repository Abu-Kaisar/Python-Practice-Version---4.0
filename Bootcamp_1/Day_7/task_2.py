import re

#block one

rand_str = "F.B.I. C.I.A. I.S.R. CID"

print("matches :", len(re.findall(".\..\..\.", rand_str)))

#block two

rand_long_str = """This a very long
lovely also a very wide
kind of line which is
actually larger than usual one but
kinda bigger"""

print(rand_long_str)
regex = re.compile("\n")
rand_long_str = regex.sub(" ", rand_long_str)
print(rand_long_str)
# \b \f \r \t \v \r\n


#block three
num_str = "1234567890"
print("matches", len(re.findall("\d", num_str)))

num_str = "123456"
if re.findall("\d{6}", num_str):
    print("Special Zip Code")

num_str = "12 123 1234 12345 123456 1234567 12345678"
print("Matches:", len(re.findall("\d{4,7}", num_str)))


#block four
ph_num = "017-18-720639"
if re.search("\w{3}-\w{2}-\w{6}", ph_num):
    print("Valid BD Number!!")
