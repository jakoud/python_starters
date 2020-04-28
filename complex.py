class zespolona():
    def __init__(self, re, im):
        self.re=re
        self.im=im
    
    def add(zespolona_1, zespolona_2):
        zespolona_3=zespolona(zespolona_1.re+zespolona_2.re, zespolona_1.im+zespolona_2.im)
        return zespolona_3
    
    def print(self):
        print(str(self.re)+'+'+str(self.im)+'i')
    
    def multi(zespolona_1, zespolona_2):
        zespolona_3=zespolona(zespolona_1.re*zespolona_2.re-zespolona_1.im*zespolona_2.im, zespolona_1.re*zespolona_2.im+zespolona_1.im*zespolona_2.re)
        return zespolona_3
    
    def square(zespolona_1):
        zespolona_2=zespolona.multi(zespolona_1, zespolona_1)
        return zespolona_2
    

x=zespolona(1, 2)
zespolona.print(x)
y=zespolona(2, 3)
w=zespolona.multi(x,y)
z=zespolona.add(x,y)
c=zespolona.square(x)
zespolona.print(z)
zespolona.print(w)
zespolona.print(c)