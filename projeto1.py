# Lógica de Programação

# Passo 0 - Entender o desafio que devo resolver

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (pasta vendar)

import os
import plotly.express as px
import pandas as pd #Apelido, para abreviar
pasta = r'C:\Users\richa\Desktop\Cursos\Curso-Pthon-HeitorLima\Vendas'
lista_arquivo = os.listdir(pasta)

# Passo 2 - Importas as bases de dados de vendas

tabela_total = pd.DataFrame()
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(fr"C:\Users\richa\Desktop\Cursos\Curso-Pthon-HeitorLima\Vendas\{arquivo}")
        tabela_total = tabela_total._append(tabela)

# Passo 3 - Tratar / Compilar as bases de dados

print(tabela_total)

# Passo 4 - Calcular o produto mais vendido (em quantidade)

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos["Quantidade Vendida"].sort_values(ascending=True)

print(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"]*tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento["Faturamento"].sort_values(ascending=True)
print(tabela_faturamento)

# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um grafico/dashboard

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas["Faturamento"].sort_values(ascending=True)
print(tabela_lojas)

#Criando gráfico

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()
