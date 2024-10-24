minute=int(input())
83727343
heure=minute//60
jour=heure//24
jour%=31
print(f"nous sommes le {jour} du mois")
