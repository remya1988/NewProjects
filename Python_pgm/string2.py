parr= "hello youdfdf"
print(parr)
print(parr[1])

print(parr[:8])
print(parr[8:])
print(parr[:])
letters="abcdefghijklmnopqrstuvwxyz"
print(parr[-4:-1])
print(parr[-4: 11])
#for i in range(0,13):
#    print(parr[i-13])
numb="1,226;372:036 854,775;807"
print(numb[1::4])
sep=numb[1::4]
values="".join(char if char not in sep else " " for char in numb).split()
print([int(val) for val in values])
#seperators=num[1::4]
#print(seperators)