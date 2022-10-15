import sqlite3 as sq
from PyQt5 import uic, QtWidgets

# <<< functions >>>
def login_usuario():    
    usuario = janela.usuario.text()
    senha = janela.senha.text()
    banco = sq.connect("usuarios.db")
    cursor = banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario text, senha text)")
    cursor.execute(f"SELECT usuario, senha FROM usuarios WHERE senha = '{senha}'")
    login = cursor.fetchall()

    if login == []:
        login.append(("0", "0"))

    if usuario == "" or senha == "":
        if usuario == "" and senha == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou tudo! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
        elif usuario == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou o usuário! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
        elif senha == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou a senha! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
    elif usuario == login[0][0] and senha == login[0][1]:
        home()
        janela.usuario.setText("")
        janela.senha.setText("")
        janela.nomeLabel.setText(f"Nome: {login[0][0]}")
        janela.labelAviso.setText("")
        janela.labelAviso.close()
    elif usuario != login[0][0] and senha != login[0][1]:
        janela.labelAviso.show()
        janela.labelAviso.setText("Usuário ainda não cadastrado!")
        janela.usuario.setText("")
        janela.senha.setText("")

    banco.commit()
    banco.close()


def cadastrar_usuario():
    usuario = janela.usuario.text()
    senha = janela.senha.text()
    banco = sq.connect("usuarios.db")
    cursor = banco.cursor()

    senhas = []

    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario text, senha text)")
    cursor.execute("SELECT senha FROM usuarios")
    resultado = cursor.fetchall()

    for s in resultado:
        senhas.append(s[0])

    if usuario == "" or senha == "":
        if usuario == "" and senha == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou tudo! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
        elif usuario == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou o usuário! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
        elif senha == "":
            janela.labelAviso.show()
            janela.labelAviso.setText("Faltou a senha! ¯\_(ツ)_/¯ ")
            janela.usuario.setText("")
            janela.senha.setText("")
    elif senha in senhas:
        janela.labelAviso.show()
        janela.labelAviso.setText("Senha já existente!")
        janela.usuario.setText("")
        janela.senha.setText("")
    elif len(senha) < 6:
        janela.labelAviso.show()
        janela.labelAviso.setText("Senha insuficiente!")
        janela.usuario.setText("")
        janela.senha.setText("")
    else:
        cursor.execute(f"INSERT INTO usuarios VALUES ('{usuario}', '{senha}')")
        janela.labelAviso.setText("Usuário cadastrado!")
    
    banco.commit()
    banco.close()


def home():
    janela.leftMenu.show()
    janela.widget.show()
    janela.widget_2.close()
    janela.widget_3.close()
    janela.widget_4.show()
    janela.widget_5.close()


def dados():
    janela.leftMenu.show()
    janela.widget.show()
    janela.widget_2.show()
    janela.widget_3.show()
    janela.widget_4.close()
    janela.widget_5.close()


def logout():
    janela.leftMenu.close()
    janela.widget.close()
    janela.widget_2.close()
    janela.widget_3.close()
    janela.widget_4.close()
    janela.widget_5.show()


def calcular_IMC():

    if janela.pesoEdit.text() == "" or janela.alturaEdit.text() == "":
        janela.imc.setText("")
        janela.classificacao.setText("Algo está faltando!")
        janela.recomendacao.setText("")
    else:
        peso = float(janela.pesoEdit.text())
        altura = float(janela.alturaEdit.text())

        if altura < 2.51:
            altura = altura * 100

        imc = ((peso / ((altura**2)/100))*100)

        if imc < 18.5:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Magreza")
            janela.recomendacao.setText("Consequências: Fadiga, stress, ansiedade")

        elif 18.5 < imc < 25:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Peso Normal")
            janela.recomendacao.setText("Consequências: Menor risco de doenças cardíacas e vasculares")

        elif 25 < imc < 30:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Sobrepeso")
            janela.recomendacao.setText("Consequências: Fadiga, má circulação, varizes")

        elif 30 < imc < 35:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Obesidade I")
            janela.recomendacao.setText("Consequências: Diabetes, angina, infarto, aterosclerose")

        elif 35 < imc < 40:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Obesidade II")
            janela.recomendacao.setText("Consequências: Apneia do sono, falta de ar")

        elif imc > 40:
            janela.imc.setText(f"IMC: {imc:.2f}")
            janela.classificacao.setText("Classificação: Obesidade III")
            janela.recomendacao.setText("Consequências: Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC")


# <<< Main Program >>>
app = QtWidgets.QApplication([])
janela = uic.loadUi("IMC.ui")

janela.labelAviso.close()
janela.leftMenu.close()
janela.widget.close()
janela.widget_2.close()
janela.widget_3.close()
janela.widget_4.close()
janela.widget_5.show()

janela.login.clicked.connect(login_usuario)
janela.cadastrar.clicked.connect(cadastrar_usuario)
janela.homeButton.clicked.connect(home)
janela.dadosButton.clicked.connect(dados)
janela.logoutButton.clicked.connect(logout)
janela.calculatorButton.clicked.connect(calcular_IMC)

janela.show()
app.exec()