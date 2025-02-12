import socket,pickle

#Socket connection
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 5555))

#Getting Respose from server regarding Connection through message
connectionmsg = clientsocket.recv(4096).decode()
print("\n",connectionmsg)

#Function for Displaying Menu
def display_menu():
    print("\n------------Menu------------")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit")
    print("----------------------------\n")

#function for getting age from user with validations so that age accepts only Positive Integer
def getage():
    customerage=input("Enter Customer's Age: ")
    if not customerage == "":
      if not customerage.isdecimal():
          if not customerage==" ":
              print("Age must be positive Integer only!! Without any sLeading or Trailing or inbetween whitespace!")
              customerage = getage()
    return customerage

#Functon or getting name from user with validations so that name must accepts only characters without any whitespace
#And it can't be empty
def getname():
    customername = input("Enter Customer's Name: ")
    if (customername.isalpha()) == False:
        print("Invalid Input!!")
        print("Name Can't be blank and Should contain only alphabets without any whitespace")
        customername = getname()
    return customername

#Main_Logic
while True:
    display_menu()
    try:
        choice = int(input("Select Which Operation You Want to Perform : "))
        if choice == 1:
            stringg = "1|"
            print("::To Find Customer Enter Details::")
            fname = str(getname())
            msg = stringg + fname
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 2:
            stringg = "2|"
            print("-::Enter Details Of New Customer::-")
            cname = getname()
            cage = str(getage())
            caddress = input("Enter Customer's Address: ")
            cphone = input("Enter Customer's Phone: ")
            msg = stringg + cname + "|" + cage + "|" + caddress + "|" + cphone
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 3:
            stringg = "3|"
            print("::To Delete Customer Enter Details::")
            cname = str(getname())
            msg = stringg + cname
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 4:
            stringg = "4|"
            print("::To Update Customer's Age Enter Details::")
            cname = getname()
            cage = str(getage())
            msg = stringg + cname + "|" + cage
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 5:
            stringg = "5|"
            print("::To Update Customer's Address Enter Details::")
            cname = getname()
            caddress = input("Enter New Address: ")
            msg = stringg + cname + "|" + caddress
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 6:
            stringg = "6|"
            print("::To Update Customer's Phone Enter Details::")
            cname = getname()
            cphone = input("Enter New Phone: ")
            msg = stringg + cname + "|" + cphone
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 7:
            msg="7|printreport"
            clientsocket.send(msg.encode())
            smsg = pickle.loads(clientsocket.recv(4096))
            i = 1
            print("________________________________________________CUSTOMER_REPORT___________________________________________________")
            for k in smsg:
                print("__________________________________________________________________________________________________________________")
                print("  [ Record-", i, " : ", "|| Name: ", k[0], " || Age: ", k[1][0], " || Address: ", k[1][1],
                      " || Phone: ", k[1][2], "]")
                i = i + 1
            print("__________________________________________________________________________________________________________________")

        elif choice == 8:
            msg = "8|Exit"
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)
        else:
            print("\nInvalid Choice!!! Please Enter valid Choice from 1 - 8")

        if not smsg:
            # if data is not received break
            break
        if smsg == "Good Bye!!":
            break
    except ValueError:
        print("\nInvalid Choice!!! Please Enter valid Choice from 1 - 8")

clientsocket.close()