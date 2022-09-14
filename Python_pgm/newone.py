shopping_list = ["rice",
                 "tomato",
                 "jam",
                 "egg",
                 "bread"]

for i in range(0,len(shopping_list)):
    print(shopping_list[i])
print("***************")
print(id(shopping_list))



shopping_list += ["beas"]

print(id(shopping_list))

a = b = c = d = e = shopping_list
print(a)

b.append("cream")
print(d)
print(e)
print(a)