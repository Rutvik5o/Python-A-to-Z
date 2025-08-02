## Generate even numbers b/w 10 & 30 using function

def gen_even():
    return [i for i in range(10,31) if i % 2 ==0]

print(gen_even())