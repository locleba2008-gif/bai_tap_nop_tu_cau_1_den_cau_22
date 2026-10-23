n=int(input(''))
so_to_tam_nghin=n//5000
so_to_hai_nghin=(n%5000)//2000
so_to_mot_nghin=((n%5000)%2000)//1000
print(so_to_tam_nghin,so_to_hai_nghin,so_to_mot_nghin)