score=0
word=input("Enter a word: ")
for i in word:
    if [i]=="a":
        score=score+5
    elif [i]=="e":
        score=score+4
    elif [i]=="i":
        score=score+3
    elif [i]=="o":
        score=score+2
    elif [i]=="u":
        score=score+1
print("Your score is ",score)

number1=float(input("Enter your first number: "))
number2=float(input("Enter your second number: "))
def larger(number1,number2):
    if number1>number2:
        return(number1)
    else:
        return(number2)
print(larger(number1,number2))

name=str(input("Enter your name: "))
def long_name(name):
    if len(name)>14:
        return("True")
    else:
        return("False")
print(long_name(name))

number1=float(input("Enter your first number: "))
number2=float(input("Enter your second number: "))
number3=float(input("Enter your third number: "))
def largest(number1,number2,number3):
    if number1>number2 and number1>3:
        return(number1)
    elif number2>number1 and number2>number3:
        return(number2)
    elif number3>number1 and number3>number2:
        return(number3)


print("Number ",largest(number1,number2,number3)," is the largest")















