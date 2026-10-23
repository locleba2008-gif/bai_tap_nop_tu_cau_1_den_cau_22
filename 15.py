a,b,c=map(int, input().split())
if a+b>c and a+c>b and b+c>a:
    cv=a+b+c
    p=cv/2
    dt=(p*(p-a)*(p-b)*(p-c))**0.5
    print('Day la 3 canh cua mot tam giac')
    print(f"{cv:.2f} {dt:.1f}")
else:
    print('Day khong phai la 3 canh cua mot tam giac')    