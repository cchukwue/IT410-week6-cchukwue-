# Author: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Working with Lists Assignment

# Requirement 1: Create a list of courses taken at Walsh College in all lowercase
walsh_courses = ["it405", "it410", "it408"]

# Requirement 2: Sort the list and print each course in uppercase with a message
walsh_courses.sort()
for course in walsh_courses:
    print("I have taken " + course.upper() + " at Walsh College.")

# Requirement 3: Add upcoming courses, re-sort, and print each element
walsh_courses.append("it412")
walsh_courses.append("it414")
walsh_courses.sort()

print("This is my course of study with upcoming courses added:")
for course in walsh_courses:
    print(course)

# Requirement 4: Remove previously taken courses and print each removed course
print("I do not have to take these courses:")
removed_course_1 = walsh_courses.pop(0)
print(removed_course_1)
removed_course_2 = walsh_courses.pop(0)
print(removed_course_2)
removed_course_3 = walsh_courses.pop(0)
print(removed_course_3)

# Requirement 5: Print remaining upcoming courses each on its own line
print("I plan to take the following courses next term")
for course in walsh_courses:
    print(course)

# Requirement 6: Create a list of numbers from 1 to 1000 divisible by 6
divisible_by_six = list(range(6, 1001, 6))

# Requirement 7: Print the first 20 numbers in the list each on its own line
print("Here are twenty numbers divisible by 6.")
for number in divisible_by_six[:20]:
    print(number)

# Requirement 8: Calculate and store the maximum value of the large list
max_number = max(divisible_by_six)

# Requirement 9: Print the maximum value with the required message
print("The maximum value in the list is: " + str(max_number))

# Requirement 10: Sum values between the 10th value (index 9) and 50th value (index 49)
partial_sum = sum(divisible_by_six[9:50])
print("Here is the sum of several values in the list: " + str(partial_sum))

# Requirement 11: Overwrite the original courses variable with the large numbers list
walsh_courses = divisible_by_six
