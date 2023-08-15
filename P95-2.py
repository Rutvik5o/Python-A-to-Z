print("Binary File")

f1=open("testing.jpg","rb")
f2=open("testing2.jpg","wb")

for i in f1:
    f2.write(i)


#print(f1.read())