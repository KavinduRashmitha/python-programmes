nums=input("Enter Values: ").split(",")
nums=list(map(int,nums))
i=0
j=1
start=nums[0]
Sort=True
for i in nums:
    if i>=start:
        start=i
    else:
        Sort=False
        break
if Sort:
    print("This is a Sorted List")
else:
    print("This List is Not Sorted")