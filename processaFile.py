import pandas as pd
import numpy as np
import pyodbc
df =  pd.read_excel('C:/Users/tinew/Downloads/cet/ct.xls', sheet_name="rel_pedido", header=None)
header_row = df[df.eq("PEDIDO").any(1)].index[0]
df.columns = df.iloc[header_row]
df = df[header_row+1:]
df = df.loc[:, :'VENDEDOR_DO_MERCADOLIVRE']
pedido_col = df.columns.get_loc("PEDIDO")
df = df.iloc[:,pedido_col:]
df.dropna(how='all', inplace=True)

#contando total de colunas
colunas = df.shape[1]
#verificando tipos
tipos = df.dtypes
#substituindo valores vazios 
df['PAGAMENTO1'].fillna(0, inplace=True)
#substituindo valores nulos da coluna Forma_pagamento_paga (string) por indefinido
df['FORMA_PAGAMENTO_PAGA'].fillna('indefinido', inplace=True)
# FORMA_PAGAMENTO_ESCOLHIDA (string) por indefinido
df['FORMA_PAGAMENTO_ESCOLHIDA'].fillna('indefinido', inplace=True)
#substituinfo valores da coluna FRETES (STRING) por indefinido
df['FRETE'].fillna(0, inplace=True)
# DATA_ENVIOS (date) por None
df['DATA_ENVIOS'].fillna('', inplace=True)
# cod_envio (STRING) POR INDEFINIDO
df['COD_ENVIO'].fillna('indefinido', inplace=True)
# OBS_CLIENTE (STRING)
df['OBS_CLIENTE'].fillna('indefinido', inplace=True)
df['PARCEIRO'].fillna('indefindo', inplace=True)
df['CUPOM_DESCONTO'].fillna('indefinido',inplace=True)
df['APELIDO'].fillna('indefinido', inplace=True)
df['RG'].fillna('indefindo', inplace=True)
df['TELEFONE'].fillna('indefinido', inplace=True)
df['TELEFONE2'].fillna('indefinido', inplace=True)
df['RAZAO'].fillna('indefinido', inplace=True)
df['CNPJ'].fillna('indefinido', inplace=True)
df['IE'].fillna('indefinido', inplace=True)
df['DESTINATARIO'].fillna('indefinido', inplace=True)
df['COMPLEMENTO'].fillna('indefinido', inplace=True)
df['DATA_PAGAMENTO'].fillna('', inplace=True)
df['COMPLEMENTO_COBRANCA'].fillna('indefinido', inplace=True)
df['VENDEDOR_DO_MERCADOLIVRE'].fillna('indefinido', inplace=True)
#verificando se há valores ausentes 


df.rename(columns={'CARTÕES':'CARTOES'}, inplace=True)
df.to_csv('cet_processado.csv', index=False)
valoresAusentes = df.isnull().sum()
df['VALOR_COMISSAO'].replace(",",".", inplace=True)
print(df.groupby('VALOR_COMISSAO').size())