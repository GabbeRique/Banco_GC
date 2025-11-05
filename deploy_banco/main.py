# main.py
import os
from datetime import date, datetime

# Data e hora atuais
data = date.today()
hora = datetime.now()

# Dicionário de contas (mantido)
conta = {
    0: ['Banco_MG', '836.514.810-65', 15843529.5, 'adm2024']
}

# Próximo ID
prox_id = 1


# Funções “de fachada” — ainda existem, mas não usam input()
def pix(remetente_id, destinatario_id, valor):
    """
    Faz uma transferência entre contas.
    Agora recebe parâmetros em vez de usar input().
    """
    global conta

    # Verifica se as contas existem
    if remetente_id not in conta or destinatario_id not in conta:
        return "Conta não encontrada"

    # Verifica saldo
    if valor <= 0:
        return "Valor inválido"
    if valor > conta[remetente_id][2]:
        return "Saldo insuficiente"

    # Realiza transferência
    conta[remetente_id][2] -= valor
    conta[destinatario_id][2] += valor

    return f"Pix de R${valor:.2f} enviado de {conta[remetente_id][0]} para {conta[destinatario_id][0]}"


def cadastrar(nome, cpf, saldo, senha):
    """
    Cadastra uma nova conta.
    """
    global conta, prox_id
    conta[prox_id] = [nome, cpf, saldo, senha]
    prox_id += 1
    return prox_id - 1  # retorna o ID criado


def mostrar_dados(id_conta, senha, cpf):
    """
    Retorna os dados da conta se a senha e CPF estiverem corretos.
    """
    if id_conta not in conta:
        return "Conta não encontrada"

    if conta[id_conta][3] == senha and conta[id_conta][1] == cpf:
        return {
            "nome": conta[id_conta][0],
            "cpf": conta[id_conta][1],
            "saldo": conta[id_conta][2],
            "senha": conta[id_conta][3],
        }
    else:
        return "Erro: senha ou CPF incorretos"
