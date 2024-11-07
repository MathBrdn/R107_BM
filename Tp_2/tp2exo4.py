base=int()
base=4
fromage=float()
fromage=800.0
eau=int()
eau=2
ail=int()
ail=2
pain=int()
pain=400
print("Entrez le nombre de personne(s) conviées à la fondue :")
nbConvives=int(input())
fromage=fromage*nbConvives/base
eau=eau*nbConvives/base
ail=ail*nbConvives/base
pain=pain*nbConvives/base
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut:")
print(f"-{fromage}g de fromage")
print(f"-{eau}dL d'eau")
print(f"-{ail}gousse(s) d'ail")
print(f"-{pain}g de pain")

