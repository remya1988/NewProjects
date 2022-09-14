def fib(n: int):
    n1 = 0
    n2 = 1

    n3 = 0
    """
    for i in range(n: int):
        print(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3
    """
    list1 = []
    for i in range(n):
        list1.append(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3
    print(list1)



fib(10)