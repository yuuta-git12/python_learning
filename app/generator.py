# ジェネレーターについての補足学習用

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci2():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b


for i in range(55):
    print(fibonacci(i))
    if i == 55:
        break


for i in fibonacci2():
    print(i)
    if i == 55:
        break
    

def fibonacci3(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, b+a