import socket

#Socket Connection
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 5555))
serversocket.listen(5)
print("Server Started!!!!!")

#Load Data From File
testFile = open("data.txt","r")
dictionary={}
for line in testFile:
    x =line.split("|")
    name = x[0]
    tp = x[3]
    phone = tp[0:len(tp) - 1]
    datalist = [x[1].strip(),x[2],phone]
    dictionary[name] = (datalist)
testFile.close()
print("\nData Successfully Loaded From File!")

while True:
    #wait for Client to connect
    clientsocket, address = serversocket.accept()
    print(f"\nConnection from Client{address} has been established.")
    msg = "Welcome to the server!"
    clientsocket.send(msg.encode())

    while True:
        data = clientsocket.recv(4096).decode()
        splitdata = data.split("|")
        if splitdata[0]=="7":
            senddata = "report"
            clientsocket.send(senddata.encode())
        elif splitdata[0]=="8":
            # if data is not received break
            clientsocket.send("Good Bye!!".encode())
            break

        # data = input('Enter Reply:')
        # clientsocket.send(data.encode())  # send data to the client

    # clientsocket.close()  # close the connection