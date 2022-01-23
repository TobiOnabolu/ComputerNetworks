#print(packet[-data_length:])

#Alvin Onabolu
#Nahor Yirgaalem

# Import socket module

from socket import * 
import struct
import sys
import time
import random


CLIENT = 1
SERVER = 2

def listen():
    # Assign a port number
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to server address and server port
    #no ip address cause we want to receive messages from any computer
    serverSocket.bind(("", serverPort))

    #Executing phases one at a time while keeping connection open
    while True:
        print('Starting Phase A...')
        serverPort = phaseA(serverSocket)
        #rebind socket to ensure were listening on new port
        serverSocket.bind(("", serverPort))
        print('Finished Phase A.')
        print('Starting Phase B...')
        #server is still listenting
        phaseB(serverSocket)
        print('Finished Phase B.')
        print('Starting Phase C...')
        #phaseC
        print('Finished Phase C.')
        print('Starting Phase D...')
        #phaseD
        print('Finished Phase D.')
        print('Closing Program')

        #close the socket and server once all phases are done 
        closeConnection(serverSocket)


def closeConnection(serverSocket):
    serverSocket.close()
    sys.exit()


def phaseA(serverSocket):
    #TODO Check if we been listening for 3 seconds
    #way to check if its been 3 seconds is 
    #thread .sleep for 3 seconds
    #then execute this code
    #if packet and client address received something then were good, if they didnt then close socket
    #do this check for each phase

    #Receiving packet from client
    packet, clientAddress = serverSocket.recvfrom(1024)

    #Checking socket termination conditions
    try:  
        #If we werent sent correct number of argument in packet, a struct error would be raised
        data_length, pcode, entity, word = struct.unpack('!IHH16s', packet)
        word = word.decode('utf-8')

        #Check that all value are correct, and packet is divisble by 4
        if (data_length != 16 or pcode != 0 or entity != 1 or word != "Hello World!!!00" or len(packet) != 24):
            #close Conection 
            print("incorrect value")
            closeConnection(serverSocket)
    except struct.error:
        #close connection
        print("Incorrect number of arguments")
        closeConnection(serverSocket)

    
    #collect Hello World message
    word = word[:-2].decode('utf-8')
    print(word)

    #TODO Verify message sent from client

    #create new packet to send back to client
    repeat = random.randint(5,20)
    udp_port = random.randint(20000, 30000)
    len = random.randint(50, 100)
    codeA = random.randint(100, 400)
    entity = SERVER

    #Pack message back to bytes
    data = struct.pack('IIHH', repeat, udp_port, len, codeA)
    data_length = len(data)

    #Put header details back to bytes ensure this has big endian
    header = struct.pack('!IHH', data_length, pcode, entity)
    
    #concat bytes back together
    packet = header + data
    
    #send packet back to client
    serverSocket.sendto(packet, clientAddress)

    #return the udpport to be listened to for next phase
    return udp_port


def phaseB():
    pass

def phaseC():
    pass

def phaseD():
    pass

def checkConditions():
    pass


phaseA()