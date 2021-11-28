#!/usr/bin/env python
# coding: utf-8

# # Python para exe com códigos simples
# 
# ### Códigos que não interagem com outros arquivos ou ferramentas do computador
# 
# Usaremos abiblioteca pyinstaller
# 
# - Passo 1 - Instalar o pyinstaller
# - Passo 2 - Executar o pyinstaller
# 
# 
# pyinstaller -w nome_do_arquivo.py

# In[ ]:


from twilio.rest import Client

# SID daminha conta TWILIO em twilio.com/console
account_sid = 'ACdfdcabb817fabeca3216cc0e26dd8c92'

#Token de autenticação da minha conta Twilio
auth_token = 'a3d505b7d3af090c2130c5942687211b'

client = Client(account_sid, auth_token)

message = client.messages.create(to='+5524988219104', from_='+12565675179', body='Testando envio de SMS via twilio.')

print(message.sid)


# In[ ]:




