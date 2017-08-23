__author__ = 'eduardo.fano'



def factor_n():
    L=[]
    n=int(input("Enter a number"))
    # L.append(n)
    for i in range(1, n+1):
        if(n%i==0):
            L.append(i)

    print(L)
    # return L

factor_n()