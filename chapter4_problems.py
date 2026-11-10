# Name: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Chapter 4 "Try It Yourself" Problems

# Problem 4-1: Loop through four favorite places to visit
favorite_places = ["Kyoto", "Iceland", "Barcelona", "Banff National Park"]
for place in favorite_places:
    print(place + " is a nice place to visit")


# Problem 4-2: Print numbers from 90 to 100 inclusive
for number in range(90, 101):
    print(number)


# Problem 4-3: List of numbers from 100,000 to 1,000,000 and their sum
large_numbers = list(range(100000, 1000001))
print("Sum of numbers from 100,000 to 1,000,000:", sum(large_numbers))


# Problem 4-4: List of 20 unordered numbers with max() and min()
random_numbers = [42, 7, 89, 13, 56, 3, 94, 28, 61, 19, 75, 4, 83, 37, 50, 11, 68, 22, 91, 15]
print("Largest number in the list:", max(random_numbers))
print("Lowest number in the list:", min(random_numbers))


# Problem 4-5: Multiples of 5 between 1 and 100
multiples_of_five = list(range(5, 101, 5))
print("Multiples of 5 between 1 and 100:", multiples_of_five)


# Problem 4-6: Values from 20 to 30 doubled using a list comprehension
base_values = list(range(20, 31))
print("Original values from 20 to 30:", base_values)

doubled_values = [value * 2 for value in base_values]
print("Doubled values:", doubled_values)


# Problem 4-7: Slicing the random_numbers list from Problem 4-4
print("The first 2 values in the list are:", random_numbers[:2])
print("Items 5-10 in the list are:", random_numbers[4:10])
print("The last 4 items in the list are:", random_numbers[-4:])


# Problem 4-8: Copying a list of bands and proving independence
favorite_bands = ["Daft Punk", "Radiohead", "Fleetwood Mac"]
copied_bands = favorite_bands[:]

favorite_bands.append("Tame Impala")

print("Original list of bands:", favorite_bands)
print("Copied list of bands:", copied_bands)


# Problem 4-9: Tuple of school grades and attempting list-style modification
school_grades = ("1st", "2nd", "3rd", "4th", "5th")

# Attempting to modify a tuple raises a TypeError because tuples are immutable
school_grades[0] = "Kindergarten"
