def bank_holiday(month_number):
    print(bank_holidays_in_month[month_number-1])


bank_holidays_in_month=[1,0,1,1,2,0,0,1,0,0,0,2]
month_number=int(input("Which month number are you trying to find out how many bank holidays it has?: "))
bank_holiday(month_number)
    
    
