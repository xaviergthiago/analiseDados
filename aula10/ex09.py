from sqlalchemy import create_engine
import pandas as pd
host = 'localhost' #host = '127.0.0.1'
user = 'root'
password = ''
database = 'aulapandas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
df = pd.read_sql('SELECT * FROM odontologia', con=engine)
print(df.to_string()) #Exibe o DataFrame completo, sem truncar as linhas ou colunas.