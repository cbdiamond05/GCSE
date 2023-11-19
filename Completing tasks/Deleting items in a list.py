mylist=[2,3,5,4,6,67]
def remove_five(mylist):
    return mylist.remove(5)
remove_five(mylist)
print(mylist)

mylist= [1,2,2,3,3,3,4,4,5,5,6]
def unique_elements(x):
    newlist=[]
    for iteam in range(len(x)):
        iteam=x.pop()
        if iteam not in newlist:
            newlist.append(iteam)
    newlist.reverse()
    print(newlist)
    print(mylist)
unique_elements(mylist)

mylist=[2,343,45,54,7543,35]
def backways(mylist):
    return mylist.reverse()
backways(mylist)
print(mylist)

mylist=[2,3,4,6,58,779]
def sum_list(mylist):
    total=0
    for iteam in mylist:
        total=total+iteam
        return total
print(sum_list(mylist))

mylist=[2,3,4,6,58,779]
def sum_list(mylist):
    total=0
    for iteam in mylist:
        total=total+iteam
        return total
print(sum_list(mylist))

def mean_list(mylist):
    return sum_list(mylist)/len(mylist)

    
