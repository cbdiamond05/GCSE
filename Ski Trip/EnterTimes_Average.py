import sqlite3
import os
from Menu import *

def enter_times():                             
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
    
    new_db=sqlite3.connect('SkiTrip.db')
    c=new_db.cursor()
    c.execute('''SELECT average FROM SkiTrip WHERE Pupil_ID = ?''',(Pupil_ID,))
    time=c.fetchone()
    average=time[0]
    
    if average != None:
        print("Your times have already been completed for this pupil!")
        choice=str(input("Would you like to enter new times? Y/N: ")).upper()
        while choice not in ["Y","N"]:
            choice=input("You have entered and invalid responce. Please enter Y/N: ").upper()
        if choice=="N":
            print("You will be redirected to the menu page.")
            os.system('cls')
            main_menu()
            return;
        else:
            choice="Y"
        

    time1=get_time("\nPlease enter the pupil's first time: ")
    time2=get_time("\nPlease enter the pupil's second time: ")
    time3=get_time("\nPlease enter the pupil's third time: ")
    time4=get_time("\nPlease enter the pupil's fourth time: ")
    time5=get_time("\nPlease enter the pupil's fifth time: ")
    average=(time1+time2+time3+time4+time5)/5
    with sqlite3.connect('SkiTrip.db')as db:
        c=db.cursor()
        c.execute('UPDATE SkiTrip SET time1=?,time2=?,time3=?,time4=?,time5=?,average=? WHERE Pupil_ID=?',(time1,time2,time3,time4,time5,average,Pupil_ID))
        db.commit()
    print("Your average is ",average)
    update_ability(Pupil_ID)
#

def update_ability(pupilID):
    new_db=sqlite3.connect('SkiTrip.db')
    c=new_db.cursor()
    c.execute('''SELECT Quiz FROM SkiTrip WHERE Pupil_ID=?''',(pupilID,))
    quiz=c.fetchone()

    c.execute('''SELECT average FROM SkiTrip WHERE Pupil_ID = ?''',(pupilID,))
    time=c.fetchone()
    average=time[0]
    
    if average != None and quiz!=None:
        score=quiz[0]
        if average<40 and score>=23:
            group_level="Advanced"
        elif average<50 and score>=19:
            group_level="Intermediate"
        else:
            group_level="Beginner"
        new_db=sqlite3.connect('SkiTrip.db')
        c=new_db.cursor()
        c.execute('''UPDATE SkiTrip SET group_level = ? WHERE Pupil_ID = ?''',(group_level, pupilID))
        print("\nYour new times have been recorded, and your ability has been changed to",group_level)
    else:
        print("Your times have been recorded.")
    new_db.commit()


def get_time(input_message):
    while True:
        try:
            time=float(input(input_message))
        except ValueError:
            print("The pupil's time cannot include a letter. Please try again.")
        else:
            break

    return time


def average_time():
    while True:
        try:
            Pupil_ID=int(input("Please enter pupil's ID: "))
        except ValueError:
            print("Pupil ID must be a number.")
        else:
            new_db=sqlite3.connect('SkiTrip.db')
            c=new_db.cursor()
            c.execute('''SELECT Pupil_ID FROM SkiTrip WHERE Pupil_ID = ? ''', (Pupil_ID,))
            pupil = c.fetchone()
            if pupil == None:
                print("This pupil does not exist. Please check the Pupil ID!")
            else:
                break
        c.execute('''SELECT forename, average FROM SkiTrip WHERE Pupil_ID = ?''',(Pupil_ID,))
        average=c.fetchone()
        print("Pupil's average time is: ",average,"\n")
        


def view_abilities():
    ability=input("Please enter which ability list you would like to explore?\n a)Beginner\n b)Intermediate\n c)Advanced\n Answer: ").lower()
    while ability not in ["a", "b", "c"]:
        ability=input("You have entered and invalid responce. Please enter a, b or c: ")
    if ability=="a":
        ability="Beginner"
    if ability=="b":
        ability="Intermediate"
    if ability=="b":
        ability="Advanced"
    
    new_db=sqlite3.connect('SkiTrip.db')
    c=new_db.cursor()
    c.execute('''SELECT forename FROM SkiTrip WHERE Ability=?''',(ability,))
    pupil=c.fetchone()
    
    print(ability,"Pupils: ",pupil)
