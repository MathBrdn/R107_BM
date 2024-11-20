print("Donnez le nombre sur lequel vous voulez connaitre sa factorielle!")
n=int(input())
print("Vous voulez utiliser un for(si oui tappez 'for') ou un while(tappez 'while')?")
a=str(input())
f=1
b=0
if a=="for":
    for i in range(n):
        b+=1
        f*=b
elif a=="while":
    while not b==n:
        b+=1
        f*=b
else:
    print("erreur! tappe 'for' ou 'while'")
    a=str(input())
print(f"La factorielle de {n} est {f}.")
