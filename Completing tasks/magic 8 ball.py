#Magic 8 Ball
loop="yes"
while loop=="yes":
     import random
     import time
     magic = random.randint(1,6)
     if magic==1:
         ans="It is certain"
     elif magic==2:
         ans="Outlook uncertain"
     elif magic==3:
         ans="Ask again later"
     elif magic==4:
         ans="My sources say no"
     elif magic==5:
         ans="You may rely on it"
     else:
         ans="No"
     
     question=input("Ask the magic 8 ball a question: ")
     time.sleep(2)
     print(ans)
     time.sleep(2)
     loop=input("Ask again? yes/no: ")
     loop.lower
     time.sleep(2)
     if loop=="No":
         print("See you again")


 

