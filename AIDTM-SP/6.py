## Copy content from one file to another

with open("5.py","r") as src:
    content = src.read()

with open("temp.py","w") as dest:
    dest.write(content)

