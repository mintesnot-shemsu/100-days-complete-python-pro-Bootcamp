import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!")
lett=int(input("How many letters would you like in your password: "))
sym=int(input("How many symbols would you like: "))
num=int(input("How many numbers would you lik: "))

pass_comb=[]
for i in range(0,lett):
    chose_letter= random.choice(letters)
    pass_comb.append(chose_letter)

for i in range(0, sym):
    chose_symbol=random.choice(symbols)
    pass_comb.append(chose_symbol)

for i in range(0, num):
    chose_number=random.choice(numbers)
    pass_comb.append(chose_number)

password=""
for char in pass_comb:
    password+=char
print(f"your passowrd is: {password}")

random.shuffle(pass_comb)
pas=""
for char in pass_comb:
    pas+=char
print(f"randomized passowrd : {pas}")


