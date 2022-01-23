import struct

data = 'Hello World!!!00'
header = struct.pack('!IHH', 16, 0, 1)
packet = header + data.encode('utf-8')


#print(packet)
print(len(packet))







#TODO check that we can receive the info using the correct query string for this phase DONE
#TODO check that header is received, data is received DONE
#TODO check data length, pcode, entity, data, and packet lenght are what they should be for this phase DONE
#TODO check paacket lenghth divisible by 4 DONE


