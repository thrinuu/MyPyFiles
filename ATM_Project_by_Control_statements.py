print("welcome to bank atm")
restart=('y')
chances=3
balance=699

while chances>=0:
    pin=int(input("Enter your PIN \n"))
    
    if pin==(1234):
        print("you entered currectly \n")
        
        while restart not in ('n','N','No'):
            print("Press 1 for balance enquiry \n")
            print("Press 2 for balance withdrawl \n")
            print("Press 3 for Pay_in \n")
            print("Press 4 for return cord \n")
            
            option=int(input("Choose an options for furtherly ?"))
            
            if option==1:
                print("Your available balance is RS : ",balance,'\n')
                restart=input("will go back? (Y/N) ")
                if restart in ('n','N','No'):
                  print("Thank You")
                  break
                
            elif option==2:
                option2=('y')
                withdrawl= float(input("Enter Your Desered withdrawl amount \n Rs 10 / Rs 200 /RS 500 /Rs 1000"))

                if withdrawl in [10,50,100,200,300,400,500,1000,2000]:
                  balance= balance-withdrawl
                  print("\n Current Available Balance is Rs", balance)
                  restart= input("will go back? (Y/N)")

                  if restart in ('n','no','N'):
                      print("Thank You")
                      break

                elif withdrawl [7,35,59,45,63,67,86,88,99,150,120]:
                    print("Insufficient amount \n")
                    restart=('y')

                elif withdral==1:
                    withdrawl=float (input("Please enter your desered withdrawl amount :"))

            elif option==3:
                pay_in = float(input("how much would you like to Pay In PyBank"))
                balance= balance + pay_in
                print("\n Your available balance RS:",balance)
                restart= input("will you go back ?(Y/N) ")
                if restart in ('n','N','No'):
                    print("Thank You")
                    break

            elif option==4:
                print("please wait cord is processing.......")
                print("THANK YOU FOR SERVICE")
                break

            else:
              print("Please Enter correct number. \n")
              restart = ('y')
    
    if chances==0:
        print("\n No more tries")
        break

