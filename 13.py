a,b,c=map(int, input().split())
if a==b==c:
    print('=')
else:
    gtln=a
    for i in [b,c]:
        if i>a:
            gtln=i
        else:
            gtln=a
    print(gtln)                