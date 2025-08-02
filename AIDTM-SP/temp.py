## Delete list of keys form dict

my_dict = {'a':1,'b':2,'c':3,'d':4}

key_to_remove = ['a','c']

for key in key_to_remove:
    my_dict.pop(key,None)
    #return none & avoid error if key is not found 

print(my_dict)