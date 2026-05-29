n=int(input("Number of Rows: "))
print("* "*n)
for i in range(2,n):
    x=("{}{}{}")
    x=x.format("*"," "*(((n-2)*2)+1),"*")
    print(x)
print("* "*n)