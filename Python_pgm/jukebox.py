from test import albums

print("JUKEBOX MENU PROGRAM")
print("1.Welcome to my Nightmare")
print("2.Bad Company")
print("3.Nightflight")
print("4.More Mayhem")
print("Enter your album ?")
ch=input()

for song in albums :
    song=albums[int(ch)][3]
    if ch!=0:
        for i in range (len(song)):
            print(song[i])
        sn=input("Enter the song choice ? ")
        print("You are playing the song {}".format(song[int(sn)-1][1]))
        break
