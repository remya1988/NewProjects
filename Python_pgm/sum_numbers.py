def sum_numbers(*value : float) -> float:
    sum = 0
    for num in value:
        sum=sum+num
    return sum

print(sum_numbers(1,2,3))
print(sum_numbers(2.3,7,1.2))