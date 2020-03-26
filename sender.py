"""
SENDER
Created on Sun Mar  1 02:15:46 2020

author: Paulo Cezar da Paixao

The present codes were based on the follows books:
    
    Programação de redes com Python: Guia abrangente de programação e 
    gerenciamento de redes com Python 3 (Portuguese Edition - Novatec - 2015)
    by Brandon Rhodes and John Goerzen
    
    Learning Python Network Programming
    Dr. M. O. Faruque Sarker Sam Washington
    Packet Publishing - 2015

    -*- coding: utf-8 -*-
    
"""
#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

#------------------------------------------------------------------------------  
#import sys
#import time
#import random
#import os
#import argparse
#from datetime import datetime
#from socket import *
#from time import sleep


#------------------------------------------------------------------------------  
# constants
sizeDatagram = 65535       # datagram maximun size in bytes (MTU)
delay = 2                  # time delay
udpPortLowLimit = 10001    # udp port low limit
udpPortHighLimit = 11000   # udp port high limit

#------------------------------------------------------------------------------  
# global variables
# ipAddress = ''             # ip address default (loopback)
# udpPort = 0                # udp port number default
currentState = 1           # state machine current
nMsg = 0                   # number of messages
messages= []               # list of messages to sender
event = 0                  # status event control
address= [2]

#------------------------------------------------------------------------------  
# function to realize
def setIP():
    
    # show header message
    print('=== Data for UDP connection ===')
    
    # ip addresss enter
    ipReceiver = input('Enter the Receiver''s IP address: ')
    print()
    
    return ipReceiver

#------------------------------------------------------------------------------  
# function to set UDP port [between 10001 and 11000]    
def setPort():
        
    # try datainput  
    try:
        # UDP port input
        udpPort = int(input('UDP port entry [10001 - 11000]: '))  
        
        # input test
        if(udpPort < 10001 or udpPort > 11000):
            print('entry out of range.')
            # return to main menu
            menu(1)
        
        # return
        return udpPort
    
    # error treatement       
    except:
        # show error message
        print('Invalid input.')
        # return to main menu
        menu(1)

#------------------------------------------------------------------------------  
# function to realize ethernet ping uisng OS (operatiomnal system API)        
def osPing(ip):
        
    # import library        
    import os
    
    # set event
    pingEventFlag = False   
   
    # use this method to ping system
    if not (os.system('ping -n 4 {}'.format(ip))):
        # update flag
        pingEventFlag = True
        # marker for debugging
        #print(pingEventFlag)
        # return 
        return pingEventFlag
         
    else:
        # print error message
        print('Receiver no response.')
        # update event state
        pingEventFlag = False
        # marker for debugging
        print(pingEventFlag)
        # return 
        return pingEventFlag
    
    
#------------------------------------------------------------------------------  
# function to realize ethernet ping without OS (operatiomnal system API)           
def localPing(ip, port):
    
    # import library
    import argparse, socket
    from datetime import datetime

    # Receber IP do server como argumento de linha de comando
    #argv = sys.argv
    
    # set delay time
    delay = 1
        
    # socket creation
    try:    
        sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sck.bind((ip, port))
        print('Listening on the Socket {}'.format(sck.getsockname()))
        
        # reset counter
        nPing = 0
        # ping 4 vezes
        while nPing <= 4:
            
            # increment counter
            nPing += 1
            
            # socket timeout delay
            sck.settimeout(delay) 
            
            try:   
                startTime = time.time()
                sck.sendto('ping'.encode(), (ip, port))
                endTime = time.time()
                message, address = sck.recvfrom(sizeDatagram)                        
               
                print('Receiver Response: ' + ip + ': ' + 
                      ' TTL: {:.2f}' .format ((endTime - startTime)*1000000)) 
            
            # timeout error                   
            except:
                print('Timeout')
                continue
            
    # open socket failure         
    except:
        print('Error opening Socket.')
        sck.close()
        menu(1)
    
    # close socket
    sck.close()
    
    # return to menu
    menu(1)
    
