even=[2,4,6,8]
odd=[1,3,5,7,9]

even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)

part=["comp","mouse","cpu","keyboard","abc"]
part.sort(reverse=True)
print(part)

tex = "This is my new test"
tx = sorted(tex,key = str.casefold)
print(tx)