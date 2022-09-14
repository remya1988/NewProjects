number = 5
print("Please enter a number between 1 and 10 :")
guess= int(input())

if guess != number :
    if guess < number :
        print("Enter higher number :")
        guess= int(input())
        if guess == number :
            print("You entered correct answer ")
        else :
            print("Enter right number ")
    else :
        print("Enter a lower number")
        guess= int(input())
        if guess == number :
            print("You entered correct answer ")
        else :
            print("Please enter the right number ")
else :
    print("You entered correct number ")