n=int(input(''))
tien=0
if n<=1:
    tien=n*12000
elif 1<n<=30:
    tien=1*12000+(n-1)*10000
else:
    tien=1*12000+(30-1)*10000+(n-30)*9000
print(tien)           