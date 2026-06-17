#Inputs
n=input("Enter Values: ").split(",")
#End

#Variables
n_list=sorted(list(set(map(int,n))))
IsDone=False
Final_set=set()
#End

#Proceder
while (len(n_list)!=0):
    temp_list=[n_list.pop(0)]
    count=0
    while IsDone==False:
        if temp_list[count]+1 in n_list:
            temp_list.append(temp_list[count]+1)
            n_list.remove(temp_list[count]+1)
            count+=1
        else:
            IsDone=True
    ListToTuple=tuple(temp_list)
    Final_set.add(ListToTuple)
    temp_list.clear()
    IsDone=False 
print(Final_set)
#End   
            

#LogicToFindTheLargestOne
lenth=0
large=[]
for i in Final_set:
    if len(i)>lenth:
        lenth=len(i)
        large.clear()
        large.append(i)
    elif len(i)==lenth and i not in large:
        large.append(i)

print("***Largest Sequence/s***")
for i in large:
    print(i)
#End