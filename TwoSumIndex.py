x=input("Enter Values: ").split(",")
x=list(map(int,x))
n=int(input("Enter Target Number: "))
new=[]

for i in x:
    num=n-i
    if num==i:
        continue
    else:
        if num in x:
            if (x.index(i)) not in new:
                new.append(x.index(i))
                new.append(x.index(num))
                print(x.index(i),",",x.index(num))