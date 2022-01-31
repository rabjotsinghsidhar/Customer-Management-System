
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="tiger1000", database="TestDB")
myCursor = con.cursor()
myCursor.execute("USE TestDB")

class Customer:

    def __init__(self):
        self.id = 0  # Instance variable
        self.name = ""
        self.items = ""
        self.bill = 0

    def addCus(self):
        myCursor = con.cursor()
        strQuery = "insert into customer values(%s,%s,%s,%s)"
        customer1=(self.id, self.name, self.items, self.bill)
        myCursor.execute(strQuery,customer1)
        con.commit()

    def modifyCus(self):
        myCursor = con.cursor()
        strQuery = "update Customer set name=%s, items=%s,bill=%s where id=%s"
        rowaffected = myCursor.execute(strQuery, (self.name, self.items, self.bill, self.id))
        con.commit()
        if (rowaffected == 0):
            raise Exception("The customer id doesn't exist")

    def searchCustomer(self):
        myCursor = con.cursor()
        strQuery = "select * from Customer where id=%s"
        rowaffected = myCursor.execute(strQuery,(self.id,))
        if (rowaffected == 0):
            raise Exception("The customer id doesn't exist")
        data = myCursor.fetchone()
        self.name = data[1]
        self.items = data[2]
        self.bill = data[3]

    def deleteCustomer(self):
        myCursor = con.cursor()
        strQuery = "delete from Customer where id=%s"
        rowaffected = myCursor.execute(strQuery,(self.id,))
        con.commit()
        if (rowaffected == 0):
            raise Exception("The customer id doesn't exist")

    def displayCustomer(self):
        myCursor = con.cursor()
        strQuery = "select * from customer"
        myCursor.execute(strQuery)
        print("ID     Name     item    Bill")
        for row in myCursor.fetchall():
            for cell in row:
                print(cell, end='\t')
            print()


cus= Customer()

if(__name__=="__main__"):
    while(1):
        print("\tEnter 1 to add New customer")
        print("\tEnter 2 to search customer by id")
        print("\tEnter 3 to Modify customer by id")
        print("\tEnter 4 to Delete customer by id")
        print("\tEnter 5 to display all customer")
        print("\tEnter 6 to Exit")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            cus=Customer()
            cus.id=int(input("Enter Customer id: "))
            cus.name=input("Enter Name: ")
            cus.items=input("Enter items: ")
            cus.bill=int(input("Enter Bill Amount: "))
            Customer.addCus(cus)  #Calling Function 

        elif(choice==2):
            try:
                cus=Customer()
                cus.id=int(input("Enter Id of customer to be searched: "))
                cus.searchCustomer() #Calling function Syntax 2
                print("Customer Name=",cus.name,"\nCustomer items=",cus.items,"\nCustomer Bill=",cus.bill)
            except Exception as ex:
                print(ex)

        elif(choice==3):
            try:
                cus=Customer()
                cus.id=int(input("Enter Id of customer to be modified: "))
                cus.name=input("Enter  new name: ")
                cus.items=input("Enter New items: ")
                cus.bill=input("Enter new Billing Amount: ")
                cus.modifyCus() #Calling function 
                print("Data Modified successully")
            except Exception as ex:
                print(ex)

        elif(choice==4):
            cus=Customer()
            cus.id=int(input("Enter Id of customer to be deleted: "))
            Customer.deleteCustomer(cus)
            print("Customer Deleted successully \n")


        elif(choice==5):
            cus=Customer()
            cus.displayCustomer()
            ch=input("Do you want to continue? \n Enter 'Y/y/1'- Yes and 'N/n' - No :")
            if(ch=='y' or ch=='Y' or ch=='1'):
                continue
            else:
                break
                exit()
        elif(choice==6):
            break
            exit()



