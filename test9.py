# Given k numbers which are less than n, return the set of prime number among them
n = 35

def busco():
    lista = []
    if n>1:
        for i in range(2,n):
            if (n % i)==0:
                lista.append[i]
            else:
                print('No es primo')
        return lista
    else:
        print('Es muy chico el numero')

   
