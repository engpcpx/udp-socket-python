# udp-socket-python
Sender / Receiver functions using UDP socket


Sender / Receiver functions using UDP socket
by Paulo Paixao

This project consists of two files sender.py and receiver.py.
The function of the Sender is to carry out a message transmission using
an udp socket for a receiver that is listening to the network.

RECEIVER:
Run the receiver.py file on the server computer, following the instructions
requests made available through a basic input menu that
requests only a port number according to a specified range
between 10001 to 11000.

SENDER:
Run the sender.py file on the client computer.
Fill in the data according to the guidelines shown in a menu.
Use the same udp port defined in the receiver program.
The program was parameterized to transmit a maximum of five
sequential messages. However, this can be easily changed in the
source code.
After transmission, Sender waits for a confirmation
message received by the Receiver, informing the status of Ok or nOk.
