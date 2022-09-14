arr=[40, 23, 7, 49, 32, 98, 76, 48, 87]
for i in range(len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
