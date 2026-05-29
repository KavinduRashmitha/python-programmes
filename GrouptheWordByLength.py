n=input("Ente Text: ").split(",")
#j=[]
new=dict()
for i in n:
    new[len(i)]=new.get(len(i),[])+[i]
print(new)