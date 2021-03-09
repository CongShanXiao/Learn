n = 0
while n < 11:
    print(n)
    n += 1
#斐波那契数列：前两项为1，之后的每一项都是前两项之和
print('%' * 50)
a,b = 0,1
while b<100:
    print(b)
    a,b = b,a+b
#乘法表
for i in range(1,10):
    for j in range(1,1+i):
        print("%d*%d=%2d"%(i,j,i*j),"","",end="")
    print("")