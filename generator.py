def fibo(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


s = fibo(30)

# for i in s:
#     print(i)


mygen = (i for i in range(10) if i % 2 == 0)

for i in mygen:
    print(i)
