from multiplication_persistency import per
from matplotlib import pyplot

persistency=[]

for i in range(1000):
    persistency.append(per(i,0))
    
arguments=[i for i in range(1000)]

pyplot.scatter(arguments, persistency, s=10, c=persistency, cmap=pyplot.cm.Blues)