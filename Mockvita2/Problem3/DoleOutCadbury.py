def cadbury(l,b):
    count = 0
    while True:
        lon=max(l,b)
        sh=min(l,b)
        count+=1
        diff=lon-sh
        if diff==0:
            return count
        else :
            l=min(l,b)
            b=diff
minl=int(input())
maxl=int(input())
minw=int(input())
maxw=int(input())
count=0
for i in range(minl,maxl+1):
    for j in range(minw,maxw+1):
        count+=cadbury(i,j)
print(count)