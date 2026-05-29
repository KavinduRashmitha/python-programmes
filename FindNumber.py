nums=input("Enter Numbers: ").split(",")
nums=list(map(int,nums))
n=int(input("Enter a Target Number: "))
if n in nums:
    print(True)
else:
    print(False)