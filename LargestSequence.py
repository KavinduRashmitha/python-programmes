n=input("Enter Values: ").split(",")
y=n.pop(0)
y=[int(y)]
n=list(map(int,n))
x=0
new=set()
for i in n:
    if i==y[x]+1 or i==y[x]:
        y.append(i)
        x+=1
    else:
        z=tuple(y)
        new.add(z)
        y.clear()
        y.append(i)
        x=0
z=tuple(y)
new.add(z)

lenth=0
large=[]
for i in new:
    if len(i)>lenth:
        lenth=len(i)
        large.clear()
        large.append(i)
    elif len(i)==lenth and i not in large:
        large.append(i)

print("***Largest Sequence/s***")
for i in large:
    print(i)