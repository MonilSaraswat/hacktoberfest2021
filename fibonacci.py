# 0 1 1 2 3 5 8 13
"""a , b = 0 , 1
n = int(input("Enter Number of Terms"))
print(a,b , end = " ")
for x in range(1 , n-1):
    temp = a+b
    a=b
    b=temp
    print(temp , end = " ")
"""
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

n = int(input("Enter the end term"))
fibonacci(n)

3
