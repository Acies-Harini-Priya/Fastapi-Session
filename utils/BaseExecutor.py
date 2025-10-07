import psycopg2
import pandas as pd

class BaseExecutor:
    def __init__(self, db_config = None):
        """
        Initialize the database connection configuration.
        
        Args:
            db_config (dict): A dictionary with keys: dbname, user, password, host, port.
        """
        self.db_config = db_config

    def executeSelect(self, query, values=None, get_as_packet=False):
        """
        Executes a SELECT query and fetches the results.

        Args:
            query (sql.SQL): The query to be executed.
            values (tuple): Parameters for the query.
            get_as_packet (bool): Whether to return results as a Pandas DataFrame.

        Returns:
            tuple: (data, message)
        """
        try:
            # Connect to the database
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()

            # Execute the query
            cursor.execute(query, values)

            # Fetch all results
            rows = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]

            if get_as_packet:
                # Convert to Pandas DataFrame
                dataframe = pd.DataFrame(rows, columns=col_names)
                return dataframe, "Query executed successfully."
            else:
                return rows, "Query executed successfully."

        except psycopg2.Error as e:
            return None, f"Database error: {e}"
        finally:
            # Ensure resources are cleaned up
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    def executeInsert(self, query, values=None):
        """
        Executes an INSERT query and returns the number of rows affected.

        Args:
            query (sql.SQL): The query to be executed.
            values (tuple): Parameters for the query.

        Returns:
            tuple: (rows_affected, message)
        """
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)

            connection.commit()

            rows_affected = cursor.rowcount
            return rows_affected, "Insert query executed successfully."
        except psycopg2.Error as e:
            if connection:
                connection.rollback()
            return 0, f"Database error: {e}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    def executeUpdate(self, query, values=None):
        """
        Executes an UPDATE query in the database.

        Args:
            query (sql.SQL): The UPDATE query to execute.
            values (tuple): The parameters for the query.

        Returns:
            tuple: (rows_affected, message)
        """
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()

            cursor.execute(query, values)
            rows_affected = cursor.rowcount  

            connection.commit()

            return rows_affected, "Query executed successfully."
        except psycopg2.Error as e:
            if connection:
                connection.rollback()
            return 0, f"Database error: {e}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    def executeDelete(self, query, values=None):
        """
        Executes a DELETE query in the database.

        Args:
            query (sql.SQL): The DELETE query to execute.
            values (tuple): The parameters for the query.

        Returns:
            tuple: (rows_affected, message)
        """
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(**self.db_config)
            cursor = connection.cursor()

            cursor.execute(query, (values,))
            rows_affected = cursor.rowcount  

            connection.commit()

            return rows_affected, "Query executed successfully."
        except psycopg2.Error as e:
            if connection:
                connection.rollback()
            return 0, f"Database error: {e}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()