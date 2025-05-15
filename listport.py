import socket,sys

srtHost = input('Informe o host ou URL do site')


try:
    lstInfohost = socket.getaddrinfo(host=srtHost ,port=443)
except:
    print(f'Erro: {sys.exc_info()}')
for info in lstInfohost:
 print(info)
