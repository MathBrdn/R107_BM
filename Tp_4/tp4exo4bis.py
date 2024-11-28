L2=[0]*10
L = []
for i in range(10):
    a = int(input("Donne un chiffre (entre 0 et 9) : "))
    L.append(a)
for i in range(10):
    L2[i]=L.count(i)
maximum=max(L2)
print(f"Le nombre le plus fréquent dans la liste est :{L2.index(maximum)} ({maximum} x)")
