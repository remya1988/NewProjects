A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print("A0:",A0)
print("***********")
print("A1:",A1)
print("***********")
print("A2:",A2)
print("***********")
print("A3:",A3)
print("***********")
print("A4:",A4)
print("***********")
print("A5:",A5)
print("***********")
print("A6:",A6)
