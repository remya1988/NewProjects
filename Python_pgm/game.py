import random
hs=10
ans= random.randint(1,hs)
gues=int(input("Enter a number between 1 and {}").format(hs))
if gues==ans:
    print("U are correct")
    print(ans)
else :
    print("Enter correct guess")
    print(ans)
