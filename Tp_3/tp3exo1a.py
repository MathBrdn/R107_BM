print("Donnez un nombre!")
N=int(input())
S=0
for i in range(N+1):
    S+=i
print(f"La somme des nombres entiers de 0 à {N} est de {S}")