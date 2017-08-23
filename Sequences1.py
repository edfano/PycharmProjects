xmax=eval(input("Enter Xmax: "))
xmax=xmax+1
for x in range(2,xmax):
    y=x+x-1
    print (('x={} and y={}').format(x,y))
