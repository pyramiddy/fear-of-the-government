import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def enviar_mensagem_whatsapp(nome_contato, mensagem):
    print("Abrindo o navegador...")
    options = webdriver.ChromeOptions()
    caminho_absoluto = os.path.abspath("./User_Data")
    options.add_argument(f"--user-data-dir={caminho_absoluto}")
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    print("Aguardando QR code ser escaneado...")
    wait = WebDriverWait(driver, 60*2)  # espera até 2 minutos
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    print("Login realizado com sucesso!")

    print(f"Procurando contato/grupo: {nome_contato}")
    search_box.click()
    search_box.clear()
    search_box.send_keys(nome_contato)

    time.sleep(2)  # deixa buscar resultados

    try:
        contato = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{nome_contato}"]')))
        contato.click()
        print(f"Contato {nome_contato} aberto!")
    except Exception as e:
        print(f"Contato {nome_contato} não encontrado: {e}")
        driver.quit()
        return

    print("Procurando caixa de mensagem...")
    try:
        caixa_mensagem = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        caixa_mensagem.click()
        caixa_mensagem.send_keys(mensagem)
        print("Mensagem digitada!")

        botao_enviar = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
        botao_enviar.click()
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

    print("Fechando navegador em 10 segundos...")
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    nome_contato = "KKKKKKKKKKK"  # Coloque aqui o nome exato do contato/grupo no WhatsApp
    mensagem = "Olá, essa é uma mensagem automática enviada pelo bot."  # Mensagem que será enviada

    enviar_mensagem_whatsapp(nome_contato, mensagem)
