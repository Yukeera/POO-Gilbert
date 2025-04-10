valor = 15
def umaodez (n):
    if(n!=1):
        umaodez(n-1)
    print (f'Número {n}', end = " ")

umaodez(valor)
    