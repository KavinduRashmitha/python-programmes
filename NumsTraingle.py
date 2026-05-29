n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    isPrinted=False
    for j in range(1,i+1):
        if isPrinted==False:
            print(" "*(n-i),end="")
            isPrinted=True
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()