import time
import os
import sys
from Valida_Input import valida_input_sim_nao


def localizar_aba(aplicacao,driver,nome_aba) :
    

    while True:
        abas = driver.window_handles
        aba_encontrada = False
        # percorro as abas do Chrome para encontrar a correta
        for aba in abas:
            driver.switch_to.window(aba)
            time.sleep(0.5)  

            # verifico se a aba do S-Works (Novo Processo) foi encontrada
            if nome_aba in driver.title:
                print("Aba correta encontrada!")
                aba_encontrada = True
                break
                
        
        # Checo se encontrei a aba correta    
        if aba_encontrada == False :
            print('Aba não encontrada.')
            tentativa_aba = valida_input_sim_nao(aplicacao,'Verifique se abriu uma aba da tela de Novo Processos do S-Works.','Deseja tentar novamente? ')
            if tentativa_aba.upper() == 'N' :
                return sys.exit()
            else:
                os.system('cls')
                print(aplicacao)
                print('')
                print('Buscando aba...')
                continue
        else :
            break
