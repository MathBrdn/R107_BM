nom=[]
for i in range(2):
    n=str(input("Donnez votre nom!"))
    p=str(input("Donnez votre prénom!"))
    str.upper(n)
    str.capitalize(p)
    nom.append(n)
    nom.append(p)
if nom[0]<nom[2]:
    temp=nom[0]
    nom[0]=nom[2]
    nom[2]=temp
    temp = nom[1]
    nom[1] = nom[3]
    nom[3] = temp
elif nom[0]==nom[2]:
    if nom[1]<nom[3]:
        temp = nom[1]
        nom[1] = nom[3]
        nom[3] = temp
        temp = nom[0]
        nom[0] = nom[2]
        nom[2] = temp
    elif nom[1]==nom[3]:
        


