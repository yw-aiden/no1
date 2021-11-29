day=1
max=0
mday=1
for day in range(1,366):
    sum=1
    term=365//day
    for j in range(term):
        sum+=sum*1.00*day/365
    sum+=1/365*(365-day*term)
    if sum>max:
        max=sum
        mday=day
print("取得最大利益化时，每",mday,"天存取一次钱")
print("最大收益为：",max,"元")






