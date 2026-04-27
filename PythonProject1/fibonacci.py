def fib(limit):
    a,b=0,1
    while a<limit:
        print(a)
        a,b=b,a+b
fib(100)


def fib(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b
    return b
fib(7)