import timeit

def a():
    return 1+1

print(timeit.timeit(a, number=1000000))