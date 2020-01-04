def combinations(n,m):
    result=1
    ttmp=n-m
    if ttmp>m:
        tmax,tmin=ttmp,m
    else:
        tmax,tmin=m,ttmp
    for i in range(n,0,-1):
        if i>tmax:result*=i
        elif i<tmin:result//=i
    return result

def num(n,max=3):
    sum =0
    for n1 in range(n,n//max,-1):
        if max==2:
            sum+=combinations(n1,n-n1)
            continue
        for n2 in range(n1):
            n3=n-n2-n1
            if n3>n2:
                continue
            elif 0>n3:
                break
            # print(n1,n2,n3)
            sum+=combinations(n1,n2)*combinations(n2,n3)
    return sum

if __name__=='__main__':
    a=[int(i) for i in input("输入楼梯台阶数:").split()]
    b=[int(i) for i in input("输入最多能爬m级台阶").split()]
    max = min(a[0],b[0])
    while max:
        print(num(a[max],b[max]),end=' ')
        max-=1
    print()
