def fibo(n):
    f_0 = 0
    f_1 = 1
    
    if n == 0:
        return f_0
    elif n == 1:
        return f_1
    else:
        return fibo(n - 1) + fibo(n - 2)

for i in range(12):
    print(i,fibo(i))