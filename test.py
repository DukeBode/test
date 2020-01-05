def combinations(n,m):
    result = 1
    for i in range(min(n-m,m)):
        result=result*(n-i)//(i+1)
    return result

def num(n,max):
    sum=1
    for m in range(n//max,n):
        if max*m<n:
            continue
        for i in range(1,m+1):
            if i*(max-1)<n-m:
                continue
            if n-m<i:
                break
            sum+=combinations(m,i)*combinations(i,n-m-i)
    return sum

if __name__=='__main__':
    a=[int(i) for i in input("输入楼梯台阶数:").split()]
    b=[int(i) for i in input("输入最多能爬m级台阶").split()]
    max = min(a[0],b[0])
    while max:
        print(num(a[-max],b[-max]),end=' ')
        max-=1
    print()
