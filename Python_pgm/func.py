def func(p1, p2, *args, k, **kwargs):
    print("Positional argumetns............. : {} {}".format(p1,p2))
    print("Variable arguments (*args)....... : {}".format(args) )
    print("key argumets..................... : {}".format(k))
    print("Variable keywords................ : {}".format(kwargs))

func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)