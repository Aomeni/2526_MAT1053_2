def bai2(n):
    a=[]
    for i in range(2,n+1):
        while n%i==0:
            a.append(i)
            n=n//i
    return a
n=int(input())
print(bai2(n))  