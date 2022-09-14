print("Choose from the below list : ")
print("1.\tSwimming")
print("2\tDancing")
print("3\tTeaching")
print("0\tExit")

while True:
    choice =input()
    if choice==0:
        break;
    elif choice in "123":
        print("Your choice is {}".format(choice))
        break
    else:
        print("Enter a valid choice ")
        break

