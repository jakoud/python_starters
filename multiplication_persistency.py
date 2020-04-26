def per(n, steps):
    if len(str(n))==1:
        return steps
    result=1
    digits=[int(i) for i in str(n)]
    for j in digits:
        result*=j
    steps+=1
    return per(result, steps)
    
addition_persistency={}
    
for i in range(100):
    steps=per(i,0)
    addition_persistency[i]=steps

for key, value in sorted(addition_persistency.items(), key= lambda x:x[1]):
    print(str(key)+', '+ str(value))