import socket,sys

srtHost = input('Informe o host')

try:
    strIPhost = socket.gethostbyname(srtHost)
except socket.gaierror:
    print('Error')
except:
    print(f'Erro: {sys.exc_info()}')
else:
    print(srtHost)
