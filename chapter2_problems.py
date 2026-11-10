# Name: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Chapter 2 "Try It Yourself" Problems

# Problem 2-1: Restaurant and favorite dish variables
favorite_item = "The Cheesecake Factory"
print(favorite_item)

favorite_item = "Chicken Madeira"
print(favorite_item)


# Problem 2-2: Store purchase concatenation
last_store = "Target"
purchased_item = "wireless mouse"
print("The last time I went to " + last_store + ", I purchased a " + purchased_item + ".")


# Problem 2-3: Case methods on a car name
favorite_car = "Ford Mustang"
print(favorite_car.lower())
print(favorite_car.upper())
print(favorite_car.title())


# Problem 2-4: Whitespace characters and stripping methods
favorite_quote = "Stay hungry, stay foolish."
formatted_quote = "\t\n" + favorite_quote + "\t\n"

print("Original quote with whitespace:")
print(formatted_quote)

print("Quote after lstrip():")
print(formatted_quote.lstrip())

print("Quote after strip():")
print(formatted_quote.strip())


# Problem 2-5: Arithmetic calculation and string conversion
math_result = 12 * 4
print("The result of my math problem is: " + str(math_result) + ".")
