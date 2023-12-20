from abc import ABC,abstractmethod
import snowflake.connector 


class snowflakeConnection(ABC):
    def __init__(self,username,password,account,warehouse,database,schema):
        self.username = username
        self.password = password
        self.account = account 
        self.warehouse = warehouse
        self.database = database
        self.schema = schema 
        self.conn = None 
    
    @abstractmethod 
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self,query):
        pass 
    
    @abstractmethod
    def fetch_data(self):
        pass
    
    @abstractmethod
    def write_data(self,table_name):
        pass 
    
    @abstractmethod
    def disconnect(self):
        pass

class sf_connect(snowflakeConnection):

    def connect(self):
        try:
            self.conn = snowflake.connector.connect(
                user = self.username
                password = self.password 
                account = self.account
                warehouse = self.warehouse
                database = self.database
                schema = self.schema)
        except Exception as e :
            print(f"Connection failed as {e}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print(f"Snowflake connection closed !! ")

    def execute_query(self, query):
        if self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query)
                curr.close()
                return 0 
        print("No snowflake connection !! ")
        return -1 

    def fetch_data(self,query):
        if self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query)
                return curr.fetchall()
        print("No snowflake connection !! ")
        return -1    

    def write_data(self,table_name,data):
        ## Assume data is a list of tuples or a pandas dataframe 
        if self.conn:
            with self.conn.cursor() as curr:
                insert_query = f"INSERT INTO {table_name} VALUES (?,?,?) "
                curr.execute(insert_query)
                curr.close() 
        print("No snowflake connection !! ")
        return -1






        

