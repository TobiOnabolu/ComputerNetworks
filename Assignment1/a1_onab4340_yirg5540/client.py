#Alvin Onabolu
#Nahor Yirgaalem

# Import socket module

from socket import * 
import struct
import sys


CLIENT = 1
SERVER = 2

def phaseA():
    #packet should contain pcode, entity, data length, data
    pcode = 0
    entity = CLIENT 
    data = 'Hello World!!!00'
    #returns size of string in bytes
    data_length = len(data.encode())


    #pack data, into packet
    header = struct.pack('!IHH', data_length, pcode, entity)
    packet = header + data.encode('utf-8')
  
    server_name = '34.69.60.253' #use ip address of computer u want to connect to
    server_port = 12000

    # Bind the socket to server address and server port
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    #Send the packet(bytes) to server address
    clientSocket.sendto(packet, (server_name, server_port))


    #receiving response back from server
    response, serverAddress = clientSocket.recvfrom(2048)
    data_length, pcode, entity, repeat, udp_port, lens, codeA = struct.unpack('!IHHIIHH', response)

    #confirming we get back message
    print(udp_port)


    clientSocket.close()  
    return repeat, udp_port, lens, codeA


def phaseB():
    pass

def phaseC():
    pass

def phaseD():
    pass


phaseA()


