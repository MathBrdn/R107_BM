minute=78
heure=35
jour=44
while minute > 60:
    minute%=60
    heure+=1
while heure > 24:
    heure%=24
    jour+=1
jour%=31
heure+=jour*24
minute+=heure*60
print(f"{minute} se sont écoulées depuis le début du mois")
