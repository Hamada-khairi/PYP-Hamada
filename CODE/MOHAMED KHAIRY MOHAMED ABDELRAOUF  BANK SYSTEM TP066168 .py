#Name: MOHAMED KHAIRY MOHAMED ABDELRAOUF 
#TP NO: TP066168
#The Super User Account is: 
#Super User Name: MuhammedSU
#Password :12345678



#The Main Logic Fuction
def main_menu():
    while True:
        print(
        "*==================================================*\n"
        "| ---------Welcome to Hamada's Bank Mangment------ |\n"
        "*==================================================*\n"
        "| =<< 1.            Open a new account         >>= |\n"
        "| =<< 2.                  login                >>= |\n"
        "| =<< 3.       Curnncey Converter Calculatour  >>= |\n"
        "| =<< 4.                Exit/Quit              >>= |\n"
        "*==================================================*\n"
    )


        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; ")


        if choiceNumber == "1":
            OPenAccMenu() # Open Account Menu  

        elif choiceNumber == "2":
            Login() 
        

        elif choiceNumber == "3":
            Currncy_Conv_Calc() #Currncy Converter Calculator 
            

        elif choiceNumber == "4":
            exit() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-4   |\n"
            "*===================*"
        )
        main_menu() 






#=======================================================================================================================================================================

#A Fuction That Displays The Open Account Menu
def OPenAccMenu():
    while True:
        print(
        "*==================================================*\n"
        "| ------- Welcome to Opening Account Menu -------- |\n"
        "*==================================================*\n"
        "| =<< 1.              Islamic Account          >>= |\n"
        "| =<< 2.              Current Account          >>= |\n"
        "| =<< 3.              Saving Account           >>= |\n"
        "| =<< 4.            Return to Manin Menu       >>= |\n"
        "*==================================================*\n"
    )

        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            IOPenAcc() # Islamic Open Account 
        
        elif choiceNumber == "2":
            COPenAcc() # Current Open Account 

        elif choiceNumber == "3":
            SaVOPenAcc() #Saving Open Account 

        elif choiceNumber == "4":
            main_menu() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-4   |\n"
            "*===================*"
        )
            return OPenAccMenu() 





#========================================================================================================================================================================

#A Fuction That Open An Account For Islamic Customer 
def IOPenAcc():
    print(
                "*=====================================*\n"
                "| -----Please Fill Up The Form------- |\n"
                "*=====================================*\n"
        )
    
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "ICU"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("Fourm.txt","a") as fh:
                recored = First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+str(Amount_Diposit)+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                    "*=======================================================================================================*\n"
                    "| -----Thank You For Filling Up The Form We Will Contact you in your email within 2 Busniss Days------- |\n"
                    "*=======================================================================================================*\n"
                )
            break
            
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )
        
        



#=======================================================================================================================================================================

#A Fuction That Open An Account For Saving Customer 
def SaVOPenAcc():
    print(
                "*=====================================*\n"
                "| -----Please Fill Up The Form------- |\n"
                "*=====================================*\n"
        )
    
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ") 
    AccType   = "SAV"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 100:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 100RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("Fourm.txt","a") as fh:
                recored = First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+str(Amount_Diposit)+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                    "*=======================================================================================================*\n"
                    "| -----Thank You For Filling Up The Form We Will Contact you in your email within 2 Busniss Days------- |\n"
                    "*=======================================================================================================*\n"
                )
            break
            
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )
            
        




#========================================================================================================================================================================

#A Fuction That Open An Account For Current Customer 
def COPenAcc():
    print(
                "*=====================================*\n"
                "| -----Please Fill Up The Form------- |\n"
                "*=====================================*\n"
        )
    
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ") 
    AccType   = "CCU"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("Fourm.txt","a") as fh:
                recored = First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+str(Amount_Diposit)+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                    "*=======================================================================================================*\n"
                    "| -----Thank You For Filling Up The Form We Will Contact you in your email within 2 Busniss Days------- |\n"
                    "*=======================================================================================================*\n"
                )
            break
            
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )
            
            
            
        


#=======================================================================================================================================================================

