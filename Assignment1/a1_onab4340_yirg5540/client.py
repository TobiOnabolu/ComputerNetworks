#Alvin Onabolu
#Nahor Yirgaalem

# Import socket module

from socket import * 
import struct
import sys
CLIENT = 1



#packet should contain pcode, entity, data length, data
pcode = 0
entity = CLIENT 
data = 'Hello World!!!'
#returns size of string in bytes
data_length = len(data.encode())


#pack data, into packet
header = struct.pack('IHH', data_length, pcode, entity)
packet = header + data.encode('utf-8')


#TODO collect server name, server port to send to
server_name = ''
server_port = ''



#TODO Send packet to server
