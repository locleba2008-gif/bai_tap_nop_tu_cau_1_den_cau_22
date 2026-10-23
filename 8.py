a,b,c=map(int, input().split())
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
R=a*b*c/(4*s)
print(f'{R:.3f}')