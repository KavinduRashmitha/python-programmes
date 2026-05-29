n=input("Enter Values: ").split(",")
n=list(map(int,n))
new=dict()
for i in n:
    new[i]=new.get(i,0)+1
for i in new:
    print(i,":",new.get(i))