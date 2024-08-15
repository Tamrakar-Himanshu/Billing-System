import mysql.connector
import tkinter as tk
import random


mydb = mysql.connector.connect(host="localhost",user="root", password="1234" )
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE HOTEL_MANAGEMENT")
    mydb = mysql.connector.connect(host="localhost",user="root", password="1234", database ="HOTEL_MANAGEMENT" )
except:
      pass

try:              
      mydb = mysql.connector.connect(host="localhost",user="root", password="1234", database ="HOTEL_MANAGEMENT" )
      mycursor=mydb.cursor()
      mycursor.execute("CREATE TABLE FOOD_MENU (FOODCODE INT(5)PRIMARY KEY,ITEM CHAR(50),PRICE INT(6))")
      fd="insert into food_menu(foodcode,item,price) values(201,'Veg Burger',30),(202,'CheeseBurger',40),(203,'Paneer Burger',40),(204,'Double CheeseBurger',40),(205,'Paneer Cheese Burger',50),(206,'Garlic Burger',40),(207,'Spring Roll',40),(208,'Kathi Roll',40),(209,'Paneer Roll',40),(210,'Veg Roll',40),(211,'French Fries',30),(212,'Momos',40),(213,'Momos Fries',50),(214,'Chilly Paneer',70),(215,'Potato Chilly',40),(216,'Manchurian',40),(217,'Dry Manchurian',40),(218,'Paneer Manchurian',60),(219,'Soyabean Manchurian',40)"
      mycursor.execute(fd)
      mydb.commit()
      fd1="insert into food_menu(foodcode,item,price) values(301,'Cheese Paratha',40),(302,'Aalu Paratha',30),(303,'Pyaz Paratha',40),(304,'Aalu Pyaz Paratha',40),(305,'Paneer Paratha',50),(306,'Gobhi Paratha',40),(307,'Butter Paratha',40),(308,'Fried Rice',30),(309,'Manchurian Rice',40),(310,'Paneer Rice',40),(311,'Garlic Rice',40),(312,'Saijwan fried Rice',40),(313,'Veg Pasta',40),(314,'White Pasta',50),(315,'Cheese Pasta',50),(316,'Red Pasta',40),(317,'White Paneer Pasta',60),(318,'Red Paneer Pasta',60)"
      mycursor.execute(fd1)
      mydb.commit()
      fd3 = "insert into Food_Menu (Foodcode,Item,Price) values (101,'VegMaggie',(40)) , (102,'planeMaggie' ,30 ) , (103,'ButterMaggie',40),(104,'CheeseMaggie',40) ,(105,'BreadMaggie',40) , (106,'ManchurianMaggie',40),(107,'Butter Masala Maggie',40) , (108,'Soyabean Maggie',50),(109,'Chawmein Veg' , 30) , (110,'Paneer Chawmein',50) , (111,'Hakka Noodles',40),(112,'Soya Noodles',45)"
      mycursor.execute(fd3)
      mydb.commit()
except:
      pass

try:
    s="create table BILL_RECORDS(CUSTOMER_CODE INT(4) PRIMARY KEY ,ORDER_DATE varchar(12),NAME CHAR(20),CONTACT_NO VARCHAR(10) ,COST INT(6),MODE_OF_PAYMENT CHAR(10))"
    mycursor.execute(s)
    mydb.commit()
except:
      pass

mydb = mysql.connector.connect(host="localhost",user="root", passwd="1234", database ="HOTEL_MANAGEMENT" )
mycursor=mydb.cursor()
try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="HOTEL_MANAGEMENT")
    mycursor = mydb.cursor()

    s = "INSERT INTO BILL_RECORDS (customer_code, order_date,name, contact_no, cost, mode_of_payment) VALUES (1000, '05/10/20', 'Dipak', 'NULL', 000, 'NULL')"
    mycursor.execute(s)
    mydb.commit()
    print("Record inserted successfully.")

except mysql.connector.Error as err:
    pass
    
    
    
