a,b,c=map(int, input().split())
cv=a+b+c
p=cv/2
dt=(p*(p-a)*(p-b)*(p-c))**0.5
print(f"{cv:.1f} {dt:.3f}")