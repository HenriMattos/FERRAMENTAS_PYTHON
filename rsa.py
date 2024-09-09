from Crypto.PublicKey import RSA

chave = RSA.generate(2048)
chave_privada = chave.export_key()
chave_publica = chave.publickey().export_key()

with open('private.pem', 'wb') as f:
    f.write(chave_privada)
with open('public.pem', 'wb') as f:
    f.write(chave_publica)
