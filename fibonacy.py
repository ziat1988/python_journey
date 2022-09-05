# Annonce: print n number of serie fibonacy
# 1 1 2 3 5 8 13 21 34

def fib1(n):
    first = 0
    second = 1

    for i in range(n):  # 0 -> n-1
        print(second)
        temp = second
        second += first
        first = temp


# fib(8)


# Variant 2 : find the n-th of serie fibo
def fib2(n):
    first = 0
    second = 1

    for i in range(n):  # 0 -> n-1
        if i == n - 1:
            print(second)
        temp = second
        second += first
        first = temp


#####################################
### Variant 3: Recursive return resultat of nth element in serie
# fib(3) = fib(2) + fib(1)
def fib_res(n):
    if n <= 2:
        return 1

    a = fib_res(n - 1)
    print(a)
    b = fib_res(n - 2)
    print(b)
    t = a+b

    return t


x = fib_res(8)
print(x)

### Variant 4 : print out n serie


