name = input("Enter your name : ")
age=int(input("Enter your age {0} : ".format(name)))
print("""Name : {0} 
 Age : {1:4}""".format(name,age))

if age>=18:
    print("You are old enough to vote")
else:
    print("Come back after {0} years ".format(18-age))