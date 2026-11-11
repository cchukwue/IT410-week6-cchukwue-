# Author: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Variables and Simple Data Types Assignment

# 1. Store first name in all lowercase and last name in all uppercase
first_name = "christopher"
last_name = "OKORO"

# 2. Print greeting with first name in uppercase and last name in lowercase
print("Hello, " + first_name.upper() + " " + last_name.lower())

# 3. Print out two newlines
print("\n\n")

# 4. Print the quote with double quotes at the beginning and end
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")

# 5. Store 2 decimal numbers as variables
decimal_one = 12.5
decimal_two = 2.5

# 6. Store addition, subtraction, multiplication, and division operations as variables
addition_result = decimal_one + decimal_two
subtraction_result = decimal_one - decimal_two
multiplication_result = decimal_one * decimal_two
division_result = decimal_one / decimal_two

# 7. Print each of the four results on its own line
print(str(decimal_one) + " plus " + str(decimal_two) + " equals " + str(addition_result))
print(str(decimal_one) + " minus " + str(decimal_two) + " equals " + str(subtraction_result))
print(str(decimal_one) + " times " + str(decimal_two) + " equals " + str(multiplication_result))
print(str(decimal_one) + " divided by " + str(decimal_two) + " equals " + str(division_result))

# 8. Store current month as a string variable and day of the month as a numeric variable
current_month = "November"
day_of_month = 11

# 9. Output date message on a new line and tabbed over two times
print("\n\t\tToday is day " + str(day_of_month) + " of the month of " + current_month + ".")
