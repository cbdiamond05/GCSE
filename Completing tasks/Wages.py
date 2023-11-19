while True:
        try:
            wage1=int(input("Please enter the first wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage2=int(input("Please enter the second wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage3=int(input("Please enter the third wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage4=int(input("Please enter the fourth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage5=int(input("Please enter the fifth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage6=int(input("Please enter the sixth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage7=int(input("Please enter the seventh wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage8=int(input("Please enter the eighth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage9=int(input("Please enter the ninth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
while True:
        try:
            wage10=int(input("Please enter the tenth wage: "))
        except ValueError:
            print("It must be a number: ")
        else:
            break
totalwage=wage1+wage2+wage3+wage4+wage5+wage6+wage7+wage8+wage9+wage10
if totalwage>200:
    print("Your total wage for the group exceeds the maximum of £200")
else:
    averagewage=totalwage/10
    print("Your total wage for the group is £",totalwage," and your average wage for the group is £",averagewage)
    