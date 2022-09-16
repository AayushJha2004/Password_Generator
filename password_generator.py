#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l=""
for a in range(1, nr_letters+1):
  l+=letters[random.randint(0,51)]
s=""
for b in range(1, nr_symbols+1):
  s+=symbols[random.randint(0,8)]
n=""
for c in range(1, nr_numbers+1):
  n+=numbers[random.randint(0,9)]
password=l+s+n
password_1=list(password)
random.shuffle(password_1)
final=''.join(password_1)
print(f"Your custom password is: {final}")
input()
