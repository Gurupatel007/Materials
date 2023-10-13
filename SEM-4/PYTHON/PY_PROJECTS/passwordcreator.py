import random
characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_'

pass_length=int(input("Enter the length of required password: "))
pass_count=int(input("Enter the no. of passwords required: "))

for i in range(pass_count):
    password=" "
    for i in range(pass_length):
        pass_char=random.choice(characters)
        password+=pass_char
    print("the generated password is: ",password)