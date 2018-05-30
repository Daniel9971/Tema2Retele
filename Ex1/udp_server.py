# UDP Server
import socket
import logging

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = 'rt3'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portnul portul %d", adresa, port)
prevData="0"
data="0"
sock.settimeout(60)
while True:
    logging.info('Asteptam mesaje...')
    data, address = sock.recvfrom(1024)
    mesaj = "ack"+data
    while data==prevData:
        try:
            data, address = sock.recvfrom(1024)
            sent = sock.sendto(mesaj, address)
        except socket.timeout:
            data,address = sock.recvfrom(1024)
    logging.info('Content primit: "%s"', data)
    prevData=data





