import math 
numbers=[]
z=1
i=int(input("enter number of numbers in the list :"))
print("the number of elements in the list =",i)
for t in range(i):
    print("enter",z,"number")
    numberss=int(input(""))
    t=t+1
    z=z+1
    numbers.append(numberss)
print(numbers)
print("1)mode")
print("2)mean")
print("3)median")
print("4)range")
list=int(input("choose from the list :"))
if list==1:
    most_common_item = max(numbers, key=numbers.count)
    print({most_common_item},"it rapeat", {numbers.count(most_common_item)},"times" )
if list==2:
    sums=sum(numbers)
    print(sums/i)
if list==3:
    def mean(list_of_nums):
        total=0
        for num in list_of_nums:
            total=total+num
        return total/len(list_of_nums)    

def median(list_of_nums):
    numbers.sort()
    if i% 2 != 0:
        medil_index=int((i-1)/2)
        return  list_of_nums[medil_index]
    elif i% 2 ==0 :
        meddle_index_1=int((i)/2)
        meddle_index_2=int(i/2)-1
        return int(mean([list_of_nums[meddle_index_1],list_of_nums[meddle_index_2]]))   
if list==4:
    zxc=max(numbers)
    zsd=min(numbers)
    print(zxc-zsd)