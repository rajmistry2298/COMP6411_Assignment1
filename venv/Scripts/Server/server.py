import socket,pickle

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
    name = x[0].strip()
    tp = x[3]
    phone = tp[0:len(tp) - 1]
    datalist = [x[1].strip(),x[2].strip(),phone.strip()]
    if name!= "":
        dictionary[name] = (datalist)

testFile.close()
print("\nData Loaded Successfully From The File(data.txt)!")

#Main_Logic
while True:
    #wait for Client to connect
    clientsocket, address = serversocket.accept()
    print(f"\nConnection from Client{address} has been established.")
    msg = "Welcome to the server!"
    clientsocket.send(msg.encode())

    while True:
        data = clientsocket.recv(4096).decode()
        splitdata = data.split("|")
        if splitdata[0]=="1":
            senddata="Customer Not Found!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="[ Record_You_Want: || Name: "+key+" || Age: "+values[0]+" || Address: "+values[1]+" || Phone: "+values[2]+"]"
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="2":
            senddata="New Customer Successfully Added!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="Customer Already Exist!!"
            if senddata == "New Customer Successfully Added!!":
                datalist1 = [splitdata[2].strip(), splitdata[3], splitdata[4]]
                dictionary[splitdata[1]] = (datalist1)
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="3":
            senddata="Customer Does Not Exist!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="Customer Successfully Deleted!!"
            if senddata == "Customer Successfully Deleted!!":
                del dictionary[splitdata[1]]
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="4":
            senddata="Customer Not Found!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="Customer's Age Successfully Updated!!"
            if senddata == "Customer's Age Successfully Updated!!":
                dictionary[splitdata[1]][0] = splitdata[2]
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="5":
            senddata="Customer Not Found!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="Customer's Address Successfully Updated!!"
            if senddata == "Customer's Address Successfully Updated!!":
                dictionary[splitdata[1]][1] = splitdata[2]
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="6":
            senddata="Customer Not Found!!"
            for key, values in dictionary.items():
                if key == splitdata[1]:
                    senddata="Customer's Phone Successfully Updated!!"
            if senddata == "Customer's Phone Successfully Updated!!":
                dictionary[splitdata[1]][2] = splitdata[2]
            clientsocket.send(senddata.encode())

        elif splitdata[0]=="7":
            sorteddictionary = sorted(dictionary.items())
            senddata = pickle.dumps(sorteddictionary)
            clientsocket.send(senddata)

        elif splitdata[0]=="8":
            clientsocket.send("Good Bye!!".encode())
            break

    # clientsocket.close()  # close the connection