import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("",1))
server_sock.listen(1)
print "Waiting for connections..."

uuid = "8952e4a9-fc51-48a6-8312-080ed3ee3b35"
bluetooth.advertise_service(server_sock, "My Service", uuid)

client, add = server_sock.accept()
print "Client connected"
data = client.recv(1024)

print "Data Received: ", data

server_sock.close()
client.close()
