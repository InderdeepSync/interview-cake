

cache = {}

def fib_efficient(n):
    if n in cache:
        return cache[n]

    cache[n] = fib(n)
    return cache[n]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_efficient(n - 1) + fib_efficient(n - 2)






if __name__ == "__main__":
    print(fib_efficient(5))