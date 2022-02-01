import struct


bytes = b'\x00\x00\x00\r'

# python strucn unpack() method
Numeric_values = struct.unpack('!I', bytes)
# printing
print(Numeric_values)






#TODO check that we can receive the info using the correct query string for this phase DONE
#TODO check that header is received, data is received DONE
#TODO check data length, pcode, entity, data, and packet lenght are what they should be for this phase DONE
#TODO check paacket lenghth divisible by 4 DONE


