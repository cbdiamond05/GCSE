def bank_holiday(month_number):
    print(bank_holidays_in_month[month_number-1])

bank_holidays_in_month=[1,0,1,1,2,0,0,1,0,0,0,2]
month_number=int(input("Which month number are you trying to find out how many bank holidays it has?: "))
bank_holiday(month_number)

mylist=[35,56,94,845,68]
def add_hello(mylist):
    mylist.append("Hello")
    print(mylist)
add_hello(mylist)


mylist=[9.6,586.76,24.68,94.6]
def discount_ten(alist):
    newlist=[]
    for item in alist:
        newlist.append(item*.9)
    return newlist
print(discount_ten(mylist))

    

        






