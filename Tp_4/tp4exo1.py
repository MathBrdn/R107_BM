n=float(input("Vous cherchez la table de multiplication de quel nombre ?"))
for i in range(10):
    x=n*i
    x=round(x,2)
    print(f"{n}*{i}={x}")


