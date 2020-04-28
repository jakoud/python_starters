def fact(n):
    factorial=1
    for value in range(2,n+1):
        factorial*=value
    return factorial


def taylor_general(list, M, n):
    sum=0
    if M==0:
        return 0
    else:
        for value in range(1,M+1):
            sum+=(((n-1)**value/fact(value)))*list[value]
        return sum


def taylor(M, n):
    sum=0
    if M==0:
        return 0
    else:
        for value in range(1,M+1):
            sum+=(((-1)**(value+1))/value)*(n-1)**value
        return sum


def mapping(sequence_1, sequence_2, N=0):
        for n in range(1,len(sequence_1)+1):
            N+=n
            sum=taylor(sequence_1[n-1], N)
            if sum<n:
                j=0
                while j<sum:
                    sequence_2.append(1)
                    j+=1
                for value in range(j, n):
                    sequence_2.append(0)
            else:
                for value in range (0,n):
                    sequence_2.append(1)
        return "done"


rising=[0,3,20]
typical=[]

mapping(rising, typical)

print(typical)