mylist=[4,0,2,3,1]
for i in range(len(mylist)):
    no_swaps=True
    for j in range(len(mylist)-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
            no_swaps=False
        if no_swaps:
            print(mylist)
