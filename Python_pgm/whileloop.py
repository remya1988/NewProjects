dir_ext = ["east" , "west" , "north" ,"south"]
founds = ""
while founds not in dir_ext :
    founds = input("Enter a direction ? ")
    if founds.casefold() == "no":
        print("No here")
        break
print("You are right here .....")
for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        break

