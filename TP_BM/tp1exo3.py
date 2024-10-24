jour=int(input())
56
heure=int(input())
76
minute=int(input())
34
while minute > 60:
    minute%=60
    heure+=1
while heure > 24:
    heure%=24
    jour+=1
jour%=31
heure+=jour*24
minute+=heure*60
print(f"{minute} minute se sont écoulées depuis le début du mois")

