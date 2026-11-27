# Lab 4 · About me: data types, input() and converting
# Example answers: Amina | Abuja | 22 | 1.65

name = input("What is your name? ")
city = input("Which city do you live in? ")
age = int(input("How old are you? "))            # int: a whole number
height = float(input("How tall are you in metres? "))   # float: a decimal

is_adult = age >= 18                              # bool: True or False

print(f"Nice to meet you, {name} from {city}!")
print(f"In 5 years you will be {age + 5}.")
print(f"Your height in centimetres: {height * 100}")
print(f"Adult? {is_adult}")
print("Types:", type(name), type(age), type(height), type(is_adult))
