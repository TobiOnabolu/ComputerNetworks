#Alvin Onabolu
#Nahor Yirgaalem

# Import socket module

from socket import * 
import struct
import sys


CLIENT = 1
SERVER = 2

def phaseA(clientSocket, server_name, server_port):
    #packet should contain pcode, entity, data length, data
    pcode = 0
    entity = CLIENT 
    data = 'Hello World!!!00'
    #returns size of string in bytes
    data_length = len(data.encode())


    #pack data, into packet
    header = struct.pack('!IHH', data_length, pcode, entity)
    packet = header + data.encode('utf-8')
  

    #Send the packet(bytes) to server address
    clientSocket.sendto(packet, (server_name, server_port))


    #receiving response back from server
    try:
        response, serverAddress = clientSocket.recvfrom(2048)
    except:
        print("Client did not receive any packet back for phase A...")
        clientSocket.close()
        sys.exit()
    data_length, pcode, entity, repeat, udp_port, length, codeA = struct.unpack('!IHHIIHH', response)
  
    return repeat, udp_port, length, codeA


def phaseB(clientSocket, server_name, server_port, repeat, length, pcode):
    #Assign variables
    entity = CLIENT
 
    
    #make lenght divisible by 4
    while length % 4 != 0:
        length += 1

    data = bytearray(length) 

    # 4 is the length of packet id
    data_length = len(data) + 4

    
    #send repeat number of packets
    for packet_id in range(repeat):
        packet = struct.pack(f'!IHHI{length}s', data_length, pcode, entity, packet_id, data)
        print(f'Sending packet with packet ID: {packet_id}')
     
        clientSocket.sendto(packet, (server_name, server_port))
        
        #try to receive ack packet if no receive keep on resending packet
        failed = True
        while (failed):
            try:
                response, serverAddress = clientSocket.recvfrom(2048)
            except:
                #This except block will hit if timeout eeror on socket
                print("Did not receive ack packet from server...")
                print(f'Resending packet with packet id: {packet_id}')
                packet = struct.pack(f'!IHHI{length}s', data_length, pcode, entity, packet_id, data)
                clientSocket.sendto(packet, (server_name, server_port))
            else:
                failed = False


        #SOMETIME THIS GIVES INCORRECT BUFFER ERROR, PLEASE HELP
        s_data_length, pcode, s_entity, s_packet_id = struct.unpack('!IHHI', response)
        print(f'Recieved ack packet for packet ID: {s_packet_id}!')

    #Once received all ack packets from server wait to receive final packet
    try:
        response, serverAddress = clientSocket.recvfrom(2048)
    except:
        print("Did not receive final packet from server")
        clientSocket.close()
        sys.exit()
    


    data_length, pcode, entity, tcp_port, codeB = struct.unpack('!IHHII', response)

    return tcp_port, codeB
        
        




def phaseC():
    pass

def phaseD():
    pass



#Create Socket
#server_name = '34.69.60.253' #use ip address of computer u want to connect to
server_name = 'localhost' #use ip address of computer u want to connect to

server_port = 12000
# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_DGRAM)
#incase server runs into error and doesnt send nothing 
clientSocket.settimeout(5)


repeat, udp_port, length, codeA = phaseA(clientSocket, server_name, server_port)



#Create new socket with new port 
server_port = udp_port

tcp_port, codeB = phaseB(clientSocket, server_name, server_port, repeat, length, codeA)



