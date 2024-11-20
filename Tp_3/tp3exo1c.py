a=0
b=0
c=0
for i in range(10):
    print("Donnez un nombre!")
    N=int(input())
    if N<0 or N>20:
        print("La valeur n'est pas bonne, donnez-en une nouvelle!")
        N=int(input())
    elif N<10:
        a+=1
    elif N>=10 and N<15:
        b+=1
    else:
        c+=1
print(f"Parmis les 10 valeurs donnés il y a: {a}valeur(s) strictement inférieur(s) à 10, {b}valeur(s) supérieur(s) ou égal à 10 et strictement inférieur(s) à 15 et {c}valeurs supérieur(s) ou égal à 15.")

