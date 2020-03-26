"""
UDP RECEIVER
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
netIp = '0.0.0.0'        # ip address default  
currentState = 1           # state machine current
messages= []               # list of messages to sender
event = 0                  # status event control
address= [2]

#------------------------------------------------------------------------------  
# function to set UDP port [between 10001 and 11000]    
def setPort():
        
    # try datainput  
    try:
        # UDP port input
        udpPort = int(input('Entrada da porta UDP [10001 - 11000]: '))  
        
        # input test
        if(udpPort < 10001 or udpPort > 11000):
            print('entrada fora da faixa.')
            # return to main menu
            menu(1)
        
        # return
        return udpPort
    
    # error treatement       
    except:
        # show error message
        print('Entrada inválida.')
        # return to main menu
        menu(1)
    
#------------------------------------------------------------------------------        
# function to sender messages to server
def receiver(net, port):
    
    # import library
    import argparse, random, socket, sys
    
    
    try:
        # open udp socket 
        sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # identification sock return
        sck.bind((net, port))
        # show info
        print('Escutando no Soquete UDP: {}'.format(sck.getsockname()))
        print('Aguardando recepção de mensagens...')
        
        # loop; listening to network
        while(True):
        
            # loop: reading packages
            packages = []                    
            while(True):
                # receive package
                data, address = sck.recvfrom(sizeDatagram)
                # decodefying message
                pck = data.decode('ascii')
                packages.append(pck)
                
                # feedback
                answer = str(pck)
                sck.sendto(answer.encode('ascii'), address)
                                
                # stop loop condition
                if(pck == 0):
                    break    
                    
                # show receive packages
                print(packages)
           
    # open socket failure     
    except:
        # show error message
        print('Erro na abertura de Conexão do Receptor.')
        print('Provavelmente a porta UDP já está em uso.')
        # return to menu
        menu(1)
    
#------------------------------------------------------------------------------
#      
def rcvState1():
    
    # show current state
    print('[Executando Recepção...]')
       
    # set udp port
    udpPort = setPort()
    
    # active server
    receiver(netIp, udpPort)
    

#------------------------------------------------------------------------------ 
# 
def rcvState2():
    
    # show current state
    print('[Executando Estado 2...]')
   
     
#------------------------------------------------------------------------------
# main menu
def menu(option):
    
    # show main menu
    print('''
    -------------------------------------------------                 
	RECEIVER
    -------------------------------------------------
    [1] - Ativa Receptor de Mensagens
    [2] - Enter para Sair    
    -------------------------------------------------''')
    
    '''
    # show current address
    print('    IP atual: {}'.format(ipAddress))
    print('    Porta atual: {}'.format(udpPort))
    print('    Qtd. Mensagens: {}'.format(messages))
    print('    =================================================')
    '''
    
    # select menu option
   
    option= int(input('    Escolha a opção => '))
    print()
    
    # select menu option
    if option == 1:
        rcvState1()
        
    elif option == 2:
        pass
         
    elif option == 3:
        exit()
        
    else:
        print('Opção inválida.')
        menu(0)
    
        
#------------------------------------------------------------------------------
# loop
        
if __name__ == '__main__':	
    menu(1)
    
