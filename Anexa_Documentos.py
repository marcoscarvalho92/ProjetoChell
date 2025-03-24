import time
from selenium.webdriver.common.by import By
import os
from Valida_Input import valida_input_sim_nao


def anexar_arquivos(aplicacao,driver) :
    os.system('cls')
    print(aplicacao)
    print('')
    # informo o caminho onde está a pasta
    caminho = input('Informe a pasta onde estão os arquivos: ')
    # percorro o caminho informado e crio a string de localização de cada arquivo
    for arquivo in os.listdir(caminho) :
        arquivo_a_enviar = caminho+r'\\'+arquivo
        

        # localizo  o campo de upload e envia o arquivo
        caixa_anexar = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        caixa_anexar.send_keys(arquivo_a_enviar)

        # clico no botão para anexar
        botao_enviar = driver.find_element(By.ID, "uploadFileBtn")
        botao_enviar.click()
        time.sleep(1)
    
    print('Documentos anexados!')


