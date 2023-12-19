import pandas as pd
from sqlalchemy import create_engine
server = 'XWHGQ9CY3\\SQLEXPRESS'
database = 'sampleproject'
driver = 'ODBC+Driver+17+for+SQL+Server'
trusted_connection = 'Yes'
engine = create_engine(f"mssql+pyodbc://{server}/{database}?driver={driver}&Trusted_Connection={trusted_connection}")
file_path = r'C:\Users\BD781CZ\Downloads\Source Files\CDW_SAPP_D_CALENDAR.txt'
data = pd.read_csv(file_path)
table_name = 'CALENDER_RETAIL_PROJECT'
data.to_sql(table_name, engine, if_exists='replace', index=False)
engine.dispose()
