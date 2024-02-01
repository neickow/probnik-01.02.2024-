def f(a, b):
    if a==b:
        return True
    if a>b:
        return False
    if a<b:
        return f(a+3, b)+f(a*2, b)
print(f(12, 96))

