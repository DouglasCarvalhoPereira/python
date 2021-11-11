file = open('clientes.txt','r')
linhas = file.readlines()
del linhas[:4]

qt_anuncios = 0
qt_org = 0
qtd_yt_org = 0
qtd_igfb = 0
qtd_site_org = 0

for linha in linhas:
    linha.split(',')
    email, origem = linha
#   if "_org" in origem:
#       qt_org+=1
#   else:
#       qt_anuncios+=1
file.close()

print("Anuncio: {}".format(qt_anuncios))  
print("Organico: {}".format(qt_org))