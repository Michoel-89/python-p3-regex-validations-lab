import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"(?![a-z])(?!.*\d)(?!.*\s\s)[A-Za-z\s'-]+"
name_regex = re.compile(name)


phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)



email_address = r"^[A-Za-z]+[\w.]*@[A-Za-z]+\.[A-Za-z]+$"
email_regex = re.compile(email_address)

