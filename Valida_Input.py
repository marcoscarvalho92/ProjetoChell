import os

def valida_input_sim_nao(nome_aplicacao,mensagem_inicial,cta_tentativa) :
    os.system('cls')
    print(nome_aplicacao)
    print('')
    print(mensagem_inicial)
    print('')
    resposta_input_sim_nao = input(f'{cta_tentativa} [S]im [N]ão :')
    
    # valido o que foi digitado, só aceitando uma opção específica
    while not(len(resposta_input_sim_nao) == 1 and (resposta_input_sim_nao.upper() == "S" or resposta_input_sim_nao.upper() == "N")) :
        os.system('cls')
        print(nome_aplicacao)
        print('')
        print('Escolha uma opção válida.')
        resposta_input_sim_nao = input(f'{cta_tentativa} [S]im [N]ão :')

    return resposta_input_sim_nao
    