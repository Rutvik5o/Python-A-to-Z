#Remove Empty items from list to strings

str_list = ["apple","","ban ana","","cherry"," "]


cleaned = [s for s in str_list if s.strip()]

print(cleaned)

#s.strip() remove whitespace, if result is non-empty, keep it

