nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
s=0.0
for i in range(nombreEtudiants):
    a=float(input(f"Note etudiant {i}:"))
    notes.append(a)
    s+=a
moyenne = s/nombreEtudiants
moyenne=round(moyenne,2)
print(f"Moyenne de classe : {moyenne}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart=notes[i]-moyenne
    print(f"{i} | {notes[i]} | {ecart}")
