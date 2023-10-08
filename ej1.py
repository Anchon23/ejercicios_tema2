n = 0
def sumar(n):
    if n<=0:
        return 0
    else:
        return n + sumar(n-1)
    
print(sumar(10))