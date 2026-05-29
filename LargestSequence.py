n=input("Enter Values: ").split(",")
y=n.pop(0)
y=list(y)
n=list(map(int,n))
y=list(map(int,y))
x=0
new=[]
for i in n:
    if i==y[x]+1 or i==y[x]:
        y.append(i)
        x+=1
    else:
        z=tuple(y)
        new.append(z)
        y.clear()
        y.append(i)
        x=0
z=tuple(y)
new.append(z)

lenth=len(new[0])
large=[new[0]]
for i in new:
    if len(i)>lenth:
        lenth=len(i)
        large.clear()
        large.append(i)
    elif len(i)==lenth:
        large.append(i)

print("***Largest Sequence/s***")
for i in large:
    print(i)