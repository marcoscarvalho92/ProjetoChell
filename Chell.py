import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
from Anexa_Documentos import localizar_aba,anexar_arquivos
from Valida_Input import valida_input_sim_nao

nome_aplicacao = '----- Chell 1.0.0 -----'
print(nome_aplicacao)
print('')
print('Antes de iniciarmos, algumas informações importantes:',end='\n\n')
print('* O programa irá abrir uma nova janela do Chrome, e toda a operação deverá ser feita por ela.',end='\n')
print('* Organize os arquivos em uma pasta, sem subpastas. Não execute o programa com os arquivos soltos em pastas como o "Desktop" ou "Downloads".')
print('* Acesse a página de "Novo Processo" do S-Works, na versão que precisar e, quando estiver pronto, volte aqui e dê um "OK" para seguirmos.',end='\n\n')
print('* Caso tenha expectativa de realizar várias anexações automáticas, só deixar o programa aberto e a janela do Chrome aberta. Depois é só solicitar para executar a operação novamente.')
input('Deseja Iniciar? Pressione ENTER para iniciarmos: ')


# Caminho do chorme, para acionar a execução
caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Porta de depuração remota
porta_depuracao = "9222"

# Abre o Chrome em modo de depuração (se ainda não estiver aberto)
subprocess.Popen(
    [caminho_chrome, f"--remote-debugging-port={porta_depuracao}", "--user-data-dir=C:\\selenium_chrome_profile"],
    shell=True,
)

# Aguarde alguns segundos para garantir que o Chrome foi iniciado
input('Pressione ENTER para seguir coma anexação automática: ')

# Configurar o Selenium para conectar ao Chrome já aberto
chrome_options = Options()
chrome_options.debugger_address = "localhost:9222"

# Criar driver sem abrir uma nova janela
driver = webdriver.Chrome(service=Service(), options=chrome_options)

# estrutura de loop para permitir múltiplas execuções
while True :
    localizar_aba(nome_aplicacao,driver)
    anexar_arquivos(nome_aplicacao,driver)
    controlador_execucoes = valida_input_sim_nao(nome_aplicacao,'Posso realizar a operação novamente, em outro processo que está sendo iniciado.','Deseja realizar a operação novamente? ')
    if controlador_execucoes.upper() == 'S' :
        continue
    else :
        sys.exit()



































# # Configurar o Selenium para conectar ao Chrome já aberto
# chrome_options = Options()
# chrome_options.debugger_address = f"localhost:{porta_depuracao}"

# # Criar driver sem abrir uma nova janela
# driver = webdriver.Chrome(service=Service(), options=chrome_options)

# abas = driver.window_handles
# aba_encontrada = False

# # Itera sobre as guias para encontrar a correta
# for aba in abas:
#     driver.switch_to.window(aba)
#     time.sleep(1)  # pause de segurança para alternar entre as abas

#     # Verificar se a aba contém o título esperado
#     if "S-Works | Novo Processo" in driver.title:
#         print(f"Aba correta encontrada: {driver.current_url}")
#         aba_encontrada = True
#         break

# if aba_encontrada == False :
#     input('Aba não encontrada. Clique em qualquer botão para fechar o programa')
#     sys.exit()


# ##############################################
# #Navego entre os arquivos para anexar na página
# caminho = input('Informe a pasta onde estão os arquivos: ')
# # r'C:\\Users\\Marcos\\Desktop\\Backup Marcos\\Desktop\\Controles Marcos\\Diversos'
# for arquivo in os.listdir(caminho) :
#     arquivo_a_enviar = caminho+r'\\'+arquivo
#     print(caminho+r'\\'+arquivo)
#     # Localiza o campo de upload e envia o arquivo
#     caixa_anexar = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#     caixa_anexar.send_keys(arquivo_a_enviar)
#     botao_enviar = driver.find_element(By.ID, "uploadFileBtn")
#     botao_enviar.click()
#     time.sleep(1)






# #     # Caminho do arquivo a ser anexado
# #     caminho_arquivo = os.path.abspath("C:/caminho/para/o/arquivo.pdf")

# #     # Digita o caminho do arquivo e confirma
# #     pyautogui.write(caminho_arquivo)
# #     time.sleep(1)
# #     pyautogui.press("enter")

# #     print("Arquivo anexado com sucesso!")

# # else:
# #     print("Aba não encontrada!")