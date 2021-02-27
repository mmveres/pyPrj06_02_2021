# n! = n * (n-1)!       5! = 5*4*3*2*1

def fact_iter(n):
    if n == 1 or n == 0:
        return 1
    x = 1
    for i in range(2,n+1):
        x*=i
    return x

def fact_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * fact_rec(n-1)

# fib(n) = fib(n-1)+fib(n-2)
def fib_rec(n):
    if n== 1 or n==0:
        return 1
    print(n)
    return fib_rec(n-1)+fib_rec(n-2)

def fib_iter(n):
    if n == 1 or n == 0:
        return 1
    x=1
    y=1
    z=1
    for i in range(2,n+1):
        z = y+x
        x= y
        y= z
        print(z)
    return z

if __name__ == '__main__':
    print(fact_iter(5))
    print(fact_rec(5))
    print("*****")
    print(fib_rec(10))
    print("*****")
    print(fib_iter(10))