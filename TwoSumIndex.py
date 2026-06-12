x=input("Enter Values: ").split(",")
x=list(map(int,x))
n=int(input("Enter Target Number: "))
new=set()

for i in x:
    num=n-i
    if num in x:
        if (x.index(num)) in new:
            print(x.index(i),",",x.index(num))
        new.add(x.index(i))