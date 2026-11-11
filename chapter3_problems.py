# Name: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Chapter 3 "Try It Yourself" Questions

# Problem 3-1: List of 4 books printed individually in title case without loops
original_books = ["dune", "project hail mary", "the hobbit", "1984"]
print("I just read: " + recent_books[0].title())
print("I just read: " + recent_books[1].title())
print("I just read: " + recent_books[2].title())
print("I just read: " + recent_books[3].title())


# Problem 3-2: Modifying, adding, and removing TV shows in a list
tv_shows = ["Severance", "The Bear", "Stranger Things", "Abbott Elementary"]

# Swap a cancelled show with a new show
tv_shows[1] = "Slow Horses"

# Add one show using append() and one in the middle using insert()
tv_shows.append("The Last of Us")
tv_shows.insert(2, "Only Murders in the Building")

# Remove the last item using pop() and print it out
removed_show = tv_shows.pop()
print("Removed show: " + removed_show)

# Use del statements to remove the first three shows from the list
del tv_shows[0]
del tv_shows[0]
del tv_shows[0]

# Print whatever is left in the list
print("Remaining shows:", tv_shows)


# Problem 3-3: Using len(), sort(), sorted(), and reverse()
travel_cities = ["Tokyo", "Madrid", "Chicago", "Sydney", "Toronto"]
print("Number of cities in list:", len(travel_cities))
print("Temporarily sorted list:", sorted(travel_cities))

travel_cities.sort()
print("Permanently sorted list:", travel_cities)

travel_cities.reverse()
print("Reversed list:", travel_cities)


# Problem 3-4: Intentional IndexError with commented fix underneath
primary_colors = ["red", "blue", "green"]

# Intentional indexing error (valid indexes are 0, 1, and 2)
print(primary_colors[3])

# Solution for the above indexing bug:
# print(primary_colors[2])
