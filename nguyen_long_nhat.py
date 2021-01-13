x=int(input())
for i in range(1,x+1):
    dem=0
    if x%i==0:
        dem+=1
if dem==2:
    print("%d la so nguyen to :" % (x))
else:
    print("%d khong phai la so nguyen to "%(x))
