a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1

for i in range(1,max(a,b)):
    if a%i==0 and b%i==0:
        hcf=i
lcm= (a*b)//hcf
print(lcm,hcf)