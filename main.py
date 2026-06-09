import random
import string
all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%"
password = ""
enter = int(input("Enter the number of characters in the password (number):"))
for i in range(enter):
    random_char = random.choice(all_chars)
    password = password + random_char
print("Your unique password:" + password)
