#bai1
def checktamgiac(a,b,c):
    if a==b and a==c and b==c:
        print("Tam giác đều")
    elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
        print("tam giác cân")
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
        print("Tam giác vuông")
    elif a>b+c or b>c+a or c>a+b:
        print("Không phải tam giác")
    else:
        print("Tam giác thường")
    #Bài 2
def bai2(n):
    a=[]
    for i in range(2,n+1):
        while n%i==0:
            a.append(i)
            n=n//i
    return a  
#Bài 3
def bai3(n):
    list=[]
    for i in range(n+1):
        a=n-i
        list.append([i,a])
    return list
print(bai3(7))
#Bài 4
def bai4(n):
    if n%3==0:
        return n//3 + 1,n//3,n//3 -1
    else:
        return "Không phân tích được"
print(bai4(18))
#Bài 5
def bai5(n):
    ans=0
    while n%10==0:
        ans=ans+1
        ans=ans/10
    return ans
print(bai5(10000))
#Bài 6
def bai6(n):
    



         
