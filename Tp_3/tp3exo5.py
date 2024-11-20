print("Donnez l'heure de début de la location (un entier).")
a=int(input())
if a<0 or a>24:
    print("« Les heures doivent être comprises entre 0 et 24 ! »")
print("Donnez l'heure de fin de la location (un entier).")
b=int(input())
if b<0 or b>24:
    print("« Les heures doivent être comprises entre 0 et 24 ! »")
elif a==b:
    print("« Attention ! l’heure de fin est identique à l’heure de début. »")
elif b>a:
    print("« Attention ! le début de la location est après la fin ... »")
c=b-a
elif a>=0 and a<=7 and b>=0 and b<=7 or a>=17 and a<=24 and b>=17 and b<=24:
    print(f"Vous avez loué votre vélo pendant {c} heure(s) au tarif horaire de 1.0 euro(s)")
    p=c
elif a>7 and a<17 and b>7 and b<17:
    print(f"Vous avez loué votre vélo pendant {c} heure(s) au tarif horaire de 2.0 euro(s)")
    p=2*c
print(f"Cela vous fera {p}€.")
else:
