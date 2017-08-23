H=[1,2]
W=[1,3]

h=int(input('Enter H of the Pyramid'))

for i in range(2,h+1):

    H.append(i+1)
    W.append(i+3)
    print("i={} || h={} || w={}".format(i ,H[i], W[i]))

print(H, end='\n')


'''    if ((H.index(i)==0) and (W.index(i)==0)): H.append(1);W.append(1)
    if ((H.index(i) == 1) and (W.index(i) == 1)): H.append(2);W.append(3)'''