L=[5,2,4,8,1,3]
L2=[1,2,3,4,5,8]
while not L==[1,2,3,4,5,8]:
    for i in range(6):
        n=0
        print(f"L={L}")
        while not L[n]==min(L2):
            n+=1
        L[n]=L[i]
        L[i]=L2[0]
        L2.remove(L2[0])



    










    

