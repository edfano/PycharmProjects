import random


v=[]
vn=[]
n=random.randint(c
for i in str(n):
    v.append(i)
    vn.append(int(i))

a=(vn[0]+vn[2]+vn[4]+vn[6])*3
b=(vn[1]+vn[3]+vn[5]+vn[7])
c=a+b
mul_of_10=((c//10)+1)*10
check_digit=mul_of_10-c

if (check_digit==9):print("XXXXXXXXXX945869056893568039568096XXX")



print(vn)
print(v)
print("a={}, b={}, c={}, mul_of_10={}, check_digit={}".format(a,b,c,mul_of_10,check_digit))
#print("For check digit:{} the number is:{}".format(check_digit,n))