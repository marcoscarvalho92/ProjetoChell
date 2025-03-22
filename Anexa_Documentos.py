import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import sys
from Valida_Input import valida_input_sim_nao


def localizar_aba(aplicacao,driver) :
    

    while True:
        abas = driver.window_handles
        aba_encontrada = False
        # percorro as abas do Chrome para encontrar a correta
        for aba in abas:
            driver.switch_to.window(aba)
            time.sleep(0.5)  

            # verifico se a aba do S-Works (Novo Processo) foi encontrada
            if "S-Works | Novo Processo" in driver.title:
                print("Aba correta encontrada!")
                aba_encontrada = True
                break
                
        
        # Checo se encontrei a aba correta    
        if aba_encontrada == False :
            print('Aba não encontrada.')
            tentativa_aba = valida_input_sim_nao(aplicacao,'Verifique se abriu uma aba da tela de Novo Processos do S-Works.','Deseja tentar novamente? ')
            if tentativa_aba.upper() == 'N' :
                sys.exit()
            else:
                os.system('cls')
                print(nome_aplicacao)
                print('Buscando aba...')
                break
        else :
            break
        



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


