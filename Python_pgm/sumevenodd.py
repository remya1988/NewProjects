def sum_eo(n,t):
    sum = 0
    if t=='e':
        num=2
    elif t=='o':
        num=1
    else:
        return -1

    for i in range(num,n,2):
        sum+=i
    return sum





n = int(input("Enter a range number : "))
t = input("Enter a string e for even and o for odd  : ")
sum =  sum_eo(n,t)
if sum == -1:
    print("Invalid entry")
else:
    print("Sum of numbers upto {} is {}".format(n,sum))





