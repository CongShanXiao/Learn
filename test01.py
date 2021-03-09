print("Hello World")
N = 10
sum = 0
count = 0
print("请输入10个数字:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
average = sum/N
print("N = {},sum = {}".format(N,sum))
print("averager = {:.2f}".format(average))