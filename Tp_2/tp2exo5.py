print("Entrez un nombre entier:")
x=int(input())
if x>0:
    if x%2==0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
elif x<0:
    if x%2==0:
        print("Le nombre est négatif et pair")
    else:
        print("Le nombre est négatif et impair")
else:
    print("Le nombre est zéro (et il est pair)")
