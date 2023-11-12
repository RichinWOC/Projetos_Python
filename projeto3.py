import pandas as pd
import win32com.client as win32

# Importar a base de dados

tabela = pd.read_excel("Vendas.xlsx")

# Fazer o tratamento de dados

pd.set_option("display.max_columns", None)

# Faturamento por loja

tabela_faturamentoL = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(tabela_faturamentoL)
print("="*47)

# Quantidade de produtos vendidos por loja

tabela_qtdL = tabela[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(tabela_qtdL)
print("="*47)

# Ticket médio por produto por loja

tabela_ticketML = (tabela_faturamentoL["Valor Final"]/tabela_qtdL["Quantidade"]).to_frame()
tabela_ticketML = tabela_ticketML.rename(columns={0: "Ticket Médio"})
print(tabela_ticketML)
print("="*47)

# Enviar um email por relatório


outlook = win32.Dispatch("outlook.application")
msg = outlook.CreateItem(0)
msg.Subject = "Tabela Vendas"
msg.To = "rwo.camargo@unesp.br"
msg.HTMLBody = f"""
<h1>Prezado Xuxu,</h1>

<h2>Segue a baixo o Relatório de Vendas por cada Loja.</h2>

<p>{'='*47}</p>

<h2>Faturamento:</h2>

<p>{tabela_faturamentoL.to_html(formatters={"Valor Final": "R${:,.2f}".format})}</p>

<p>{'='*47}</p>

<h2>Quantidade:</h2>

<p>{tabela_qtdL.to_html()}</p>

<p>{'='*47}</p>

<h2>Ticket Médio:</h2>

<p>{tabela_ticketML.to_html(formatters={"Ticket Médio": "R${:,.2f}".format})}</p>

<p>{'='*47}</p>

<h3>Qualquer duvida estou a disposição.</h3>

<p>Att, Richard.</p>
"""
msg.Send()
print("Email Enviado")