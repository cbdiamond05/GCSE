import os
import time
from Pupil import *
from EnterTimes_Average import *
from summary_report import *
import sqlite3

def login():
    password='ClarendonHigh21'
    chance=3
    guess=input("Please enter the login password: ")
    while guess!=password and chance >0:
        guess=input("Sorry your password is incorrect. Please try again: ")
        chance=chance-1
    if guess==password:
        print("Access granted.")
        time.sleep(1)
        os.system('cls')
    if guess !=password:
        input("Sorry you have been locked out! Please try again later!")
        quit()

def main_menu():
    print("Welcome to Clarendon High Ski Trip menu!")
    print("                                    ")
    print("1. Add new pupil ")
    print("2. Enter ski slope times")
    print("3. Complete the ski safety quiz")
    print("4. See pupil's average time")
    print("5. View pupil report")
    print("6. View list of abilities")
    print("7. View the management summary")
    print("8. Enter a new query")
    print("9. Exit the system")
    print("                            ")
    
    while True:
        try:
            choice=int(input("Please choose an option: "))
        except ValueError:
            print("Input invalid. You must choose a number: ")
        else:
            break
    if choice<1 or choice>8:
        choice=int(input("Your choice must be between 1 and 8. Please enter again: "))
    elif choice==1:
        os.system('cls')
        add_pupil()
        main_menu()
    elif choice==2:
        os.system('cls')
        safety_quiz()
        main_menu()
    elif choice==3:
        os.system('cls')
        enter_times()
        main_menu()
    elif choice==4:
        os.system('cls')
        average_time()
        main_menu()
    elif choice==5:
        os.system('cls')
        view_abilities()
        main_menu()
    elif choice==6:
        os.system('cls')
        management_summary()
        main_menu()
    elif choice==7:
        os.system('cls')
        pupil_report()
        main_menu()
    elif choice==8:
        os.system('cls')
        new_query()
        main_menu()
    else:
        input("Thank you for using Clarendon High Ski Trip menu!")
        quit()




login()
main_menu()