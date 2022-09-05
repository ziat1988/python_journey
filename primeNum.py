
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


for number in range(2, 251):
    numCheck = isPrime(number)
    if numCheck:
        print(number)
