from cryptography.fernet import Fernet

# Gera uma chave e salva em senha.key
chave = Fernet.generate_key()
with open("senha.key", "wb") as chave_arquivo:
    chave_arquivo.write(chave)

# Criptografa a senha
senha_plana = "xodmtnitaiyklawn"  # sua senha de app aqui
fernet = Fernet(chave)
senha_criptografada = fernet.encrypt(senha_plana.encode())

# Salva a senha criptografada
with open("senha.secure", "wb") as arquivo:
    arquivo.write(senha_criptografada)

print("Senha criptografada e salva com sucesso.")