def placeorder():
    cName = input("Enter your name: ")
    print("Welcome", cName)
    mob = None

    while True:
          mob = input("Enter mobile no: ")
          if len(mob) == 10 and mob.isnumeric():
            print("Valid mobile number:", mob)
            break
          else:
                print("Invalid mobile number. Please enter a 10-digit numeric mobile number.")
    while True:    
          print("Format: DD/MM/YYYY")
          date = input("Enter Date: ")
          if len(date) == 10 and date[2] == '/' and date[5] == '/':
                day, month, year = date.split('/')
                if day.isnumeric() and month.isnumeric() and year.isnumeric():
                      print("Valid date:", date)
                      break
                else:
                     print("Invalid date format. Day, month, and year should be numeric.")
          else:
                print("Invalid date format. Please enter a date in the format DD/MM/YYYY.")

    # Fetch the menu items
    s = "SELECT * FROM FOOD_MENU"
    mycursor.execute(s)
    n = mycursor.fetchall()
    
    print("| FOODCODE                | ITEM                       | PRICE            |")
    print("------------------------------------------------------------------")
    for item in n:
        print(f"|{item[0]:<24}|{item[1]:<30}|{item[2]:<18}|")

    a = []
    x = int(input("Enter Number Of Items: "))

    for _ in range(x):
          while True:
                y = int(input("Enter Food Code: "))
                z = int(input("Enter Quantity: "))
        
        # Fetch food details using placeholders
                sql = "SELECT foodcode, item, price, %s FROM food_menu WHERE foodcode = %s"
                mycursor.execute(sql, (z, y))
                data = mycursor.fetchone()
        
                if data is not None:
                      a.append(data)
                      break  # Valid input, exit the loop
                else:
                      print("Invalid input. Food code not found. Please re-enter.")


    # Initialize new_customer_code
    new_customer_code = None

    # Fetch the customer code
    D = "SELECT MAX(customer_code) FROM bill_records"
    mycursor.execute(D)
    data = mycursor.fetchone()

    if data[0] is not None:
        max_customer_code = data[0]
        new_customer_code = max_customer_code + 1
        print("New Customer Code:", new_customer_code)
    else:
        print("No records in the table.")

    print("1. UPI")
    print("2. Wallets")
    print("3. Credit/Debit/ATM Card")
    print("4. Cash")
    pay = int(input("Enter Mode Of Payment: "))
    xp = ' '
    
    if pay == 1:
        xp = "UPI"
    elif pay == 2:
        xp = "Wallets"
    elif pay == 3:
        xp = "Card"
    
    
    print("Payment Mode:", xp)
    print("Customer name:", cName)
    print("Mobile Number:", mob)
    
    
    print("Do You Want To Change:")
    print("1.Yes")
    print('2.NO')
    
    
    Q=int(input("Enter Choice:"))
    
    if Q==1:
          h = input("Enter your name: ")
          print("Welcome", cName)
          mob = int(input("Enter mobile no: "))
          print("Format: DD/MM/YYYY")
          date = input("Enter Date: ")

          a = []
          x = int(input("Enter Number Of Items: "))

          for _ in range(x):
                y = int(input("Enter Food Code: "))
                z = int(input("Enter Quantity: "))
          s = "SELECT foodcode, item, price, %s FROM food_menu WHERE foodcode = %s"
          mycursor.execute(s, (z, y))
          data = mycursor.fetchone()
          if data is not None:
            a.append(data)

    # Initialize new_customer_code
          new_customer_code = None

    # Fetch the customer code
          D = "SELECT MAX(customer_code) FROM bill_records"
          mycursor.execute(D)
          data = mycursor.fetchone()

          if data[0] is not None:
                max_customer_code = data[0]
                new_customer_code = max_customer_code + 1
                print("New Customer Code:", new_customer_code)
          else:
                print("No records in the table.")

          print("1. UPI")
          print("2. Wallets")
          print("3. Credit/Debit/ATM Card")
          print("4. Cash")
          pay = int(input("Enter Mode Of Payment: "))
          xp = ' '
    
          if pay == 1:
                xp = "UPI"
          elif pay == 2:
            xp = "Wallets"
          elif pay == 3:
            xp = "Card"
    
          else:
            print("Invalid Input")
          
          
          
          print("Payment Mode:", xp)
          print("Customer name:", cName)
          print("Mobile Number:", mob)
    
    elif Q==2:
          print("Your Order is:")
          print("_________________________________________________________")
          print("CUSTOMER CODE:", new_customer_code)
          print("Foodcode|        Item               |Price|Quantity|Cost")
          print("---------------------------------------------------------")

          r = []
          z = 0

          for item in a:
                foodcode, item_name, price, quantity = item
                cost = price * quantity
                r.append(cost)
                print(f"|{foodcode:<9}|{item_name:<25}|{price:<6}|{quantity:<8}|{cost:<4}|")
          for cost in r:
                z += cost

          print("__________________________________________________________")
          print("Total Amount Of Order =", z)

          discount = random.randint(5, 20)
          print(f"Congratulations You Got A Discount Of {discount}%")
          discounted_amount = int(z - (z * (discount / 100)))
          print(f"Now You Have To Pay: {discounted_amount}")
          
          l = f"INSERT INTO BILL_RECORDS (customer_code,  order_date, name, contact_no, cost, mode_of_payment) VALUES ({new_customer_code}, '{date}', '{cName}', {mob}, {discounted_amount}, '{xp}')"
          mycursor.execute(l)
          mydb.commit()

          print()
          print("Have A Nice Day")
    
    

