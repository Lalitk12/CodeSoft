# password genrator
import random
import string

def password():
     lenght=int(input("Enter the length of passwor you want "))
     lower=string.ascii_lowercase # print all lower leter
     upper=string.ascii_uppercase
     digit=string.digits
     symbol=string.punctuation

     combin=lower+upper+digit+symbol
     x=random.sample(combin,lenght)
     password="".join(x)
     print(password)
print("Welcome to our Random password Genrator")
while True:
     password()

