# Import socket module
from socket import * 
import sys # In order to terminate the program
from threading import Thread
from time import sleep

gotMessage = False
shutdown = False

#https://www.geeksforgeeks.org/python-communicating-between-threads-set-1/
#https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python



#we cant use message passing cause main threads changes to a var is not reflecting in timers copy of the var
#TODO try using message passing by making the server recvfrom start on a new thread and the timer start on a thread

#start both threads at same time(and execute concurrently)
#timer thread will be reader
#recv from thread will be producer

#recv from writes to q DONE(or can even write paramaters) once it has got a messafe
#if readfrom finished its sleep for x seconds and there is nothing in q then read from thread should notify main thread to exit system



def timer():
	sleep(15)
	print(f'Timers gotMessage:{gotMessage}')
	if not gotMessage:
		print("15 seconds has passed, shutting down") #dont shutdown from other thread cause orphan process can be created
	

	

# Assign a port number
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

while True:
	#close socket if its been 3 seconds 

	
	print('The server is ready to receive')
	thread = Thread(target = timer)
	thread.start()
	#user starts client within 3 seconds then this main thread continues on, but other timer thread is still going
	#if user doesnt start client within 3 seconds then this main thread still goes but other is done
	#so basically every time we start client new timer thread goes on

	#we shutdown if when timer thread comes back, the main thread is still on recvfrom
	sentence, clientAddress = serverSocket.recvfrom(1024)
	gotMessage = True
	print(f'Main threads gotMessage:{gotMessage}')
	#if (shutdown):
	#	serverSocket.close()
	#	sys.exit()
	capitalizedSentence = sentence.decode().upper()
	serverSocket.sendto(capitalizedSentence.encode(), clientAddress)
	gotMessage = False


serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data


