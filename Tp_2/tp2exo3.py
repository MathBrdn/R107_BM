print("Entrez la premiere valeur :")
a=int(input())
print("Entrez la deuxieme valeur :")
b=int(input())
print("Entrez la troisieme valeur :")
c=int(input())
print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}")
print("permutation: a ==> b, b ==> c, c ==> a")
temp=a
a=c
c=b
b=temp
print(f"Les valeurs permutees sont : a={a}, b={b} et c={c}.")
