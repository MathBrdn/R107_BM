from random import*
x=randint(0,100)
c=0
print("Devinette: Donnez un nombre entre 0 et 100!")
n=int(input())
while not n==x:
    c+=1
    if n<x:
        print("C'est plus!")
    else:
        print("C'est moins!")
    n=int(input())
print(f"Vous avez gangné! après {c}erreur(s)")