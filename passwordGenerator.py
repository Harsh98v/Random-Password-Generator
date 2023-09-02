#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("This is the simple password, without any randomisation in order!")

ez_password = ""

#Choosing the letters
for i in range(0, nr_letters):
  j = random.randint(0, len(letters) - 1)
  ez_password = ez_password + letters[j]

#Choosing the symbols
for i in range(0, nr_symbols):
  j = random.randint(0, len(symbols) - 1)
  ez_password = ez_password + symbols[j]

#Choosing the numbers
for i in range(0, nr_numbers):
  j = random.randint(0, len(numbers) - 1)
  ez_password = ez_password + numbers[j]

print("Your password is: " + ez_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("This is the hard password, with randomisation in order!")

hard_password = ""

total_length = nr_letters + nr_symbols + nr_numbers

letter_count = nr_letters
number_count = nr_numbers
symbol_count = nr_symbols

while(len(hard_password) != total_length):
  cat_choice = random.randint(0, 2) #category choice(letters, numbers or symbols)
  if cat_choice == 0 and letter_count != 0: #letters
    j = random.randint(0, len(letters) - 1)
    hard_password = hard_password + letters[j]
    letter_count -= 1
    
  elif cat_choice == 1 and number_count != 0: #numbers
    j = random.randint(0, len(numbers) - 1)
    hard_password = hard_password + numbers[j]
    number_count -= 1
    
  elif cat_choice == 2 and symbol_count != 0: #symbols
    j = random.randint(0, len(symbols) - 1)
    hard_password = hard_password + symbols[j]
    symbol_count -= 1
    
print("Your password is: " + hard_password)
