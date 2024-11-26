import random

print("Welcome to the PyPassword Generator!")
total = int(input("How many letter would you linke in your password: "))
symbols = int(input("How many symbols would you like: "))
num = int(input("How many numbers would you like: "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

def choice(qtd, lista):
  for x in range(qtd):
    password.append(random.choice(lista))
    
choice(total, letters)
choice(symbols, sym)
choice(num, numbers)

random.shuffle(password)
password = "".join(password)

print(f"Your passowrd: {password}")
