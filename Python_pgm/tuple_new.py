metalica = "tim","had","new",2020
print(metalica)
print(metalica[1])
metalica2= list(metalica)

print(metalica2)
metalica2[1] = "jim"
print((metalica2))

data = 1,2,3
x,y,z=data
result=x+y+z
print(result)
data_list = [11,1,13]
a,b,c = data_list
print(a,b,c)
data_list.append(15)
print(data_list)

for index,char in enumerate("abcdefg"):
    print("Index : {0}  Character : {1}".format(index,char))
for s in enumerate("abcdefgh"):
    print(s)
