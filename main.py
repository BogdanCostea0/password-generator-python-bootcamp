# password generator
import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(" Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters do you want?"))
nr_symbols = int(input("How many symbols would you like?"))
nr_numbers = int(input("How many numbers would you like?"))

total_length = nr_letters + nr_symbols + nr_numbers

final_password = []
while(len(final_password) != total_length):
    num1 = r.randint(1, 3)
    if num1 == 1:
        num2 = r.randint(0, len(letters)-1)
        final_password.append(letters[num2])
    elif num1 == 2:
        num2 = r.randint(0, len(numbers)-1)
        final_password.append(numbers[num2])
    else:
        num2 = r.randint(0, len(symbols)-1)
        final_password.append(symbols[num2])


password = ''.join([str(item) for item in final_password])  # converting to string

print("Your password is: ", password)


