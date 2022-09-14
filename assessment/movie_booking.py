class Theatre:
    def set_screen(self):
        self.screen1=" 1 : Screen 1"
        self.screen2=" 2 : Screen 2"
        self.screen3=" 3 : Screen 3"
    def print_screen(self):
        print(self.screen1,self.screen2,self.screen3)



class MovieDisplay(Theatre):
    def select_movie(self):
        super().set_screen()
        super().print_screen()
        scr = int(input("Enter the number of  screen(1,2,3) : "))
        return scr

class Movies(MovieDisplay):
    def display_movie(self,n):
        if(n==1):
            print("The movie running in screen 1 is MOVIE1")
        elif n==2:
            print("The movie running in screen 2 is MOVIE2")
        elif n==3:
            print("The movie running in screen 3 is MOVIE3")

class Timing(MovieDisplay):
    def display_timing(self,n):
        if (n == 1):
            print("Timing 10.00 - 1.00 ")
        elif n == 2:
            print("Timing 2.00 - 4.00 ")
        elif n == 3:
            print("Timing 6.00 -8.00 ")


md = MovieDisplay()
scr = md.select_movie()
mv = Movies()
mv.display_movie(scr)
tm=Timing()
tm.display_timing(scr)