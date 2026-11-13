import random
import string

length = int(input("How long password? "))
letters = string.ascii_letters + string.digits + "!@#$%"
password = ""

for i in range(length):
    password += random.choice(letters)

print("Your password is:", password)
