def move(s, a, t, n):
    if n == 1:
        print(f'move from {s} to {t}')
        return
    move(s, t, a, n - 1)
    print(f'move from {s} to {t}')
    move(a, s, t, n - 1)


move('A', 'B', 'C', 3)

'''

move n-1 from source to aux
move n from source to target
move n-1 from aux to target

def countdown(i):
    print(i)
    if i <= 0:  # Base case
        return
    else:  # Recursive case
        countdown(i - 1)

#countdown(3)

2 disc:
disc go from source to aux
disc go from source to target
disc go from aux to target

3 disc
disc go from source to target
disc go from source to aux
disc go from target to aux
disc go from source to target

disc go from aux to source
disc go from aux to target
disc go from source to target


'''
