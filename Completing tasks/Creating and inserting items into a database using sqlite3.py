import sqlite3
new_db=sqlite3.connect('Python')
c=new_db.cursor()
c.execute('''CREATE TABLE Books(book_isbn text,book_title text,book_type text,book_author text,publisher text)''')
c.execute('''INSERT INTO Books VALUES('978-0-340-88851-3','A2 Pure Mathematics','Non-fictional','Catherine Berry','Hodder Education')''')
c.execute('''INSERT INTO Books VALUES('978-1-118-10227-5','Android 4 Application Development','Non-fictional','Reto Merier','Wiley')''')
c.execute('''INSERT INTO Books VALUES('0-596-00699-3','Programming C#','Non-fictional','Jesse Liberty','O Reilly')''')
new_db.commit()
new_db.close()

new_db=sqlite3.connect('Python')
c=new_db.cursor()
book_library=c.fetchall()
for book in book_library:
    print(book)
new_db.close()

