from abc import ABC,abstractmethod
import mysql.connector
from mysql.connector import Error

class dbConnection(ABC):

        def __init__(self,host,database,user,password):
            self.host = host
            self.database = database
            self.user = user
            self.password = password 
            self.conn = None
        
        @abstractmethod
        def connect(self):
            pass

        @abstractmethod
        def disconnect(self):
            pass 

        @abstractmethod
        def execute_query(self,query):
            pass


class mysql_connect(dbConnection):
    
    def connect(self):
        
        try:

            self.conn = mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)
            
            if self.conn.is_connected():
                db_Info = self.conn.get_server_info()
                print(f"Connected to MYSQL Server Version : {db_Info}")
                cursor = self.conn.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print(f"You are connected to the database : {record}")
                return cursor 
            
        except Error as e : 
            print(f"Error while connecting to MYSQL : {e} ")
       
    def disconnect(self):            

        if self.conn.is_connected():
            self.conn.close()
            print("MYSQL connection is closed ! ")

    def execute_query(self, query):
        
        if self.conn.is_connected():
            print("Connection established ")


# Test 
if __name__ == "__main__":

    #$ We should be calling the sub-class 
    con =    mysql_connect("localhost","suyalmukesh","root","Paridhi")
    con.connect()

    con =    mysql_connect("localhost","testdb","root","Paridhi")
    con.connect()
    con.execute_query('aa')
    con.disconnect()




