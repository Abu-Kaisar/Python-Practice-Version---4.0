import re

regex = re.compile(r"[\w_\.%+-]{1,20}@[\w\.-]{1,20}\.[A-Za-z]{2,3}")

email_List = "db@aol.com m@.com @apple.com db@.com"

print(re.findall(regex, email_List))
