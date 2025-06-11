def extrairDados(url: str) -> tuple:
    #Remove o protocolo (http:// ou https://)
    partes = url.replace('http://', '').replace('https://', '').split('/', 1)
    host = partes[0]
    caminho = '/' + partes[1] if len(partes) > 1 else '/'
    nomeimagem =  caminho.split('/')[-1]
   
    return host, caminho, nomeimagem

print('Digite a URL utilizando HTTPS')
url = input('Digite a URL do site: ')

host, caminho, nomeimagem = extrairDados(url)

print(f'\nHost extraído........: {host}')
print(f'Nome da imagem:{nomeimagem} ')
print(f'Caminho do recurso...: {caminho}')
 



