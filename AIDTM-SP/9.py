## Count Digits & letters in a string using function

def count_text(text):
    digits = sum(c.isdigit() for c in text)
    letters = sum(c.isalpha() for c in text)
    return digits,letters

text = input("Enter String->")
d,l = count_text(text)
print(f"Digits->{d}\nLetters->{l}")