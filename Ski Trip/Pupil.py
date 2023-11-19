import sqlite3
import os
def add_pupil():
    forename=str(input("Please enter pupil's forename: ")).title()
    while str.isalpha(forename)==False:
        forename=str(input("Pupil's forename can only include letters. Please try again: "))
    
   
    surname=str(input("Please enter pupil's surname: ")).title()
    while str.isalpha(surname)==False:
        surname=str(input("Pupil's surname can only include letters. Please try again: "))
    
    while True:
        try:
            age=int(input("Please enter pupil's age: "))
        except ValueError:
            print("It must be a number: ")
        else:
            if age<10 or age>19:
                print("You you must be age between 11 and 18. Please try again: ")
            else:
                break
    
    while True:
        try:
            year_group=int(input("Please enter pupil's year: "))
        except ValueError:
            print("It must be a number: ")
        else:
            if year_group<8 or year_group>14:
                print("You must be in a year group between 8 and 14. Please try again: ")
            else:
                break
    
    while True:
        try:
            phone_number=input("Please enter pupil's contact number: ")
        except ValueError:
            print("It must be a number: ")
        else:
            if len(phone_number) !=11:
                print("Contact phone number must be 11 digits. Please enter try again: ")
            else:
                break
    
    while True:
        paid=str(input("Has this pupil paid for the trip? Please enter Y/N: ")).upper()
        if paid not in ("Y","N"):
            print("Answer must be Y or N")
        else:
            break
    
    new_db=sqlite3.connect('SkiTrip.db')
    c=new_db.cursor()
    c.execute("INSERT INTO SkiTrip(forename,surname,age,year_group,phone_number,paid)VALUES(?,?,?,?,?,?)",(forename,surname,age,year_group,phone_number,paid))
    print("Your pupil has been added.")
    new_db.commit()
  
add_pupil()
def safety_quiz():
    print("Welcome to the safety knowledge assessment!")
    print("                                           ")

    while True:
        try:
            Pupil_ID = int(input("Please enter Pupil ID: "))
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
    
    c.execute('''SELECT Quiz FROM SkiTrip WHERE Pupil_ID = ?''',(Pupil_ID,))
    temp=c.fetchone()
    test_score=temp[0]
        
    if test_score!=None:
        print("This pupil has already completed their Ski Trip Test.")
        choice=str(input("Would you like to update their Ski Trip Test? Y/N: ")).upper()
        while choice not in ["Y", "N"]:
            choice=str(input("Input invalid. Please enter Y/N: ")).upper()
        if choice=="N":
            print("You will be redirected")
            os.system('cls')
            main_menu()
            return;
        
    score = 0
    
    questions =  [["1 - Do you have any ski experience? Y/N: ","Y",5],
                 ["2 - What clothing must be worn when skiing?\n(A)skirt,t-shirt and trainers\n(B)leggings,jumper and pumps\n(C)boots,coat,helmet and goggles:","C",5],
                 ["3 - What sized hill should you start at?\n (A)big hill\n (B)small hill\n (C)middle hill\n Answer: ","B",5],
                 ["4 - What is the best way to prevent injury?\n(A)try advanced tricks\n(B)warm up,hydrate and take breaks\n(C)go skiing unsupervised:","B",5],
                 ["5 - What equipment is needed for skiing?\n(A)ski poles,skis and a ski bag\n(B)phone,jewellery and make-up\n(C)skis,handbag and earphones:","A",5],
                 ["6 - Do you have any knowledge of emergency first aid? Y/N: ","Y",5]]

    answer_1=input(questions[0][0]).upper()
    while answer_1 not in ("Y","N"):
        answer_1=input("Invalid response. Your answer must be Y or N! Please try again: ").upper()  
    os.system('cls')
    
    answer_2=input(questions[1][0]).upper()
    while answer_2 not in ("A","B","C"):
        answer_2=input("Invalid response. Your answer must be A, B or C! Please try again: ").upper() 
    os.system('cls')

    answer_3=input(questions[2][0]).upper()
    while answer_3 not in ("A","B","C"):
        answer_3=input("Invalid response. Your answer must be A, B or C! Please try again: ").upper() 
    os.system('cls')

    answer_4=input(questions[3][0]).upper()
    while answer_4 not in ("A","B","C"):
        answer_4=input("Invalid response. Your answer must be A, B or C! Please try again: ").upper() 
    os.system('cls')
    

    answer_5=input(questions[4][0]).upper()
    while answer_5 not in ("A","B","C"):
        answer_5=input("Invalid response. Your answer must be A, B or C! Please try again: ").upper() 
    os.system('cls')

    answer_6=input(questions[5][0]).upper()
    while answer_6 not in ("Y","N"):
        answer_6=input("Invalid response. Your answer must be Y or N! Please try again: ").upper() 
    os.system('cls')
    

    if answer_1==questions[0][1]:
        score=score+questions[0][2]

    if answer_2==questions[1][1]:
        score=score+questions[1][2]

    if answer_3==questions[2][1]:
        score=score+questions[2][2]

    if answer_4==questions[3][1]:
        score=score+questions[3][2]

    if answer_5==questions[4][1]:
        score=score+questions[4][2]
        
    if answer_6==questions[5][1]:
        score=score+questions[5][2]
        
    c.execute('''UPDATE SkiTrip SET Quiz = ? WHERE Pupil_ID = ?''',(score, Pupil_ID))
    

    print("Your result is ",score, " out of 30")
    print("Your score has been recorded.")
    print("Thank you for completing the ski safety test!")
    
    new_db.commit()
    update_ability(Pupil_ID)

