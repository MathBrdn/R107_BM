login1=str(input("Votre nom!"))
login2=str(input("Votre nom!"))
binome = (login1, login2)
del binome[1]
print(f"L’étudiant {binome[0]} est en binôme avec l’étudiant {binome[1]}")