import os
import pandas as pd
from sqlalchemy import create_engine, String, Float, Integer

folder_path = 'dataset_path'

for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)

    if os.path.isfile(filepath):
        # Read Excel file and remove unnamed columns
        df = pd.read_csv(filepath, usecols=lambda column: not column.strip().startswith("Unnamed"))

        # PostgreSQL connection settings
        db_username = 'username'
        db_password = 'password'
        db_host = 'localhost'
        db_port = 'port_number'
        db_name = 'db_name'

        # Create SQLAlchemy engine
        engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

        dtype_map = {
            'object': String,
            'float64': Float,
            'int64': Integer
        }

        # Determine data types for each column
        dtypes = {column: dtype_map[str(df[column].dtype)] for column in df.columns}

        # Create table in PostgreSQL with inferred schema
        table_name = filename.replace('.csv','')
        df.to_sql(table_name, engine, if_exists='replace', index=False, dtype=dtypes)

        print(f"{table_name} created in PostgreSQL with dynamically inferred schema.")
