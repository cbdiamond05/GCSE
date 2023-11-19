import sqlite3
def management_summary():
    print("Welcome to management summary.")
    print("1- View by age")
    print("2- View by paid")
    
    choice=int(input("Please enter either 1 or 2: "))
    while choice not in [1,2]:
        choice=int(input("Invalid responce. Please enter 1 or 2: "))

    if choice==1:
        age=get_age("Which age group would you like to view?: ")
        while age<11 or age>18:
            age=get_age("You you must be age between 11 and 18. Please try again: ")
        new_db=sqlite3.connect('SkiTrip.db')
        c=new_db.cursor()
        c.execute('''SELECT forename FROM SkiTrip WHERE Age=?''',(age,))
        pupil=c.fetchall()
        print("Pupils that are ",age," are ",pupil,"\n")
    
    if choice==2:
        paid=str(input("Would you like to view if the pupils have paid? Please enter Y/N: "))
        while paid not in ("Y","N"):
            paid=str(input("Invalid responce. Please enter Y/N: ")).upper()
        c.execute('''SELECT firstname FROM SkiTrip WHERE paid=?''',(paid,))
        pupil=c.fetchall()
        print("Pupils that have paid are ",pupil,"\n")
        
def get_age(input_message):
    while True:
        try:
            age=int(input(input_message))
        except ValueError:
            print("Invalid response. Please try again.")
        else:
            break

    return age

management_summary()     


def pupil_report():
    print("Welcome to pupil report.")
    
    while True:
        try:
            Pupil_ID=int(input("Please enter pupil's ID: "))
        except ValueError:
            print("Pupil ID must be a number")
        else:
            new_db=sqlite3.connect('SkiTrip.db')
            c=new_db.cursor()
            c.execute('''SELECT Pupil_ID FROM SkiTrip WHERE Pupil_ID = ? ''', (Pupil_ID,))
            pupil = c.fetchone()
            if pupil == None:
                print("This pupil does not exist. Please check the Pupil ID!")
            else:
                break
    c.execute('''SELECT forename,surname,age,year_group,average,group_level,quiz,phone_number FROM SkiTrip WHERE Pupil_ID=?''',(Pupil_ID,))
    pupil=c.fetchall()
    pupils=pupil[0]
    
    forename=pupils[0]
    surname=pupils[1]
    age=pupils[2]
    year_group=pupils[3]
    average=pupils[4]
    group_level=pupils[5]
    quiz=pupils[6]
    phone_number=pupils[7]
    
   
    
    print("\nName: ",forename,surname)
    print("\nAge: ",age)
    print("\nYear Group: ",year_group)
    print("\nPhone Number: ",phone_number)
    print("\nAbility: ",group_level)
    print("\nQuiz: ",quiz,"/25")
    print("\nAverage: ",average,"seconds")



def new_query():
    query=str(input("Would you like to enter another query? Y/N: ")).upper()
    while query not in ["Y","N"]:
        query=str(input("Invaild responce. Please enter Y/N: ")).upper()
    while query == 'Y':
        query=str(input("Would you like to enter another query? Y/N: ")).upper()
        if query not in ["Y","N"]:
           query=str(input("Invaild responce. Please enter Y/N: ")).upper()
    else:
       print("Thank you for completing the Clarendon High Ski Trip menu!")

print("Thank you for completing the Clarendon High Ski Trip menu!")
