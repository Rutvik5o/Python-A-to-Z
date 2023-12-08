# Using Magic/Dunder 
# these are not being called explicity by own based on your actions these are called implicity.

class Author:
    
    def __init__(self,name,book_name,pages):

        self.name=name
        self.book_name=book_name
        self.pages=pages


    def __str__(self):

        return f" {self.book_name} by {self.name} "
    
    def __len__(self):

        return self.pages
    
    def __call__ (self,*args,**kwargs):

        print("Hello Welcome to our Calling Direct Object")

    def __del__(self):

        print("Succesfully Deleted")
    

Obj=Author("PataNahi","MaineNahiLikhih",300)

print(Obj)

Obj()

del Obj

print(dir(int))  #-> For check how many dunder method on int class

print(Obj)


