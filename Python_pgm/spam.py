menu = [
    ["rive","jam","spam"],
    ["jam","lever","chicken"],
    ["spam","chicken"],
    ["egg","milk"],
]

for meal in menu:

        for ch in range(len(meal)-1,-1,-1) :
            if meal[ch] == "spam":
               del meal[ch]


        print(meal)