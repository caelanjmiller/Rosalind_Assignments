#Given two positive integers a and b (a < b < 10_000)
#Return the sum of all integers from a & b, inclusively

def summation(a,b):
    a = int(a)
    b = int(b)
    sum = 0
    numbers = [x for x in range(a,b+1)]
    for number in numbers:
        if number % 2 != 0:
            sum += number 
    print(f"Total sum from all numbers between {a} & {b}: {sum}")

summation(4703,9568)