#A Fuction That Makes The Login Process
def Login():
    User_Name = input("\n=<< Enter Your User Name; ")
    Password  = input("=<< Enter Your PassWord; ")
    with open ("user_id & pass.txt","r") as fh:
        login_Details = "notfound"

        for recordline in fh:
            recoredlist = recordline.strip().split(";")
            if recoredlist[0] == User_Name and recoredlist[1] == Password:
                login_Details = recoredlist
                break

        if login_Details == "notfound":
            print(
                "*==================================================*\n"
                "| -- Incorrect User Name 0r password, try again -- |\n"
                "*==================================================*\n"
            )

        else:
            print(
                "*==============================*\n"
                "| -- Login successfull......-- |\n"
                "*==============================*\n"
            )
            if login_Details != "notfound":
                print(
         "\n*=================================================*\n"
        f"| --- Welcome to Hamada's Bank: {login_Details[4]} ----- |\n"
         "*=================================================*\n"
                )

            if login_Details[9] == "SU":
                Spuer_User_Menu(login_Details) 

            elif login_Details[9] == "AU":
                Admin_Menu(login_Details) 

            elif login_Details[9] == "CCU":
                Cureent_Customer_Menu(login_Details) 

            elif login_Details[9] == "ICU":
                Islamic_Customer_Menu(login_Details) 

            elif login_Details[9] == "SAV":
                Sa_aCC_Menu(login_Details) # Saving Account Menu 

            else:
                print(
                "*==================================================*\n"
                "| -- Incorrect User Name 0r password, try again -- |\n"
                "*==================================================*\n"
            )
                return login_Details






#=======================================================================================================================================================================

#A Fuction That Displays The Super User Menu
def Spuer_User_Menu(login_Details):
    while True:
        print(
        "*==================================================*\n"
        "| ---------- Welcome to Super User Menu ---------- |\n"
        "*==================================================*\n"
        "| =<< 1.      Display All Pending Accounts     >>= |\n"
        "| =<< 2.           Add Admin Account           >>= |\n"
        "| =<< 3.      Add Current Customer Acount      >>= |\n"
        "| =<< 4.      Add Islamic Customer Acount      >>= |\n"
        "| =<< 5.       Add Saving Customer Acount      >>= |\n"
        "| =<< 6.        Display All User Accounts      >>= |\n"
        "| =<< 7.          Change The Passsword         >>= |\n"
        "| =<< 8.          Change The User Name         >>= |\n"
        "| =<< 9.        Show All The TransAction       >>= |\n"
        "| =<< 10.           Return To Main Menu        >>= |\n"
        "| =<< 11.              Exit/Quit               >>= |\n"
        "*==================================================*\n"
    )
        

        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; ")

        if choiceNumber == "1":
            Display_All_Pending() 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "2":
            AddAdmin() 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "3":
            Add_CCU_ACC() #Add Current Customer User
            return Spuer_User_Menu(login_Details)

        
        elif choiceNumber == "4":
            Add_ICU_ACC()#Add Islamic Customer User 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "5":
            Add_Sa_aCC() #Add Saving Customer User 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "6":
            Display_All_US() #Display All The Users 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "7":
            Change_Pass(login_Details)# Change The Password 


        elif choiceNumber == "8":
            Change_User_Name(login_Details) 

        elif choiceNumber == "9":
            Show_All_Trans() # Show All Users TransAction 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "10":
            return main_menu() 

        elif choiceNumber == "11":
            exit() 

        else:
             print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-11   |\n"
            "*===================*\n"
        )
        return Spuer_User_Menu() 
        




#=======================================================================================================================================================================

#A Fuction That Add A New Admin Account
def AddAdmin():
    user_id = genid("Admin User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "AU"
    loan = "-"
    Amount_Diposit  = "-"
    while True:
        try:
            age = float(input("=<< Please Enter your age; "))
            break
        except ValueError:
            print("please Ennter A valid Age")
    while age >= 18:
        with open ("user_id & pass.txt","a") as fh:
            recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
            fh.write(recored)
            print(
                    "*==============================================================*\n"
                    "| -------The Admin Account Has Been Added Successfully-------- |\n"
                    "*==============================================================*\n"
            )
        break
    
    else:
        print(
            "*==================================================*\n"
            "| -----You Are To Young For Opening Account------- |\n"
            "*===================================================*"
        )
    




#=======================================================================================================================================================================

#A Fuction That Add A New Islamic Account
def Add_ICU_ACC():
    user_id = genid("Islamic Customer User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "ICU"
    loan = "-"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("user_id & pass.txt","a") as fh:
                recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                        "*================================================================*\n"
                        "| -------The Islamic Account Has Been Added Successfully-------- |\n"
                        "*================================================================*\n"
                )
            break
        
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )





#=======================================================================================================================================================

