nMax=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
if nMax<0 or nMax>10:
    nMax=int(input("La taille n'est pas valable, Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
v1=[]
v2=[]
print("Saisie du premier vecteur :")
for i in range(nMax):
    a=int(input())
    v1.append(a)
    print(f"v1[{i}]={v1[i]}")
print("Saisie du second vecteur :")
for i in range(nMax):
    b=int(input())
    v2.append(b)
    print(f"v2[{i}]={v2[i]}")
Pscalaire=0
for i in range(nMax):
    Pscalaire+=v1[i]*v2[i]
print(f"Le produit scalaire de v1 par v2 vaut {Pscalaire}")
