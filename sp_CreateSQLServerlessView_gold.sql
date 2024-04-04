USE gold_db
GO

CREATE OR ALTER PROC sp_CreateSQLServerlessView_gold @ViewName NVARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)
    SET @statement = N'CREATE OR ALTER VIEW ' + QUOTENAME(@ViewName) + ' AS
        SELECT *
        FROM
            OPENROWSET(
            BULK ''https://bktourismstorage.dfs.core.windows.net/gold/' + @ViewName + '/'',
            FORMAT = ''DELTA''
        ) AS [result]
    '

EXEC (@statement)

END
GO