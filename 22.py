n=int(input(''))
tien=0
if 0<n<=50:
    tien=n*600
elif 50<n<=100:
    tien=50*600+(n-50)*800
elif 100<n<=200:
    tien=50*600+50*800+(n-100)*1100
else:
    tien=50*600+50*800+100*1100+(n-200)*1500
print(tien)        