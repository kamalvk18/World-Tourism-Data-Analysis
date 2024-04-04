Steps:

1. Downloaded dataset from kaggle https://www.kaggle.com/datasets/arnavvvvv/world-tourism?rvi=1.
2. Ingested data from local to postgreSQL using to_pg_script.py script.
3. Ingest data from postgreSQL to ADLS Gen2 using an ADF Pipeline.
4. Then performed transformations using storagemount.ipynb and bronze_to_gold.ipynb scripts inside Azure databricks on the ingested data present in ADLS Gen2.
   
   ![image](https://github.com/kamalvk18/World-Tourism-Data-Analysis/assets/69080406/37eccdf4-723a-4609-9927-173eb659f5cd)
   
5. Now the transformations are done and stored as delta files into gold container.
6. To Create views on top of available delta files in ADLS, A Pipeline is built in Azure Synapse analytics which gets the table names from ADLS and runs stored procedure(sp_CreateSQLServerlessView_gold.sql) to create views on top of it in ServerLess SQL Database in Azure synapse.
   
   ![image](https://github.com/kamalvk18/World-Tourism-Data-Analysis/assets/69080406/2a07425a-4f23-447f-9f27-1d5d0d5c0587)

This complete pipeline is automated such that even if a new record is inserted into the local postgreSQL, that will be picked and ingested.

Thanks for reading!
