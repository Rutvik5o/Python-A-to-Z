# Search for a string in a text file
search_term = input("Enter string to search:")

found = False

with open("temp.py","r") as file:
    for line in file: #reads file line by line
        if search_term in line:
            print("Found->:",line.strip())
            found = True


if not found:
    print("String not found")