name = {
    'rem':{
        'phone':'1123123123',
        'age':12
    },
    'raj':{
        'phone':'24325435',
        'age':23
    }
}
print(name['rem']['phone'])
k={}.fromkeys(['name','age','email'],'unknown')
print(sorted(k.keys()))
print(name.items())