def manager():
      print("1.UPDATE")
      print("2.DELETE")
      print("3.Insert")
      A=int(input("Enter Number Of What You Want:"))
      if A==1:
          D='Y'
          while D=="Y":
                  print("You Want To Update")
                  print("1.FoodCode")
                  print("2.FoodName")
                  print("3.Price")
                  print()
                  x=int(input("Enter Update Number:"))
                  if x==1:
                        k=int(input("Enter New Food Code:"))
                        R=int(input("Enter Old Food Code:"))
                        q="update food_menu set foodcode=%s where foodcode=%s "%(k,R)
                        mycursor.execute(q)
                        mydb.commit()
                        print("Successfully Updated")
                  elif x==2:
                        old=input("Enter Old Food Name:")
                        new=input("Enter New Food Name:")
                        que="update food_menu set item='%s' where item='%s' "%(new,old)
                        mycursor.execute(que)
                        mydb.commit()
                        print("Successfully Updated")
                  elif x==3:
                        op=int(input("Enter Food Code:"))
                        np=int(input("Enter New Price:"))
                        nop="update food_menu set price=%s where foodcode=%s "%(np,op)
                        mycursor.execute(nop)
                        mydb.commit()
                        print("Successfully Updated")
                  else:
                        print("Invalid Input")
                  D=input("Do You Want To Update More:Y/N")
      elif A==2:
        K="Y"
        while K=="Y":
              W=int(input("Enter Food Code:"))
              E="delete from food_menu where foodcode=%s "%W
              mycursor.execute(E)
              mydb.commit()
              print("Successfully Deleted")
              print()
              K=input("Do You Want To Delete More:Y/N")
      elif A==3:
        K="Y"
        while K=="Y":    
            q=[]
            a="select max(foodcode) from food_menu"
            mycursor.execute(a)
            data=mycursor.fetchone()
            for row in data:
                q.append(row)
                G=q[0]+1
            b=str(input("Enter Food Name"))
            c=int(input("Enter Food Price"))
            D="insert into food_menu values(%s,'%s',%s)"%(G,b,c)
            mycursor.execute(D)
      else:
        print("Invalid value")
      





def records():
      print("You Want To Check:")
      print("1.Total Sale")
      print("2.Sale By Date")
      print("3.Customer Detail")
      print()
      N=int(input("Enter Number According To What You Want To Check : "))
      if N==1:
            S="select sum(cost) from bill_records"
            mycursor.execute(S)
            data=mycursor.fetchone()
            for row  in data:
                  print("Total Sale")
            print(row)
      elif N==2:
            Q=[]
            q=int(input("Enter No Of Days"))
            for i in range(0,q):
                  e=str(input("Enter Date"))
                  A="select sum(cost) from bill_records where order_date='%s'"%e
                  mycursor.execute(A)
                  data=mycursor.fetchone()
                  for row  in data:
                        print("Date           | Totalcost")
                        print(e,          "|",row)
      elif N==3:
            P=[]
            u=int(input("Enter Customer Code:"))
            X="select * from bill_records where customer_code=%s"%u
            mycursor.execute(X)
            data=mycursor.fetchone()
            for row in data:
                  P.append(row)
            print()
            print("Customer Code:",P[0])
            print()
            print("Order Date:",P[1])
            print()
            print("Customer Name:",P[2])
            print()
            print("Contact Number:",P[3])
            print()
            print("Paid:",P[4])
            print()
            print("Mode Of Payment:",P[5])
      else:
            print("Invalid Input")

                  
def billrecords():
      Q="Select count(customer_code) from bill_records"
      mycursor.execute(Q)
      data=mycursor.fetchone()
      for row in data:
            print(row)
      P="select * from bill_records"
      mycursor.execute(P)
      for i in range(0,row):
            da=mycursor.fetchone()
            print("--------------------------------------------------")
            print("Record Number : ",i+1)
            print("Customer Code:",da[0])
            print()
            print("Order Date:",da[1])
            print()
            print("Customer Name:",da[2])
            print()
            print("Contact Number:",da[3])
            print()
            print("Paid:",da[4])
            print()
            print("Mode Of Payment:",da[5])
            print("--------------------------------------------------")
            print()
            print()
            
            
      R=int(input("Do You Want To Change In Records : "))
      print("Enter 1 For  Yes And  2 For No")
      if R==1:
             print("1.UPDATE")
             print("2.DELETE")
             A=int(input("Enter Choice:"))
             if A==1:
                   print("You Want To Update:")
                   print("1.Name")
                   print("2.Contact Number")
                   y=int(input("Enter choice :"))
                   if y==1:
                         g=str(input("Enter Name"))
                         c=int(input("Enter Customer Code"))
                         E="update bill_records set  name='%s' where customer_code=%s"%(g,c)
                         mycursor.execute(E)
                         mydb.commit()
                         print("SUCCESSFULLY UPDATED")
                   elif y==2:
                         D=int(input("Enter Customer Code:"))
                         x=int(input("Enter Contact Number :"))
                         V="update bill_records set  contact_no=%s where customer_code=%s"%(x,D)
                         mycursor.execute(V)
                         mydb.commit()
                         print("SUCCESSFULLY UPDATED")
                   else:
                         print("Invalid Input")
             elif A==2:
                    d=int(input("Enter Customer Code:"))
                    S="delete from bill_records where customer_code=%s"%d
                    mycursor.execute(S)
                    mydb.commit()
                    print("Successfully Deleted")
      elif R==2:
            print("Have A Great Time")
      else:
            print("Invalid Input")

print("Welcome to Billing System")
print("1. Place Order")
print("2. Manager")
print("3. Records")
print("4. Bill Records")

q = int(input("Enter Your Choice: "))

if q == 1:
      placeorder()
elif q == 2:
      manager()
elif q == 3:
      records()
elif q == 4:
      billrecords()
else:
      print("Program Terminated")



