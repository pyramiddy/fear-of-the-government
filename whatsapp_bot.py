import re
import pywhatkit
import time

def detectar_telefone_e_enviar(texto):
    # Regex para detectar números com 10 ou 11 dígitos seguidos
    padrao = r'\b\d{10,11}\b'
    telefones = re.findall(padrao, texto)

    for tel in telefones:
        # Formata número com código do Brasil
        numero_formatado = f"+55{tel}"

        mensagem = "Olá"  # Mensagem atualizada

        hora = time.localtime().tm_hour
        minuto = (time.localtime().tm_min + 1) % 60

        try:
            pywhatkit.sendwhatmsg(numero_formatado, mensagem, hora, minuto)
            print(f"Mensagem enviada para {numero_formatado}")
        except Exception as e:
            print(f"Erro ao enviar mensagem para {numero_formatado}: {e}")
