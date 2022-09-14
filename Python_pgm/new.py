shopping_list = ["milk","rice","tomato","jam","jar"]
item_found = None
for item in shopping_list:
    if item=="milk":
        #print("This is milk")
        continue
    elif item == "jam" :
        break

for index in range (len(shopping_list)):
    if shopping_list[index]=="jam" :
        item_found = index
        break
if item_found is not None :

    print("item found on {} position".format(item_found))
else :
    print("item not found")