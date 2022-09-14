class Player:
    name=''
    health=100
    hit_pow=5
    def attack(self,obj):
        obj.health-=self.hit_pow
        print(" %s attacked %s health is : %d" %(self.name,obj.name,obj.health))

class Hero(Player):
    health=200
    hit_pow=25

class Villain(Player):
    health=200
    hit_pow=20

kunj = Hero()
kunj.name='Kunjali Marakkar'

gama = Villain()
gama.name='Gama'

kunj.attack(gama)
gama.attack(kunj)