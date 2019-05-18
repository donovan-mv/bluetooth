import bluetooth

port = 3
size = 1024
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server.bind(("", port)) #it will use whichever interface is available
print "Waiting for client..."
server.listen(1)
client, addr = server.accept()
print "Client connected"
while 1:
    data = client.recv(size)
    if data:
        print "Data:", data
        client.send("OK")
    else:
        break
server.close()
client.close()
