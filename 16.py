import sys
sys.setrecursionlimit(100000000)
def f(n):
    if n<=2:
        return n
    else:
        return g(n)+f(n-2)
def g(n):
    if n<=2:
        return n
    else:
        return f(n-1)-g(n-2)
print(g(15))
