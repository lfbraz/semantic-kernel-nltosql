from semantic_kernel.plugin_definition import kernel_function, kernel_function_context_parameter
from semantic_kernel import KernelContext

import pyodbc


class QueryDbPlugin:
    """
    Description: Get the result of a SQL query
    """
    def __init__(self, connection_string) -> None:
        self._connection_string = connection_string
    
    @staticmethod
    def __clean_sql_query__(sql_query):
        sql_query = sql_query.replace(";", "")
        sql_query = sql_query.replace("/n ", " ")

        return sql_query  
    
    @kernel_function(name="query_db",
                     description="Query a database using a SQL query")
    @kernel_function_context_parameter(name="input",
                                       description="SQL Query to be executed")
    
    def query_db(self, context: KernelContext) -> str:    
        # Connect to the SQL Server database
        conn = pyodbc.connect(self._connection_string)

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        try:
            cursor.execute(self.__clean_sql_query__(context["input"]))
            #result = cursor.fetchone()
            
            # Get the column names from cursor.description
            columns = [column[0] for column in cursor.description]

            # Initialize an empty list to store the results as dictionaries
            results = []

            # Fetch all rows and create dictionaries
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            context["result"] = results
        except Exception as e:
            return f"Error: {e}"
        cursor.close()
        conn.close()
        
        return str(results)
