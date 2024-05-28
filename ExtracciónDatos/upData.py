import pandas as pd
from sqlalchemy import create_engine




class DataController():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:Admin2024#@172.30.0.3:5432/testdb')
        
    def upData(self):
        
        df = pd.read_csv('data_prueba_tecnica.csv')

        nuevos_nombres = {
            "id": 'id',
            "name": "company_name",
            "company_id": "company_id",
            "amount": "amount",
            "status": "status",
            "created_at": "created_at",
            "paid_at": "updated_at",  
        }

        df = df.rename(columns=nuevos_nombres)

        
        df['created_at'] = pd.to_datetime(df['created_at'], format='mixed', errors='coerce')
        df['updated_at'] = pd.to_datetime(df['updated_at'], format='%Y-%m-%d', errors='coerce')

        
        df['company_id'] = df['company_id'].fillna('sin_nombre')

       
        print("Valores máximos en 'amount':", df['amount'].max())

        #
        limite_superior = 10**14 - 1  # 99999999999999.99

        
        df = df[df['amount'] <= limite_superior]

        
        df['amount'] = df['amount'].round(2)

        
        df = df.dropna(subset=['id'])

        
        companies_df = df[['company_id', 'company_name']].drop_duplicates()

        
        charges_df = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']]

        
        try:


            # Eliminar duplicados en companies_df
            companies_df.drop_duplicates(subset=['company_id'], inplace=True)

           
            companies_df.to_sql('companies', self.engine, if_exists='append', index=False)

        
            charges_df.to_sql('charges', self.engine, if_exists='append', index=False)

            print("Datos insertados correctamente en PostgreSQL.")
            return 'Datos insertados correctamente en PostgreSQL.'
        except Exception as e:
            print(f"Error al insertar los datos en PostgreSQL: {e}")
            return e
        
    def extractData(self):
        try:
            result = pd.read_sql_query('SELECT * FROM daily_transactions', self.engine)
            result.to_csv('daily_transactions.csv', index=False)
            return 'Se genero el csv'
        except Exception as e:
            print(f'error al generar el csv: {e}')
            return e
        
        
dataController = DataController()

dataController.upData()

print(dataController.extractData())