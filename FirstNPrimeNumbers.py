n=int(input("How Far You Want: "))
p=0
count=0
while count<n:
    p+=1
    isPrime=True
    for i in range(2,p):
        if p%i==0:
            isPrime=False
            break
    if isPrime:
        print(p)
        count+=1