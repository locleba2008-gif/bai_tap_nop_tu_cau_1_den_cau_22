so_giay=int(input())
gio=so_giay//3600
phut=(so_giay-gio*3600)//60
giay=so_giay-gio*3600-phut*60
print(gio,phut,giay,sep=':')