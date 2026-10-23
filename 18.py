thang,nam=map(int, input('').split())
if nam%400==0 or (nam%4==0 and nam%100!=0):
    if thang in [1,3,5,7,8,10,12]:
        print('31')
    if thang in [2]:
        print('29')    
    elif thang in [4,6,9,11]:
        print('30')   
else:
    if thang in [1,3,5,7,8,10,12]:
        print('31')
    elif thang in [2]:
        print('28')  
    elif thang in [4,6,9,11]:
        print('30')
