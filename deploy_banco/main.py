import os
from datetime import date , datetime




data=date.today()
hora=datetime.now()



conta = {
    0: ['Banco_MG', '836.514.810-65', 15843529.5, 'adm2024']
}

# Próximo ID disponível
prox_id = 1







def clear():
    print("\033[H\033[J", end='')




def pix():


    clear()


    conta1 = int(input("Qual Seu id? "))
    clear()
    conta2 = int(input("Qual o id da conta que vai receber? "))
    clear()
    print(f'Nome da Conta que o dinheiro será transferido: {conta[conta2][0]}\nCPF da Conta que o dinheiro será transferido: {conta[conta2][1]}')
    input()
    clear()
    res = int(input('<--- Etapa De Confirmação--->\n\n 1 - Confimar Ação\n 2 - Cancelar Ação\n\n <--- Etapa De Confirmação--->\n\n' ))
    clear()
    if res == 2:
        print('Ação cancelada')
    elif res == 1:
        se = input('Digite sua Senha: ')
        clear()


        while True:
            print(f'Saldo Atual: {conta[conta1][2]}')
            valor = float(input("Valor: "))
            clear()
            res = int(input('<--- Etapa De Confirmação--->\n\n 1 - Confimar Ação\n 2 - Alterar Valor\n\n <--- Etapa De Confirmação--->\n\n' ))
            clear()
            if res == 2:
                clear()
                print("Etapa de Alteração:")
                clear()
            elif res == 1:
                if valor > conta[conta1][2]:


                    print('Erro, valor maior que seu saldo')
                    input()
                elif valor < 0:
                    print('Erro, não pode enviar valores menores de zero')
                    input()
                else:
                    print(f'Saldo Atual: {conta[conta1][2]}')
                    conta[conta1][2] = conta[conta1][2] - valor
                    print(f'Novo Saldo: {conta[conta1][2]}')
                    input()
                    conta[conta2][2] = conta[conta2][2] + valor
                    clear()
                break
            else:
                print('Tente Novamente')
               


       
    else:
        print('Algo errado, Tente Novamente')
       
   




def cadastrar(conta):




    clear()
    res = input('<--- Etapa De Confirmação--->\n\n 1 - Confimar Ação\n 2 - Negar Ação\n\n <--- Etapa De Confirmação--->\n\n' )
    clear()
    if res == '2':
        print('Ação Negada')
    elif res == '1':
        if conta == '':
            conta.clear()
        else:
            c_conta = []
            dados = input('Nome Completo: ')
            c_conta.append(dados)
            dados = input('CPF: ')
            c_conta.append(dados)
            dados = float(input('Saldo: '))
            c_conta.append(dados)
            dados = input('Senha: ')
            c_conta.append(dados)
            clear()
            conta.append(c_conta)
            print(f'Seja Bem Vindo(a)\nSr(a). {c_conta[0]}\n\nSeu Id é: {len(conta) - 1}')
            input()
            clear()
    else:
        print('Não é possivel registrar')
        input()
        clear()








        input('Pressione Enter\n\n ')
    return(conta)


clear()
var = input('Entrar\n')
clear()
while True:
    inicil = input('<--- Mine banco --->\nProcedimentos: \n\n 1 - Criar Conta\n 2 - PIX\n 3 - Mostrar Dados\n 4 - Terminar\n\n <--- Etapa De Confirmação--->\n\n')
    if inicil == '1':
        cadastrar(conta)
    elif inicil == '2':
        pix()
    elif inicil == '3':
        clear()
        id_p = int(input('Qual o Id da sua conta? '))


        senhas = input('Qual sua senha? ')
        cpf = input('Qual o CFP da conta? ')


        if senhas == conta[id_p][3] and cpf == conta[id_p][1]:
           
            clear()
            print(f'Conta:\n\nNome: {conta[id_p][0]}\nCPF: {conta[id_p][1]}\nSaldo: {conta[id_p][2]}\nSenha: {conta[id_p][3]}')


        elif senhas != conta[id_p][3] or cpf != conta[id_p][1]:
            clear()
            print('Erro, Tente Novamente')
        else:
            clear()
            print('Erro, Tente Novamente')      
       
        input()
        clear()




    elif inicil == '4':
        clear()
        print('Ate mais')
        input()
        break
    else:
        clear()
        print('Código Não encontardo')
        input()
