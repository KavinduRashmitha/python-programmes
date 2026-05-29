x=input("Enter Values: ").split(",")
x=list(set(map(int,x)))
n=int(input("Enter Target Number: "))
new=[]

for i in x:
    num=n-i
    if num==i:
        continue
    else:
        if num in x:
            if i not in new:
                new.append(i)
                new.append(num)
                print(i,",",num)