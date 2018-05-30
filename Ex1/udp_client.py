# UDP client
import socket
import logging
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = '172.111.0.14'
server_address = (adresa, port)
sock.settimeout(0.0001)
try:
    for i in range(1,10001):
        mesaj = str(i)
        logging.info('Trimitem mesajul "%s" catre %s', mesaj, adresa)
        sock.sendto(mesaj, server_address)
        ACK = False
        raspunsServ="ack"+mesaj
        while not ACK:
            try:
                raspuns,address=sock.recvfrom(1024)
                if raspuns == raspunsServ:
                    ACK=True
            except socket.timeout:
                sock.sendto(mesaj,server_address)
finally:
    logging.info('closing socket')
    sock.close()
