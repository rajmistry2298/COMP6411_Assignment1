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

while True:
    display_menu()
    try:
        choice = int(input("Select Which Operation You Want to Perform : "))
        if choice == 1:
            str = "1|"
            fname=input("Enter Customer Name To Find Record: ")
            msg = str + fname
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 2:
            str = "2|"
            print("-::Enter Details Of New Customer::-")
            cname = input("Enter Customer's Name: ")
            cage = input("Enter Customer's Age: ")
            caddress = input("Enter Customer's Address: ")
            cphone = input("Enter Customer's Phone: ")
            msg = str + cname + "|" + cage + "|" + caddress + "|" + cphone
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 3:
            str = "3|"
            cname = input("Enter Customer's Name: ")
            msg = str + cname
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 4:
            str = "4|"
            cname = input("Enter Customer's Name Whose Age You Want to Update: ")
            cage = input("Enter New Age: ")
            msg = str + cname + "|" + cage
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 5:
            str = "5|"
            cname = input("Enter Customer's Name Whose Address You Want to Update: ")
            caddress = input("Enter New Address: ")
            msg = str + cname + "|" + caddress
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 6:
            str = "6|"
            cname = input("Enter Customer's Name Whose Phone You Want to Update: ")
            cphone = input("Enter New Phone: ")
            msg = str + cname + "|" + cphone
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

        elif choice == 7:
            msg="7|print report"
            clientsocket.send(msg.encode())
            smsg = pickle.loads(clientsocket.recv(4096))
            i = 1
            print("________________________________________________CUSTOMER_REPORT___________________________________________________")
            for key, values in smsg.items():
                print("__________________________________________________________________________________________________________________")
                print("  [ Record-", i, " : ", "|| Name: ", key, " || Age: ", values[0], " || Address: ", values[1],
                      " || Phone: ", values[2], "]")
                i = i + 1
            print("__________________________________________________________________________________________________________________")
        elif choice == 8:
            msg = "8|Exit"
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)
        else:
            print("\nInvalid Choice!!! Please Enter valid Choice from 1 - 8")

        '''msg = input("Enter your message: ")
        clientsocket.send(msg.encode())
        smsg = clientsocket.recv(4096).decode()
        '''
        if not smsg:
            # if data is not received break
            break
        if smsg == "Good Bye!!":
            break
    except ValueError:
        print("\nInvalid Choice!!! Please Enter valid Choice from 1 - 8")

clientsocket.close()
