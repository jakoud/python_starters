from random import randint

N=int(input('podaj rozmiar tablicy: '))
tab=[]
for value in range(N):
    tab.append(randint(1, 10))
print(tab)
counter=0

for value in range(N-2):
    if (tab[value]<tab[value+1] and tab[value+1]>=tab[value+2]):
        counter+=1
    
print(counter)
triplets=[0,0,0]

for value in range(N-2):
    if (tab[value]<tab[value+1] and tab[value+1]>=tab[value+2]):
        triplets[0]=tab[value]
        triplets[1]=tab[value+1]
        triplets[2]=tab[value+2]
        print(triplets)
       
def search(list, value):
    licznik=0
    for item in list:
        if item==value:
            licznik+=1
    if(licznik==0):
        print('nie ma mnie na tej liście')
    else:
        print('pojawiam się na tej liście %d razy'%licznik)
        
search(tab, 10)