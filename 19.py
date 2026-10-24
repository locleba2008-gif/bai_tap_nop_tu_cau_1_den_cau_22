n=int(input('nhap so co nam chu so'))
tong=0
for i in range(5):
    tong+=n%10
    n=n//10
nut=tong%10
if nut==9:
    print(nut)
    print('may man')
else:
    print(nut)
    print('chua may man')
