## Take values from user, count total & occurrences

elements = input("Enter element sepearted by space:").split()

print("Total Elements-> ",elements)

for item in set(elements):
    #set() removes duplicates so we check each item only occure at once
    print(f"{item} occures {elements.count(item)} times")
