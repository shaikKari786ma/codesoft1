import random 
import string
all_character=string.punctuation+string.digits+string.ascii_letters
print(all_character)
n=int(input("enter the length of password:"))
password=""
for i in range(n):
    password+=random.choice(all_character)
print("  generated password  " + password)


