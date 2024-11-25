heading="Bank Management System"
print(heading)
bankaccount={}
 
def createaccount():
    print("Create Your New Account")
    email=input("enter Your mail id  : ")
    if (email==bankaccount):
        print("An Account with this email id already exist")
        return
    
    name=input("Enter Name : ")
    age=int(input("Enter Age "))
    address=input("Enter Your Address")
    mobile=int(input("Enter Your Number"))
    gender=input("Enter Number  : ")

    bankaccount[email]={
        "name":name,
        "age":age,
        "address":address,
        "mobile":mobile,
        "gender":gender,
        "balance":0.0,            
    }

    print("Account Created Successfully")

def viewaccount():
    print("view your Account Details : ")
    email=input("Enter Your Email id to login : ")

    if email != bankaccount:
        print("no account is found with this email id : ")
        return
    
    details=bankaccount[email]
    print("Account Details For {email}: ")
    for key,value in details.item():
        print("{key}:{value}")
    
def creditamount():
        print("Credit Amount")
        email=input("Enter Your Email ID : ")

        if email !=bankaccount:
            print("no account is found with this email id : ")
            return
        amount = float(input("Enter Amount to be Credit: "))
        bankaccount[email]["balance"] += amount
        print("Amount Credit Successfully New Balanace: {bankaccount[email]}")
def debitamount():
        print("debit amount")
        email=input("Enter Your email id : ")
        if email != bankaccount:
            print("no account is found with this email id : ")
            return
        
        amount=float(input("Enter Amount to be debit: "))
        if amount>bankaccount[email]["balance"]:
            print("Insufficient balance ")
        else:
            bankaccount[email]["balance"] -= amount
            print("Amount Credit Successfully New Balanace: {bankaccount[email]}")

def deleteaccount():
        print("Delete Account")
        email=input("Enter YOur Email ID to delete :")
       
        if email != bankaccount:
            print("no account is found with this email id : ")
            return
        
        confirm=input("Are Your Sure to delete this account")
        if confirm=="yes":
            del bankaccount[email]
            print("Account deleted Successfully")
        else:
            print("Account Deletion Cancelled")
def main():
    while True:
        print("\nBank Management System ")
        print("1. Create Account")
        print("2. View Acoount")
        print("3. Credit Amount")
        print("4. Debit Amount")
        print("5. Delete Account")
        print("6. Exit ")
        choice =input("Enter Your Choice: ")

        if choice == "1":
            createaccount()
        elif choice == "2":
            viewaccount()
        elif choice =="3":
            creditamount()
        elif choice == "4":
            debitamount()
        elif choice == "5":
            deleteaccount()
        elif choice == "6":
                print("Exit the System. Thank you")
                break
        else:
                print("Invalid Choice . Please Try Again")

if __name__== "__main__":
    main()