#A Fuction That Add A New Saving Account
def Add_Sa_aCC():
    user_id = genid("Saving Customer User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "SAV"
    loan = "-"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 100:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 100RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("user_id & pass.txt","a") as fh:
                recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                        "*===============================================================*\n"
                        "| -------The Saving Account Has Been Added Successfully-------- |\n"
                        "*===============================================================*\n"
                )
            break
        
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )





#=======================================================================================================================================================================

#A Fuction That Add A New Current Account
def Add_CCU_ACC():
    user_id = genid("Current Customer User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Emai; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "CCU"
    loan = "-"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("user_id & pass.txt","a") as fh:
                recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                        "*================================================================*\n"
                        "| -------The Current Account Has Been Added Successfully-------- |\n"
                        "*================================================================*\n"
                )
            break
        
        else:
            print(
                "*==================================================*\n"
                "| -----You Are To Young For Opening Account------- |\n"
                "*===================================================*"
            )
        
        



#=======================================================================================================================================================================

#A Fuction That Displays All The Users
def Display_All_US():
    allrec = []# = All Recored
    with open("user_id & pass.txt","r") as fh:
        for line in fh:
                allrec.append(line.strip().split(";"))
        print("="*157)
        print("|"+"Usre ID".center(10)+"|"+"User Password".center(15)+"|"+"Balance".center(15)+"|"+"Loan".center(10)+"|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(10)+"|"+"Email".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*157)
        for cnt in range(0,len(allrec)): #cnt Counter
            print("|"+allrec[cnt][0].center(10)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(10)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+allrec[cnt][8].center(15)+"|"+allrec[cnt][9].center(15)+"|"+allrec[cnt][10].center(10)+"|"+"\n")
        input("Press Enter to continue...\n")

                
    


#=======================================================================================================================================================================

#A Fuction That Displays All The Pendings Accounts Thats Need To be Opend
def Display_All_Pending():
    allrec = [] # = All Recored
    with open ("Fourm.txt","r") as fh:
        for line in fh:
            allrec.append(line.strip().split(";")) 
        print("="*124)
        print("|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(15)+"|"+"Email".center(15)+"|"+"Balance".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*124)
        for cnt in range(0,len(allrec)): #cnt Counter
            print("|"+allrec[cnt][0].center(15)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+"\n")
        input("Press Enter to continue...\n")
        




#=======================================================================================================================================================================

#A Fuction That Generate A New ID For A New Account
def genid(perm): # genid = Generate A New ID , Prem = premeter
    with open ("ID.txt","r") as IDfh:
        record = IDfh.readline()
        recordlist = record.strip().split(";")
        if perm == "Admin User":
            pref = "AU" #pref = Prefex 
            oldid = recordlist[0][2:]
        elif perm == "Current Customer User":
            pref = "CCU"
            oldid = recordlist[1][3:]
        elif perm == "Islamic Customer User":
            pref = "ICU"
            oldid = recordlist[2][3:]
        elif perm == "Saving Customer User":
            pref = "SAV"
            oldid = recordlist[3][3:]
        nextid = int(oldid) + 1
        if len(str(nextid)) == 1:
            newid = "0000" + str(nextid)
        elif len(str(nextid)) == 2:
            newid = "000" + str(nextid)
        elif len(str(nextid)) == 3:
            newid = "00" + str(nextid)
        elif len(str(nextid)) == 4:
            newid = "0" +str(nextid)
        elif len(str(nextid)) == 5:
            newid = str(nextid)
        newid = pref + newid
        if perm == "Admin User":
            recordlist[0] = newid
        else:
            recordlist[1] = newid
        record = ";".join(recordlist)
        with open ("ID.txt","w") as fh:
            fh.write(record)
            return newid
            





#=======================================================================================================================================================================

#A Fuction That Displays The Admin Customer Menu
def Admin_Menu(login_Details):
    while True:
        print(
        "*==================================================*\n"
        "| ---------- Welcome to Admin User Menu ---------- |\n"
        "*==================================================*\n"
        "| =<< 1.      Add Current Customer Acount      >>= |\n"
        "| =<< 2.       Add Islamic Customer Acount     >>= |\n"
        "| =<< 3.      Display All Pending Accounts     >>= |\n"
        "| =<< 4.          Change The Passsword         >>= |\n"
        "| =<< 5.          Change The User Name         >>= |\n"
        "| =<< 6.        Show All The TranAction        >>= |\n"
        "| =<< 7.       Add Saving Customer Acount      >>= |\n"
        "| =<< 8.           Return To Main Menu         >>= |\n"
        "| =<< 9.               Exit/Quit               >>= |\n"
        "*==================================================*\n"
    )
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            Add_CCU_ACC()#Add Current Customer User 
            return Admin_Menu(login_Details) 
        
        elif choiceNumber == "2":
            Add_ICU_ACC()#Add Islamic Customer User 
            return Admin_Menu(login_Details) 

        elif choiceNumber == "3":
            Display_All_Pending() 
            return Admin_Menu(login_Details) 
        
        elif choiceNumber == "4":
            Change_Pass(login_Details)# Change The Password 
            return Admin_Menu(login_Details) 

        elif choiceNumber == "5":
            Change_User_Name(login_Details) 
            return Admin_Menu(login_Details) 


        elif choiceNumber == "6":
            Show_All_Trans()# Show All Users TransAction 
            return Admin_Menu(login_Details) 


        elif choiceNumber == "7":
            Add_Sa_aCC() #Add Saving Customer User 
            return Admin_Menu(login_Details) 

        elif choiceNumber == "8":
            return main_menu() 

        elif choiceNumber == "9":
            exit() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-9   |\n"
            "*===================*\n"
        )
            return Admin_Menu() 





#=======================================================================================================================================================================

#A Fuction That Calculate & Convert The RM into Diffrent Currency's
def Currncy_Conv_Calc():
    while True:
        print(
        "*==========================================================*\n"
        "| ---------- Curnncey Converter Calculatour Menu --------- |\n"
        "*==========================================================*\n"
        "| =<< 1.                    US Dollar                  >>= |\n"
        "| =<< 2.                  Kuwaiti dinar                >>= |\n"
        "| =<< 3.                      Euro                     >>= |\n"
        "| =<< 4.                Indonesian Rupiah              >>= |\n"
        "| =<< 5.                  chinese yuan                 >>= |\n"
        "| =<< 6.               Return To Main Menu             >>= |\n"
        "| =<< 7.                    Exit/Quit                  >>= |\n"
        "*==========================================================*\n"
    )
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")

        if choiceNumber == "1":
            Amount = float(input("Please Enter The You wan't to convert From RM To USD; "))
            result = Amount   * 0.24
            print(f"The Amount is; {result} $")

        elif choiceNumber == "2":
            Amount = float(input("Please Enter The You wan't to convert From RM To KD; "))
            result = Amount   * 0.072
            print(f"The Amount is; {result} KD")

        elif choiceNumber == "3":
            Amount = float(input("Please Enter The You wan't to convert From RM To EU; "))
            result = Amount   * 0.21
            print(f"The Amount is; {result} €")

        elif choiceNumber == "4":
            Amount = float(input("Please Enter The You wan't to convert From RM To IDR; "))
            result = Amount   * 3394.01
            print(f"The Amount is; {result} Rp")

        elif choiceNumber == "5":
            Amount = float(input("Please Enter The You wan't to convert From RM To CNY; "))
            result = Amount   * 1.50
            print(f"The Amount is; {result} ¥")

        elif choiceNumber == "6":
            main_menu() 

        elif choiceNumber == "7":
            exit() 
            
        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-7   |\n"
            "*===================*\n"
        )
        Currncy_Conv_Calc() 

    