#------------------------------------------------------------------------------
# function to set quantity messages
def nMessage():
       
    # try enter message number to sender
    try:
        # enter message quantity
        nMsg = int(input('Number of messages [max. 5]: '))
        # verify entered quantity
        if(nMsg > 5):
            print('Error: Number of messages greater than 5')
            menu(2)
            
    # treatement error    
    except:
        # show error data aquisition
        print('Data entry error.')
        # return to menu option 2
        menu(2)
      
    # return function
    return nMsg

#------------------------------------------------------------------------------
# function to aquisition message package to sender
def pckMessage(nMsg):
       
    # set package message Event flag
    pckMsgEventFlag = False

    # arrays initialization 
    messages = []
        
    # inconditional loop 
    for i in range(nMsg):
        
        # initialize 
        seqNo = 1
        packages = []
        # loop for input message number
        while(seqNo != 0):
            # print message requisition
            print('Enter message [{}] to Send.'.format(i+1))
            data = input('=> ') 
            
            # loop for check size data
            while(len(data) > sizeDatagram):
                # print message requisition
                Print('Err: Very Long message.')                
                
                # print message requisition
                print('Digite a mensagem [{}] para envio.'.format(i+1))
                data = input('=> ') 
            
            # set message sequence flag
            if(i+1 >= nMsg):
                seqNo = 0           
            elif(i+1 < nMsg):
                seqNo = 1
                          
            # load packge list
            packages.append(data)
            packages.append(nMsg)
            packages.append(seqNo)
            break
        
        # assembly list of list        
        messages.append(packages)
    
    # show package list  
    print('Total [{}] packets for transmission'.format(nMsg))
    print(messages)
        
    # update package message Event flag
    pckMsgEventFlag = True
       
    # returne list of messages
    return messages

#------------------------------------------------------------------------------        
# function to sender messages to server
def sender(ip, port, nMsg):
    
    # import library
    import socket
    
    # mail array to send
    mails = []
    
    # package parameter in each message
    nParam = 3
    
    # load message list
    msgList = pckMessage(nMsg)
   
    #
    delay = 0.5
    
    try:
        # open udp socket 
        sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sck.connect((ip, port))
        print('Socket do Transmissor: {}'.format(sck.getsockname()))
    
        # scan list
        i = 0    
        for i in range(len(msgList)):       
        
            j =  0
            for j in range(nParam):  
                
                # 
                data = str(msgList[i][j])

                # data encode to send
                mail = data.encode('ascii')
                # send
                sck.send(mail)
                    
                # time to answer
                sck.settimeout(delay)
                
                # get answer
                answer = sck.recv(sizeDatagram)
                print('Enviado: {}'.format(mail))
                print('Recebido {}'.format(answer))
                
                # compare and return status
                if(mail == answer):
                    print('Ok')
                else:
                    print('nOk')
                    
                    
    # open socket failure     
    except:
        # show error message
        print('Error opening Receiver Connection.')
        print('Probably the UDP port [{}] is busy.'.format(port))
    
        # return to menu
        menu(1)     
    
#------------------------------------------------------------------------------
#      
def sndState1():
    
    # show current state
    # print('[Rinning State 1...]')
    
    # set ip address
    ipAddress = setIP()
   
    # ping 1
    if(osPing(ipAddress)): 
        # set udp port
        udpPort = setPort()   
        
        # message quantity
        msgQtd = nMessage()
   
        # active server
        sender(ipAddress, udpPort, msgQtd)
    
   
#------------------------------------------------------------------------------ 
# 
def sndState2():
    
    # show current state
    # print('[Running state 2...]')
    
    # end program
    exit()
   
#------------------------------------------------------------------------------
# main menu
def menu(option):
    
    # show main menu
    print('''
    -------------------------------------------------                 
	SENDER
    -------------------------------------------------
    [1] - Runs Message to Sender
    [0] - Exit    
    -------------------------------------------------''')
  
   
    # select menu option
    option= int(input('    Choose the option => '))
    print()
    
    # select menu option
    if option == 1:
        sndState1()
        
    elif option == 0:
        sndState2()
 
    else:
        print('Error: Invalid option.')
        menu(0)

#------------------------------------------------------------------------------
# loop
        
if __name__ == '__main__':	
    menu(1)


