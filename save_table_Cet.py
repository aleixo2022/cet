import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CD-PC-061\SQLEXPRESS;'
                      'Database=UNIMARCAS;'
                      'UID=sa;'
                      'PWD=musica2000;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor() 
df = pd.read_csv('C:/Users/tinew/Downloads/cet/cet_processado.csv') 

for index, row in df.iterrows():      
   sql = """INSERT INTO cetCorreios (PEDIDO,DATA_PEDIDOS,HORA,SUBTOTAL_DE_PRODUTOS,IMPOSTOS,LOCAL_VENDA,FRETE,VALOR_FRETE,PAGAMENTO1,
   FORMA_PAGAMENTO_ESCOLHIDA,DATA_ENVIOS,COD_ENVIO,OBS_CLIENTE,OBS_LOJA,STATUS,PARCEIRO,VALOR_COMISSAO,CUPOM_DESCONTO,DESCONTO,ACRESCIMO_FORMA,
   ID_CLIENTE,CLIENTE,APELIDO,RG,CPF,EMAIL,TELEFONE,TELEFONE2,RAZAO,CNPJ,IE,DESTINATARIO,ENDERECO,NUM,CIDADE,ESTADO,CEP,COMPLEMENTO,BAIRRO,
   PAIS,DATA_PAGAMENTO,VALOR_PAGTO,FORMA_PAGAMENTO_PAGA,ENDERECO_COBRANCA,NUM_COBRANCA,CIDADE_COBRANCA,ESTADO_COBRANCA,CEP_COBRANCA,
   COMPLEMENTO_COBRANCA,BAIRRO_COBRANCA,PAIS_COBRANCA,TOTAL,CARTOES,VENDEDOR_DO_MERCADOLIVRE) 
   VALUES (?, ?, ?,?,?,?,?,?,?,?,
           ?, ?, ?,?,?,?,?,?,?,?,
           ?, ?, ?,?,?,?,?,?,?,?,
           ?, ?, ?,?,?,?,?,?,?,?,
           ?, ?, ?,?,?,?,?,?,?,?,
           ?,?,?,?)"""        
   cursor.execute(sql, 
                  row['PEDIDO'],row['DATA_PEDIDOS'],row['HORA'],row['SUBTOTAL_DE_PRODUTOS'],row['IMPOSTOS'],row['LOCAL_VENDA'],row['FRETE'],
row['VALOR_FRETE'],row['PAGAMENTO1'],row['FORMA_PAGAMENTO_ESCOLHIDA'],row['DATA_ENVIOS'],row['COD_ENVIO'],row['OBS_CLIENTE'],
row['OBS_LOJA'],row['STATUS'],row['PARCEIRO'],row['VALOR_COMISSAO'],row['CUPOM_DESCONTO'],row['DESCONTO'],row['ACRESCIMO_FORMA'],
row['ID_CLIENTE'],row['CLIENTE'],row['APELIDO'],row['RG'],row['CPF'],row['EMAIL'],row['TELEFONE'],
row['TELEFONE2'],row['RAZAO'],row['CNPJ'],row['IE'],row['DESTINATARIO'],row['ENDERECO'],row['NUM'],row['CIDADE'],
row['ESTADO'],row['CEP'],row['COMPLEMENTO'],row['BAIRRO'],row['PAIS'],row['DATA_PAGAMENTO'],row['VALOR_PAGTO'],
row['FORMA_PAGAMENTO_PAGA'],row['ENDERECO_COBRANCA'],row['NUM_COBRANCA'],row['CIDADE_COBRANCA'],row['ESTADO_COBRANCA'],
row['CEP_COBRANCA'],row['COMPLEMENTO_COBRANCA'],row['BAIRRO_COBRANCA'],row['PAIS_COBRANCA'],row['TOTAL'],row['CARTOES'],
row['VENDEDOR_DO_MERCADOLIVRE'],
) 
conn.commit() 
cursor.close()
conn.close()




 