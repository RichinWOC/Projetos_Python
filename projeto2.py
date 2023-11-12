# Identificar o motivo dos clientes estarem cancelando o cartão

#Imports

import pandas as pd
from pprint import pprint

# Passo 1 - Importar a base de dados

tabela = pd.read_csv(fr"C:\Users\richa\Desktop\Cursos\Curso-Pthon-HeitorLima\ClientesBanco.csv", encoding="Latin1")

# Passo 2 - Visualizar e tratar a base de dados

tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()

# Passe 3 - "Dar uma olhada" na base de dados
pprint(tabela.describe().round(1))

# Passe 4 - Construir uma análise para identificar o motivo de cancelamento