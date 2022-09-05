"""
def start_decorator(func):
    def wrapper(*args, **kwargs):
        print('start here')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_decorator
def add5(x):
    return x + 5


res = add5(6)
print(res)

"""

