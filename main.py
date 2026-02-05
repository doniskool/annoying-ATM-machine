print("Hello welcome to mors mutual bank. balance = 1, deposit = 2, withdrawal = 3, cancel = 4.\n")
password = 5413
balance = 1119
choice=0 
deposit = 0
withdraw = 438
pin = int(input("Enter your 4 digit pin\n"))
if pin == password: 
   while choice == 4:
   
    print(" \n**** menu ****\n ")
    print("1 == balance")
    print("2 == deposit")
    print("3 == withdrawal")
    print("4 == cancel\n")

choice=int(input("\nEnter your option please\n 1-4\n "))
if choice == 1:
  print("Balance = $", balance)
elif choice == 2:
  input("how much do you want to deposit?(Enter here): ")
  print("Thank you for depositing.")
elif choice == 3:
  input("how much would you like to withdraw? (Enter amount here): ")
  print("Thank you for withdrawing.")
elif choice == 4:
  print("Have a good day!")
