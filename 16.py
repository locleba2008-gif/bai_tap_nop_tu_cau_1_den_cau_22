TBHK1,TBHK2=map(int,input('').split())
TBCN=(TBHK1+TBHK2*2)/3
print(f'{TBCN:.1f}')
if TBCN>=8:
    print('Gioi')
elif 6.5<=TBCN<8:
    print('Kha')   
elif 5.0<=TBCN<6.5:
    print('Trung binh')
elif 3.5<=TBCN<5.0:
    print('Yeu')
else:
    print('Kem')    