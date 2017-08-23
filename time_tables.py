
'''Program to ask the user to enter three int numbers and calculate/display the time tables (1 to 10) for each value.
'''
n=10
def xtable():
    (n1,n2,n3)=input("Enter 3 INT Numbers: ").split()
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    L1=[];L2=[];L3=[]

    for i in range(1,n+1):
        L1.append(n1*i)
        L2.append(n2*i)
        L3.append(n3*i)

    print("Time table for {} is {}".format(n1,L1))
    print("Time table for {} is {}".format(n2, L2))
    print("Time table for {} is {}".format(n3, L3))

    # Now here printing in 3 columns format:
    print("\n\n#\t\t{}X\t\t{}X\t\t{}X\t\t\n".format(n1,n2,n3))
    for i in range(n):
        print("{}\t\t{}\t\t{}\t\t{}\n".format(i,L1[i],L2[i],L3[i]))

xtable()