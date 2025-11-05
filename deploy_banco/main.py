from datetime import date, datetime

# Data e hora atuais
data = date.today()
hora = datetime.now()

# Banco de dados em memória
conta = {
    0: ['Banco_MG', '836.514.810-65', 15843529.5, 'adm2024']
}

# Próximo ID
prox_id = 1


def pix(remetente_id, destinatario_id, valor):
    """Transfere dinheiro entre contas."""
    global conta
    if remetente_id not in conta or destinatario_id not in conta:
        return "Conta não encontrada"
    if valor <= 0:
        return "Valor inválido"
    if valor > conta[remetente_id][2]:
        return "Saldo insuficiente"

    conta[remetente_id][2] -= valor
    conta[destinatario_id][2] += valor
    return f"Pix de R${valor:.2f} enviado de {conta[remetente_id][0]} para {conta[destinatario_id][0]}"


def cadastrar(nome, cpf, saldo, senha):
    """Cria nova conta e retorna o ID dela."""
    global conta, prox_id
    conta[prox_id] = [nome, cpf, saldo, senha]
    prox_id += 1
    return prox_id - 1


def mostrar_dados(id_conta, senha, cpf):
    """Mostra dados se senha e CPF estiverem corretos."""
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
