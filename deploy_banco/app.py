from flask import Flask, render_template, request
import main  # importa as funções e dados
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Criar conta
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            cpf = request.form['cpf']
            saldo = float(request.form['saldo'])
            senha = request.form['senha']

            id_novo = main.prox_id
            main.conta[id_novo] = [nome, cpf, saldo, senha]
            main.prox_id += 1

            return render_template('cadastrar.html', sucesso=True, nome=nome, id=id_novo)
        except Exception as e:
            return render_template('cadastrar.html', erro=f"Erro ao cadastrar: {e}")

    return render_template('cadastrar.html', sucesso=False)


# PIX etapa 1
@app.route('/pix-etapa1', methods=['POST'])
def pix_etapa1():
    try:
        origem = int(request.form['origem'])
        destino = int(request.form['destino'])
        valor = float(request.form['valor'])

        if origem not in main.conta or destino not in main.conta:
            return render_template('pix.html', erro="Conta inexistente.")
        if valor <= 0:
            return render_template('pix.html', erro="Valor inválido.")
        if valor > main.conta[origem][2]:
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
            saldo_atual=main.conta[origem][2]
        )
    except Exception as e:
        return render_template('pix.html', erro=f"Erro no PIX: {e}")


# PIX etapa 2
@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.method == 'POST':
        try:
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
        except Exception as e:
            return render_template('pix.html', erro=f"Erro no PIX: {e}")

    return render_template('pix.html')


# Mostrar dados
@app.route('/mostrar', methods=['GET', 'POST'])
def mostrar():
    if request.method == 'POST':
        try:
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
        except Exception as e:
            return render_template('mostrar.html', erro=f"Erro: {e}")

    return render_template('mostrar.html')


# Deletar conta (senha mestra)
@app.route('/deletar', methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        try:
            senha_admin = request.form['senha_admin']
            id_c = int(request.form['id'])

            if senha_admin != "Costa15607":
                return render_template('deletar.html', erro="Senha mestra incorreta.")
            if id_c not in main.conta:
                return render_template('deletar.html', erro="ID inválido.")

            deletada = main.conta.pop(id_c)
            return render_template('deletar.html', sucesso=True, nome=deletada[0])
        except Exception as e:
            return render_template('deletar.html', erro=f"Erro ao deletar: {e}")

    return render_template('deletar.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
