colonne1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
colonne2 = [0] * 10
L = []
for i in range(10):
    a = int(input("Donne un chiffre (entre 0 et 9) : "))
    L.append(a)
    for j in range(10):
        if a == colonne1[j]:
              colonne2[j] += 1
maximum = max(colonne2)
for j in range(10):
    if colonne2[j] == maximum:
        print(f"Le nombre le plus fréquent dans la liste est : {colonne1[j]} ({colonne2[j]} x)")




