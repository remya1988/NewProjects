#comp = ["cpu","mouse","keyboard","monitor","Mouse pad"]

#print(comp)
#comp[3:]=["New"]
#print(comp)

#data = [1,2,3,4,5,6,7,8,9,0]
#print(data)
#del data[0:2]
#print(data)
#del data[6:]
#print(data)

#min_val = 2
#max_val = 7
#for index,value in enumerate(data):
#   if (value<min_val) or (value>max_val):
 #       del data[index]
  #      index+=1

data = [4,5,6,101,107,103,110,105,106]
stop = 0
min_val=100
#for index,value in enumerate(data):
    #if value>=min_val:
    #    stop=index
    #    break
#print(stop)
#del data[:stop]
#print(data)
for index,value in enumerate(data):
    if value>stop :
        stop = value
        continue
    else:
        continue

print(stop)


