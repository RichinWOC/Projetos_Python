import psycopg2
from time import sleep
from tkinter import *
import acoes
import random
import home
import win32com.client as win32

conn = psycopg2.connect(host="localhost", database="meuprogPython3", user="postgres", password="246800@r")
cursor = conn.cursor()

def cadastrar(nome, senha, codigo, email, janelaV):

    cursor.execute(f"INSERT INTO funcionario (nome, senha, valor_vendido, codigo, email) VALUES ('{nome}', '{senha}', '{0}', '{codigo}', '{email}');")
    conn.commit()
    janelaV.destroy()
    home.home()

def logar(nome, senha, janela):
    cursor.execute("SELECT * FROM funcionario;")
    funcionarios = cursor.fetchall()
    for funcionario in funcionarios:
        if nome == funcionario[5] and senha == funcionario[2]:
            janela.destroy()
            acoes.menu()

    lbl_erro1 = Label(janela, text="Erro no login!", font=("Arial", 16, "bold"), fg="red", bg="lightblue")
    lbl_erro1.pack()
    lbl_erro2 = Label(janela, text="Senha ou nome incorretos", font=("Arial", 10), fg="red", bg="lightblue")
    lbl_erro2.pack()
    janela.mainloop()



def cadastro():
    codigo = random.randint(1, 9999)
    codigo = f"{codigo:04d}"
    codigoV = random.randint(1, 99999)
    codigoVQ = f'{codigoV:05d}'

    janela = Tk()

    janela.title("Cadastro")

    janela.configure(bg="lightblue")

    janela.geometry('600x600')

    entrada_var1 = StringVar()
    entrada_var2 = StringVar()
    entrada_var3 = StringVar()
    entrada_var4 = StringVar()

    txt_cadastro = Label(janela, text="CADASTRO", font=("Arial", 24, "bold"), bg="lightblue")
    txt_cadastro.pack(pady=20)

    txt_nome = Label(janela, text="Digite seu nome: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_nome.pack(pady=10)

    entryN = Entry(janela, width=25, textvariable=entrada_var1, borderwidth=2, font=12)
    entryN.pack()

    txt_email = Label(janela, text="Digite seu Email: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_email.pack(pady=10)

    entryE = Entry(janela, width=25, textvariable=entrada_var4, borderwidth=2, font=12)
    entryE.pack()

    txt_senha = Label(janela, text="Digite sua senha: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_senha.pack(pady=10)

    entryS = Entry(janela, width=25, textvariable=entrada_var2, borderwidth=2, font=12, show="*")
    entryS.pack()

    txt_senhaC = Label(janela, text="Confirme sua senha: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_senhaC.pack(pady=10)

    entrySC = Entry(janela, width=25, textvariable=entrada_var3, borderwidth=2, font=12, show="*")
    entrySC.pack()

    def enviarCodigo(email, nome, senha, senhaC):
        janela.destroy()
        outlook = win32.Dispatch("outlook.application")
        msg = outlook.CreateItem(0)
        msg.Subject = "Verificar Eail"
        msg.To = f"{email}"
        msg.HTMLBody = f"""
        <center><h1>CÓDIGO</h1></center>
        <p style='font-size: 16px'>Abaixo você verá um código, insira o no menu de cadastro para poder fazer verificação</h2>
        <center><h3 align='center' style='border: 1px solid black; padding: 10px; font-size:40px; width:200px;'>{codigoVQ}</h3></center>
        """

        janelaV = Tk()

        entrada_var5 = StringVar()

        msg.Send()

        janelaV.title("Confirmar Email")

        janelaV.geometry("400x400")

        janelaV.configure(bg="lightblue")

        txt_confimarcao = Label(janelaV, text="CONFIRMAR EMAIL", font=("Arial", 24, "bold"), bg="lightblue")
        txt_confimarcao.pack(pady=20)

        txt_codigo = Label(janelaV, text="Digite o codigo de verificação: ", width=30, bg="lightblue", font=("Arial", 15))
        txt_codigo.pack(pady=10)

        entryCV = Entry(janelaV, width=25, textvariable=entrada_var5, borderwidth=2, font=12)
        entryCV.pack()

        def verificar_codigo():
            codigoDV = entrada_var5.get()
            codigoDV = codigoDV.replace(" ", "")
            if codigoDV == codigoVQ:
                cadastrar(nome, senha, codigo, email, janelaV)
            else:
                print("erro")

        btn_verificar = Button(janelaV, width=20, height=3, text="Cadastrar", command=verificar_codigo, bg="blue", fg="white", font=15)
        btn_verificar.pack(pady=30)

        janelaV.mainloop()

    def verificar_email():
        nome = entrada_var1.get()
        nome = nome.replace(" ", "")
        email = entrada_var4.get()
        email = email.replace(" ", "")
        senha = entrada_var2.get()
        senha = senha.replace(" ", "")
        senhaC = entrada_var3.get()
        senhaC = senhaC.replace(" ", "")
        if senha == senhaC:
            enviarCodigo(email, nome, senha, senhaC)
        else:
            lbl_erro1 = Label(janela, text="Senha incorreta!", font=("Arial", 16, "bold"), fg="red", bg="lightblue")
            lbl_erro1.pack()

    btn_cadastrar = Button(janela, width=20, height=3, text="Cadastrar", command=verificar_email,bg="blue", fg="white", font=15)
    btn_cadastrar.pack(pady=30)

    janela.mainloop()

def login():

    janela = Tk()

    janela.title("Login")

    janela.configure(bg="lightblue")

    janela.geometry('600x600')

    entrada_var1 = StringVar()
    entrada_var2 = StringVar()

    txt_login = Label(janela, text="LOGIN", font=("Arial", 24, "bold"), bg="lightblue")
    txt_login.pack(pady=20)

    txt_email = Label(janela, text="Digite seu email: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_email.pack(pady=10)

    entryN = Entry(janela, width=25, textvariable=entrada_var1, borderwidth=2, font=12)
    entryN.pack()

    txt_senha = Label(janela, text="Digite sua senha: ", width=30, bg="lightblue", font=("Arial", 15))
    txt_senha.pack(pady=10)

    entryS = Entry(janela, width=25, textvariable=entrada_var2, borderwidth=2, font=12, show="*")
    entryS.pack()

    def obter_dados_e_logar():
        email = entrada_var1.get()
        email = email.replace(" ", "")
        senha = entrada_var2.get()
        senha = senha.replace(" ", "")
        logar(email, senha, janela)

    btn_logar = Button(janela, width=20, height=3, text="Logar", command=obter_dados_e_logar, bg="blue", fg="white", font=15)
    btn_logar.pack(pady=30)

    janela.mainloop()


