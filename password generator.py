import string
import random

# alphabets, digits and special characters
Small_alphabets = string.ascii_lowercase
Cap_alphabets = string.ascii_uppercase
digits = string.digits
sp_characters = string.punctuation

length = int(input("Enter the length of password: "))

# concadination of all the characters
password = list(Small_alphabets + Cap_alphabets + digits + sp_characters)
print("Your password is: ")
print("".join(random.sample(password, length)))

