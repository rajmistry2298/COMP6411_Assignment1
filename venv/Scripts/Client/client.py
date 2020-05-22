import socket

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
            print("\nyou want to find customer")

        elif choice == 2:
            print("\nyou want to add new customer")

        elif choice == 3:
            print("\nyou want to delete customer")

        elif choice == 4:
            print("\nyou want to update customer age")

        elif choice == 5:
            print("\nyou want to update customer address")

        elif choice == 6:
            print("\nyou want to update customer phone")

        elif choice == 7:
            msg="7|print report"
            clientsocket.send(msg.encode())
            smsg = clientsocket.recv(4096).decode()
            print(smsg)

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
