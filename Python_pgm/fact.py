def factorial(number :int):
    fact = 1
    if number==0:
        return 0


    for i in range(1,number+1):
        fact =fact*i

    return fact
print("Factorial of numbers upto 35")
for i in range(36):

    print("{} ! = {}".format(i,factorial(i)))
