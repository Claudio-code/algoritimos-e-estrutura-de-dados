def pot2(x):
    return x**2

pot2_ = lambda x: x**2


# print(pot2(2))
# print(pot2_(22))

## fatorial

def fatorial(n):
    if (n == 0):
        return 1
    return (n * fatorial(n - 1))

fatorial_ = lambda n: n * fatorial(n - 1) if n > 1 else 1

print(fatorial_(3))