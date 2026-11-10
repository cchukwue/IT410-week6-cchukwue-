# Name: Christopher Chukwuemeka Simeon Okoro
# Course: 26/FA-IT410-V1
# Week 6 - Demo Video: Looping Over Lists

# Create a list of household chores
list_of_chores = ["Take Out Trash", "Wash Dishes", "Cut Grass", "Dust Coffee Table"]

# Loop over a slice of the list (indexes 1 and 2) and print completion status
for chore in list_of_chores[1:3]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")