#=======================================================================================================================================================================

#A Fuction That Displays The Current Customer Menu
def Cureent_Customer_Menu(login_Details):
    while True:
        print(
        "*=====================================================*\n"
        "| ---------- Welcome to Customer User Menu ---------- |\n"
        "*=====================================================*\n"
        "| =<< 1.             Withdrawing Money            >>= |\n"
        "| =<< 2.             Depositing Money             >>= |\n"
        "| =<< 3.            Display My Details            >>= |\n"
        "| =<< 4.                loan Menu                 >>= |\n"
        "| =<< 5.           Change The Password            >>= |\n"
        "| =<< 6.             Pay Monthly Loan             >>= |\n"
        "| =<< 7.             Report Statement             >>= |\n"
        "| =<< 8.             Return To Main Menu          >>= |\n"
        "| =<< 9.                 Exit/Quit                >>= |\n"
        "*=====================================================*\n"
    )
    
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            WithDrraw(login_Details) 
            

        elif choiceNumber == "2":
            Deposit(login_Details) 

        elif choiceNumber == "3":
            Display_Details(login_Details) 

        elif choiceNumber == "4":
            Current_Loan_Menu(login_Details) 

        elif choiceNumber == "5":
            Change_Pass(login_Details) 

        elif choiceNumber == "6":
            pay_The_Loan(login_Details) 

        elif choiceNumber == "7":
            Report(login_Details) 

        elif choiceNumber == "8":
            return main_menu() 

        elif choiceNumber == "9":
            exit() 


        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-8   |\n"
            "*===================*\n"
        )
            Cureent_Customer_Menu() 





