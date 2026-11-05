
import mysql.connector as mysql
from datetime import datetime as dt

con=mysql.connect(host="localhost",
                  user="root",
                  password="chinni@123",
                  db="Bank")
class Bank:
    def save_transaction(self,acc_no,name,typ,amt,balance):
        cur=None
        try:
            date=dt.now()
            cur=con.cursor()
            query="insert into bank_transactions(acc_no,customer_name,transaction_type,amount,transaction_date,balance) values (%s,%s,%s,%s,%s,%s)"
            values=(acc_no,name,typ,amt,date,balance)
            cur.execute(query,values)
            con.commit()
        except mysql.Error as err:
            print("MySQL Error:",err)
            con.rollback()
            raise
        finally:
            if cur is not None:
                cur.close()
class CreateAccount(Bank):
    def operation(self):
        acc_no=int(input("Enter Account Number:"))
        name=input("Enter your Name:")
        amt=int(input("Enter Initial Deposit:"))
        if amt>0:
            self.save_transaction(acc_no,name,"Initial Deposit",amt,amt)
            print("Account Created Successfully")
        else:
            print("Invalid Amount")
class CheckBalance(Bank):
    def operation(self):
        cur=None
        try:
            acc_no=int(input("Enter the Account Number:"))
            cur=con.cursor()
            query="select balance from bank_transactions where acc_no=%s order by transaction_date desc limit 1"
            value=(acc_no,)
            cur.execute(query,value)
            result=cur.fetchone()
            if result:
                print("Current Balance:",result[0])
            else:
                print("Account Not Found")
        except mysql.Error as err:
            print("MySQL Error:",err)
            raise
        finally:
            if cur is not None:
                cur.close()
class Deposit(Bank):
    def operation(self):
        cur=None
        try:
            acc_no=int(input("Enter Account Number:"))
            amt=int(input("Enter Deposit Amount:"))
            cur=con.cursor()
            query="select customer_name,balance from bank_transactions where acc_no=%s order by transaction_date desc limit 1"
            value=(acc_no,)
            cur.execute(query,value)
            result=cur.fetchone()
            if result:
                if amt>0:
                    name=result[0]
                    balance=result[1]+amt
                    self.save_transaction(acc_no,name,"Deposit",amt,balance)
                    print("Deposit Successful")
                    print("Current Balance:",balance)
                else:
                    print("Invalid Amount")
            else:
                print("Account Not Found")
        except mysql.Error as err:
            print("MySQL Error:",err)
            raise
        finally:
            if cur is not None:
                cur.close()
class Withdraw(Bank):
    def operation(self):
        cur=None
        try:
            acc_no=int(input("Enter Account Number:"))
            amt=int(input("Enter Withdrawal Amount:"))
            cur=con.cursor()
            query="select customer_name,balance from bank_transactions where acc_no=%s order by transaction_date desc limit 1"
            value=(acc_no,)
            cur.execute(query,value)
            result=cur.fetchone()
            if result:
                if amt>0 and amt<=result[1]:
                    name=result[0]
                    balance=result[1]-amt
                    self.save_transaction(acc_no,name,"Withdraw",amt,balance)
                    print("Withdraw Successful")
                    print("Current Balance:",balance)
                else:
                    print("Insufficient Balance")
            else:
                print("Account Not Found")
        except mysql.Error as err:
            print("MySQL Error:",err)
            raise
        finally:
            if cur is not None:
                cur.close()
class Interest(Bank):
    def operation(self):
        cur=None
        try:
            acc_no=int(input("Enter Account Number:"))
            rate=float(input("Enter Interest Rate:"))
            time=float(input("Enter Time in Years:"))
            cur=con.cursor()
            query="select customer_name,balance from bank_transactions where acc_no=%s order by transaction_date desc limit 1"
            value=(acc_no,)
            cur.execute(query,value)
            result=cur.fetchone()
            if result:
                if rate>=0 and time>0:
                    name=result[0]
                    balance=result[1]
                    si=(balance*rate*time)/100
                    balance=balance+si
                    self.save_transaction(acc_no,name,"Interest",si,balance)
                    print("Simple Interest:",si)
                    print("Updated Balance:",balance)
                else:
                    print("Invalid Rate or Time")
            else:
                print("Account Not Found")

        except mysql.Error as err:
            print("MySQL Error:",err)
            raise

        finally:
            if cur is not None:
                cur.close()
class History(Bank):
    def operation(self):
        cur=None
        try:
            acc_no=int(input("Enter Account Number:"))
            cur=con.cursor()
            query="select transaction_type,amount,transaction_date,balance from bank_transactions where acc_no=%s"
            value=(acc_no,)
            cur.execute(query,value)
            result=cur.fetchall()
            if result:
                for row in result:
                    print("Transaction Type:",row[0])
                    print("Amount:",row[1])
                    print("Date:",row[2])
                    print("Balance:",row[3])
                    print("--------------------")
            else:
                print("No Transaction History")
        except mysql.Error as err:
            print("MySQL Error:",err)
            raise
        finally:
            if cur is not None:
                cur.close()
try:
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Simple Interest")
        print("6. Transaction History")
        print("7. Exit")
        c=int(input("Enter Your Choice:"))
        if c==1:
            bank=CreateAccount()
        elif c==2:
            bank=CheckBalance()
        elif c==3:
            bank=Deposit()
        elif c==4:
            bank=Withdraw()
        elif c==5:
            bank=Interest()
        elif c==6:
            bank=History()
        elif c==7:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
            continue
        try:
            bank.operation()
        except mysql.Error as err:
            print("Database Error:",err)
            con.rollback()
finally:
    if con.is_connected():
        con.close()
        print("Database Connection Closed")

# create this table in mysql
# create database Bank;

# use Bank;

# CREATE TABLE bank_transactions (
#     acc_no INT ,
#     customer_name VARCHAR(50),
#     transaction_type VARCHAR(30),
#     amount decimal(10,2),
#     transaction_date DATETIME,
#     balance decimal(10,2)
# );

# select * from bank_transactions;
