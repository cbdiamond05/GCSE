import sqlite3
new_db=sqlite3.connect('SkiTrip.db')
c=new_db.cursor()
c.execute('''CREATE TABLE SkiTrip
(Pupil_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
Forename text,
Surname text,
Age integer,
Year_group integer,
Phone_number integer,
Test_score integer,
Time1 decimal,
Time2 decimal,
Time3 decimal,
Time4 decimal,
Time5 decimal,
Average decimal,
Paid text,
Group_level text)''')

    