#=======================================================================================================================================================================

#A Fuction That Displays The Islamic Customer Menu
def Islamic_Customer_Menu(login_Details):
    while True:
        print(
        "*=============================================================*\n"
        "| ---------- Welcome to Islamic Customer User Menu ---------- |\n"
        "*=============================================================*\n"
        "| =<< 1.                 Withdrawing Money                >>= |\n"
        "| =<< 2.                 Depositing Money                 >>= |\n"
        "| =<< 3.                 Display My Details               >>= |\n"
        "| =<< 4.                 Islamic loan Menu                >>= |\n"
        "| =<< 5.                Change The Passsword              >>= |\n"
        "| =<< 6.                 Pay Monthly Loan                 >>= |\n"
        "| =<< 7.                  Report Statement                >>= |\n"
        "| =<< 8.                Return To Main Menu               >>= |\n"
        "| =<< 9.                    Exit/Quit                     >>= |\n"
        "*=============================================================*\n"
    )
    
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            WithDrraw(login_Details) 

        elif choiceNumber == "2":
            Deposit(login_Details) 

        elif choiceNumber == "3":
            Display_Details(login_Details) 

        elif choiceNumber == "4":
            Islamic_Loan_Menu(login_Details) 

        elif choiceNumber == "5":
            Change_Pass(login_Details) 

        elif choiceNumber == "6":
            pay_The_Loan(login_Details) 
        
        elif choiceNumber == "7":
            Report(login_Details) 

        elif choiceNumber == "8":
            return main_menu() 

        elif choiceNumber == "9":
            exit() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-9   |\n"
            "*===================*\n"
        )
            return Islamic_Customer_Menu() 





#=======================================================================================================================================================================

#A Fuction That Display's All Account Details
def Display_Details(login_Details):
    allrec = []
    with open("user_id & pass.txt","r") as fh:
        for line in fh:
                allrec.append(line.strip().split(";"))
        print("="*157)
        print("|"+"Usre ID".center(10)+"|"+"User Password".center(15)+"|"+"Balance".center(15)+"|"+"Loan".center(10)+"|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(10)+"|"+"Email".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*157)
        for cnt in range(0,len(allrec)):
            if (login_Details[0] == allrec[cnt][0]) :
                    print("|"+allrec[cnt][0].center(10)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(10)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+allrec[cnt][8].center(15)+"|"+allrec[cnt][9].center(15)+"|"+allrec[cnt][10].center(10)+"|"+"\n")
        input("Press Enter to continue...")




#=======================================================================================================================================================================

#A Fuction That Display's The Saving Account Menu
def Sa_aCC_Menu(login_Details):
    while True:
        print(
        "*============================================================*\n"
        "| ---------- Welcome to Saving Customer User Menu ---------- |\n"
        "*============================================================*\n"
        "| =<< 1.                 Depositing Money                >>= |\n"
        "| =<< 2.                 withdrawl  Money                >>= |\n"
        "| =<< 3.                 Display My Details              >>= |\n"
        "| =<< 4.                Change The Password              >>= |\n"
        "| =<< 5.                  Report Statement               >>= |\n"
        "| =<< 6.                Return To Main Menu              >>= |\n"
        "| =<< 7.                    Exit/Quit                    >>= |\n"
        "*============================================================*\n"
    )
    
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")



        if choiceNumber == "1":
            Deposit(login_Details) 

        elif choiceNumber == "2":
            WithDrraw(login_Details) 


        elif choiceNumber == "3":
            Display_Details() 


        elif choiceNumber == "4":
            Change_Pass(login_Details) 


        elif choiceNumber == "5":
            Report(login_Details) 


        elif choiceNumber == "6": 
            main_menu() 


        elif choiceNumber == "7":
            exit() 


        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-7   |\n"
            "*===================*\n"
        )
            return Sa_aCC_Menu() 





#=======================================================================================================================================================================

