import random

while True:
    v=[]
    vn=[]
    n=random.randint(1111111,9999999)
    s=str(n)
    for i in s:
        v.append(i)
        vn.append(int(i))

    a=(vn[0]+vn[2]+vn[4]+vn[6])*3
    b=(vn[1]+vn[3]+vn[5])
    c=a+b
    mul_of_10=((c//10)+1)*10
    check_digit=mul_of_10-c

    if (check_digit==9):break



print(vn)
print(v)
print(a)
print(b)
print(c)
print(mul_of_10)
print("For check digit:{} the number is:{}".format(check_digit,n))
print(end='\n')
num=str(n)+'9'
print("8 DIGITS NUMBER TO SCAN:------>{}".format(num))