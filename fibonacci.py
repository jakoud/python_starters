def fibo(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
def print_sequence(n):
    for value in range(n):
        print(fibo(value))

def print_value(n):
    print(fibo(n))