#A Fuction That Make The Withdraw TransAction For The Customers
def WithDrraw(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        while True:
            try:
                balance = float(input("=<< Please Enter The Amount you want to Withdraw; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt #cnt = Counter
                    break
        if balance < float(allrec[ind][2]):
            old_balance = allrec[ind][2]
            New_amount = float(old_balance) - balance
            allrec[ind][2] = str(New_amount)
            with open("user_id & pass.txt","w") as fh:
                    nor = len(allrec)
                    for cnt in range(0,nor):
                        rec = ";".join(allrec[cnt])+"\n"
                        fh.write(rec)
                    print(
                "*==============================================*\n"
                "| -----Your Have withdrawed Succsefully------- |\n"
                "*==============================================*\n")
                    print(
                "*===================================================*\n"
                f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
                "*===================================================*\n")
                    with open("Transaction.txt", "a") as fh:
                            Withdraw = str(balance)
                            money = str(New_amount)
                            ID = str(allrec[ind][0])
                            with open("Transaction.txt", "a") as fh:
                                rec = "Withdraw"";""-"+Withdraw+";"+money+";"+ID+";"+date+"\n"
                                fh.write(rec)
                        
        else:
            print(
                "*==================================================*\n"
                "| ------------You don't Have Enogh Money----------- |\n"
                "*===================================================*"
            )
            return WithDrraw(login_Details)
        




#=======================================================================================================================================================================

#A Fuction That Make The Deposit TransAction For The Customers
def Deposit(login_Details):
    allrec = [] # = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:#Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        while True:
            try:
                balance = float(input("=<< Please Enter The Amount you want to Deposit; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        ind = -1#ind = index
        nor = len(allrec)#nor = Number of The Recoreds
        for cnt in range(0,nor): #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        if balance < 10000:
            old_balance = allrec[ind][2]
            New_amount = float(old_balance) + balance
            allrec[ind][2] = str(New_amount)
            with open("user_id & pass.txt","w") as fh:
                    nor = len(allrec)
                    for cnt in range(0,nor):
                        rec = ";".join(allrec[cnt])+"\n"
                        fh.write(rec)
                    print(
                "*==============================================*\n"
                "| -------Your Have Diposit Succsefully-------- |\n"
                "*==============================================*")
                    print(
                "*===================================================*\n"
                f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
                "*===================================================*\n")
                    with open("Transaction.txt", "a") as fh:
                                Deposite = str(balance)
                                money = str(New_amount)
                                ID = str(allrec[ind][0])
                                with open("Transaction.txt", "a") as fh:
                                    rec = "Deposit"";""+"+Deposite+";"+money+";"+ID+";"+date+"\n"
                                    fh.write(rec)
                        
        else:
            print(
                "*=========================================================*\n"
                "| -------You Can't deposit more than 10000 RM a Day------- |\n"
                "*=========================================================*")
            return Deposit(login_Details)





#=======================================================================================================================================================================

#A Fuction That Change The Password For The Super, Admin and Customer Users
def Change_Pass(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:#Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        newpass = input("=<< Please Enter The new Password; ")
        ind = -1 #ind = index
        nor = len(allrec)#nor = Number of The Recoreds
        for cnt in range(0,nor):  #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        allrec[ind][1] = newpass
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
            "*====================================================================*\n"
            "| ------------Your Password Have Been Changed Succsefully----------- |\n"
            "*====================================================================*"
                )





#=======================================================================================================================================================================

#A Fuction That Change The User Name Avilibale Only For The Super And Admin User
def Change_User_Name(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh: #Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        newpass = input("=<< Please Enter The New User Name; ")
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):  #Cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        allrec[ind][0] = newpass
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
            "*=================================================================*\n"
            "| ------------Your User Name Have Changed Succsefully------------ |\n"
            "*=================================================================*"
        )





#=======================================================================================================================================================================

#A Fuction That Displays A Menu The Loan of Current Account 
def Current_Loan_Menu(login_Details):
    print(
                "*===============================================*\n"
                "| --             Enter Loan Type             -- |\n"
                "*===============================================*\n"
                "| =<< 1. Education Loan (Interest Rate; 1%) >>= |\n"
                "| =<< 2.     Car Loan (Interest Rate; 6%)   >>= |\n"
                "| =<< 3.    Home Loan (Interest Rate; 2%)   >>= |\n"
                "| =<< 4.  Personal Loan (Interest Rate; 8%) >>= |\n"
                "| =<< 5.          Back to Menu              >>= |\n"
                "*===============================================*\n"
   )

    choiceNumber = input("=<< Choose loan type; ")

    if choiceNumber == "1":
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        interestRate = float(1 / 100 / 12)
        loanPayment = round(loanAmount * (interestRate * (1 + interestRate) ** years) / (
                        (1 + interestRate) ** years - 1))
            
        print(
                    "*=======================================*\n"
                    f"| The monthly payment is {loanPayment:.2f} RM |\n"
                    "*=======================================*\n"
            )
        status_loop = True
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
    
    
    elif choiceNumber == '2':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        interestRate = float(6 / 100 / 12)
        loanPayment = loanAmount * (interestRate * (1 + interestRate) ** years) / (
                (1 + interestRate) ** years - 1)
        print(
            "*==========================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |\n"
            "*==========================================*\n"
        )

        status_loop = True
        
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
                    
    
    elif choiceNumber == '3':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        interestRate = float(2 / 100 / 12)
        loanPayment = loanAmount * (interestRate * (1 + interestRate) ** years) / (
                (1 + interestRate) ** years - 1)
        print(
            "*==========================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |"
            "*==========================================*\n"
        )

        status_loop = True
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
                

    elif choiceNumber == '4':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        interestRate = float(8 / 100 / 12)
        loanPayment = round(loanAmount * (interestRate * (1 + interestRate) ** years) / (
                (1 + interestRate) ** years - 1))
        print(
            "*============================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |\n"
            "*============================================*\n"
        )
        status_loop = True
        while status_loop:
            while status_loop:
                status = input("=<< Approve Or Reject Loan Status; ")
                if status == "Approve":
                    loan_deposit(login_Details,loanPayment,loanAmount,date) 
                    break

                elif status == "Reject":
                    print(
                                "*===============================*\n"
                                "| The Payment has been rejected |\n"
                                "*===============================*\n"
                    )

                else:
                    print(
                                "*============================*\n"
                                "| Incorrect input, try again |\n"
                                "*============================*\n"
                    )



    elif choiceNumber == '5':
        main_menu() 
    

    else:
        print(
                    "*********************\n"
                    "| Invalid option    |\n"
                    "| Choose from 1-5   |\n"
                    "*********************"
        )
        Current_Loan_Menu()




#=======================================================================================================================================================================

#A Fuction That Display a Menu For The Loan OF The Islamic Account 
def Islamic_Loan_Menu(login_Details):
    print(
                "*===============================================*\n"
                "| --             Enter Loan Type             -- |\n"
                "*===============================================*\n"
                "| =<< 1. Education Loan (Interest Rate; 0%) >>= |\n"
                "| =<< 2.     Car Loan (Interest Rate; 0%)   >>= |\n"
                "| =<< 3.    Home Loan (Interest Rate; 0%)   >>= |\n"
                "| =<< 4.  Personal Loan (Interest Rate; 0%) >>= |\n"
                "| =<< 5.          Back to Menu              >>= |\n"
                "*===============================================*\n"
   )

    choiceNumber = input("=<< Choose loan type; ")

    if choiceNumber == "1":
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        loanPayment = float(loanAmount / 12)
        print(
                    "*=======================================*\n"
                    f"| The monthly payment is {loanPayment:.2f} RM |\n"
                    "*=======================================*\n"
            )
        status_loop = True
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
                
    
    elif choiceNumber == '2':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        loanPayment = float(loanAmount / 12)
        print(
            "*======================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |\n"
            "*======================================*\n"
        )

        status_loop = True
        
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
                    
                
    
    elif choiceNumber == '3':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        loanPayment = float(loanAmount / 12)
        print(
            "*==========================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |\n"
            "*==========================================*\n"
        )

        status_loop = True
        
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )
                
    
    elif choiceNumber == '4':
        while True:
            try:
                loanAmount = float(input("=<< Enter loan amount; "))
                terms = float(input("=<< Enter loan terms in years; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        years = float(terms * 12)
        loanPayment = float(loanAmount / 12)
        print(
            "*==========================================*\n"
            f"| The monthly payment is {loanPayment:.2f} RM |\n"
            "*==========================================*\n"
        )

        status_loop = True
        
        while status_loop:
            status = input("=<< Approve Or Reject Loan Status; ")
            if status == "Approve":
                loan_deposit(login_Details,loanPayment,loanAmount,date) 
                break

            elif status == "Reject":
                print(
                            "*===============================*\n"
                            "| The Payment has been rejected |\n"
                            "*===============================*\n"
                )

            else:
                print(
                            "*============================*\n"
                            "| Incorrect input, try again |\n"
                            "*============================*\n"
                )



    elif choiceNumber == '5':
        main_menu() 
    

    else:
        print(
                    "*********************\n"
                    "| Invalid option    |\n"
                    "| Choose from 1-5   |\n"
                    "*********************"
        )
        Current_Loan_Menu() 





#=======================================================================================================================================================================

#A Fuction That Deposit The Loan Amount Into The Custoumer Account
def loan_deposit(login_Details,loanPayment,loanAmount,date):
    allrec = [] # = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh: #Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):  #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        old_balance = allrec[ind][2]
        New_amount = float(old_balance) + float(loanAmount)
        allrec[ind][2] = str(New_amount)
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
            "*==============================================*\n"
            "| -------Your Have Loaned Succsefully-------- |\n"
            "*==============================================*"
        )
                print(
            "*===================================================*\n"
            f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
            "*===================================================*\n"
        )
        loan_deposit_pay(loanPayment,login_Details,date,loanAmount) 
                    
    
                
        
                    
#=======================================================================================================================================================================

#A Fuction That Saves The Monthly Loan ON The Custoers That He Need To Pay
def loan_deposit_pay(loanPayment,login_Details,date,loanAmount):
    allrec = [] # = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:#Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):  #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        New_amount = loanPayment
        allrec[ind][3] = str(New_amount)
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
                "*==================================================================*\n"
                f"| -----You Need To Pay; {allrec[ind][3]} By The Next Month------- |\n"
                "*==================================================================*\n")
                with open("Transaction.txt", "a") as fh:
                                Deposite = str(loanAmount)
                                money = str(New_amount)
                                ID = str(allrec[ind][0])
                                with open("Transaction.txt", "a") as fh:
                                    rec = "Loan"";""+"+Deposite+";"+money+";"+ID+";"+date+"\n"
                                    fh.write(rec)
                
        



#=======================================================================================================================================================================

#A Fuction That Make The Customer Pay The Monthly Loan On Him
def pay_The_Loan(login_Details):
    date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
    while "/" not in date:
        date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
    allrec = [] # = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh: #Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):  #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        if str(allrec[ind][2]) != "-":
            if float(allrec[ind][2]) >= float(allrec[ind][3]):
                old_balance = allrec[ind][2]
                New_amount = float(old_balance) - float(allrec[ind][3])
                allrec[ind][2] = str(New_amount)
                with open("user_id & pass.txt","w") as fh:
                        nor = len(allrec)
                        for cnt in range(0,nor):
                            rec = ";".join(allrec[cnt])+"\n"
                            fh.write(rec)
                        print(
                    "*==============================================*\n"
                    "| -------Your Have Payed Succsefully-------- |\n"
                    "*==============================================*"
                )
                        print(
                    "*===================================================*\n"
                    f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
                    "*===================================================*\n")
                        with open("Transaction.txt", "a") as fh:
                                    Withdraw = str(allrec[ind][3])
                                    money = str(New_amount)
                                    ID = str(allrec[ind][0])
                                    with open("Transaction.txt", "a") as fh:
                                        rec = "Loan Pay"";""-"+Withdraw+";"+money+";"+ID+";"+date+"\n"
                                        fh.write(rec)



            else:
                print("*=================================================*\n"
                      "| -------You Don't Have Enough Money To Pay------ |\n"
                      "*=================================================*")
        else:
            print("*==============================================*\n"
                  "| -------You Don't Have Any Thing To Pay------ |\n"
                  "*==============================================*")
                            




#=======================================================================================================================================================================

#A Fuction That Diplays For Customer His Transactions 
def Report(login_Details):
    allrec = [] # = All Recored
    with open("Transaction.txt","r") as fh:
        for line in fh:
            allrec.append(line.strip().split(";"))
    print("="*85)
    print("Type OF Transaction".center(30)+"|"+"Amount".center(15)+"|"+"Balance".center(15)+"|"+"User ID".center(15)+"|"+"Date Of Tranaction".center(20)+"|")
    print("="*85)
    for cnt in range(0,len(allrec)):  #cnt = Counter
        if (login_Details[0] == allrec[cnt][3]):
            print(allrec[cnt][0].center(30)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(20)+"|")
    input("Press Enter to continue...")
        




#=======================================================================================================================================================================

#A Fuction That Show All the transacrions of Customer
def Show_All_Trans():
    allrec = []
    with open("Transaction.txt","r") as fh:
        for line in fh:
            allrec.append(line.strip().split(";"))
        print("="*98)
        print("Type OF Transaction".center(30)+"|"+"Amount".center(15)+"|"+"Balance".center(15)+"|"+"User ID".center(15)+"|"+"Date Of Tranaction".center(20)+"|")
        print("="*98)
        for cnt in range(0,len(allrec)):  #cnt = Counter)
            print(allrec[cnt][0].center(30)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(20)+"|")
    input("Press Enter to continue...")










main_menu() 



























































































#Good By No Of The Line