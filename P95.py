#File Handling in Python

print("(1) Text File")

f1=open("file_text.txt","r")
data=f1.read()
print(data)



f1=open("file_text1.txt","r+")

print(f1.read())

f1.write("This is python Practice")
f1.close()


##usage of tell function

f1=open("file_text1.txt","r+")

print(f1.tell())

f1.write("Thanks")

print(f1.tell())

print(f1.read())

print(f1.tell())
print("_____________________________________")

print("W++ Mode")

f1=open("file_2.txt","w+")

print(f1.tell())

f1.write("Hi welcome to our ")

print(f1.tell())

f1.write("that python practice")

print(f1.tell())

f1.seek(0)  # file pointer pointing to 0

print(f1.tell())

data=f1.read()

print(data)

print(f1.tell())

f1.close()

print("__________________________________________")


print("a++ -> append = end of the file")

f1=open("file_text.txt","a+")

print(f1.tell())

f1.seek(0)

print(f1.read())

f1.write("Hello Students")



