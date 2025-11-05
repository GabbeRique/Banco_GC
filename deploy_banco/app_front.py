from flask import Flask, render_template, request
import main  # importa seu código original

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Criar conta
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        saldo = float(request.form['saldo'])
        senha = request.form['senha']

        # gera novo ID único
        id_novo = main.prox_id
        main.prox_id += 1

        # salva no dicionário
        main.conta[id_novo] = [nome, cpf, saldo, senha]

        return render_template('cadastrar.html', sucesso=True, nome=nome, id=id_novo)

    return render_template('cadastrar.html', sucesso=False)

# PIX etapa 1
@app.route('/pix-etapa1', methods=['POST'])
def pix_etapa1():
    origem = int(request.form['origem'])
    destino = int(request.form['destino'])
    valor = float(request.form['valor'])

    if origem not in main.conta or destino not in main.conta:
        return render_template('pix.html', erro="Conta inexistente.")

    if valor <= 0:
        return render_template('pix.html', erro="Valor inválido.")

    saldo_atual = main.conta[origem][2]
    if valor > saldo_atual:
        return render_template('pix.html', erro="Saldo insuficiente.")

    destino_nome = main.conta[destino][0]
    destino_cpf = main.conta[destino][1]

    return render_template(
        'pix.html',
        confirmar=True,
        origem=origem,
        destino=destino,
        valor=valor,
        destino_nome=destino_nome,
        destino_cpf=destino_cpf,
        saldo_atual=saldo_atual
    )

# PIX etapa 2
@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.method == 'POST':
        origem = int(request.form['origem'])
        destino = int(request.form['destino'])
        valor = float(request.form['valor'])
        senha = request.form['senha']

        if origem not in main.conta or destino not in main.conta:
            return render_template('pix.html', erro="Conta inexistente.")

        if senha != main.conta[origem][3]:
            return render_template('pix.html', erro="Senha incorreta.")

        if valor <= 0:
            return render_template('pix.html', erro="Valor inválido.")
        if valor > main.conta[origem][2]:
            return render_template('pix.html', erro="Saldo insuficiente.")

        main.conta[origem][2] -= valor
        main.conta[destino][2] += valor

        return render_template('pix.html', sucesso=True, valor=valor)

    return render_template('pix.html')

# Mostrar dados
@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar():
    if request.method == 'POST':
        id_c = int(request.form['id'])
        cpf = request.form['cpf']
        senha = request.form['senha']

        if id_c not in main.conta:
            return render_template('mostrar.html', erro="Conta não encontrada.")

        conta = main.conta[id_c]
        if cpf == conta[1] and senha == conta[3]:
            return render_template('mostrar.html', conta=conta, id=id_c)
        else:
            return render_template('mostrar.html', erro="CPF ou senha incorretos.")
    return render_template('mostrar.html')

# 🔒 Deletar conta (senha mestra)
@app.route('/deletar', methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        senha_admin = request.form['senha_admin']
        id_c = int(request.form['id'])

        if senha_admin != "Costa15607":
            return render_template('deletar.html', erro="Senha mestra incorreta.")

        if id_c not in main.conta:
            return render_template('deletar.html', erro="ID de conta inválido.")

        deletada = main.conta.pop(id_c)
        return render_template('deletar.html', sucesso=True, nome=deletada[0])

    return render_template('deletar.html')


if __name__ == '__main__':
    app.run(debug=True)
