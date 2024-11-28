date=[]
print("Donne une date sous le format jjmmaaaa")
for i in range(8):
    a=int(input())
    date.append(a)
if date[0]>3:
    print("La date n'existe pas")
elif date[0]==3:
    if date[1]>1:
        print("La date n'existe pas")
    elif date[1]==1 and date[3]%2==1:
        print("La date n'existe pas")
elif date[2]>1:
    print("La date n'existe pas")
elif date[2]==1 and date[3]>2:
    print("La date n'existe pas")
elif (date[4]*1000+date[5]*100+date[6]*10+date[7])%4==0 and (date[4]*1000+date[5]*100+date[6]*10+date[7])%100!=0:
    if date[2]==0 and date[3]==2 and date[0]>2:
        print("La date n'existe pas")
else:
    print("La date existe")



