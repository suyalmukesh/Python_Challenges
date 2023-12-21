import requests
import time
import pandas as pd
import snowflake.connector

def get_report_id_from_file(file_name):
    return file_name.split(" ")[0]

API_URL_TEMPLATE = "http://10.254.50.120:9191/realinsight/FILE_NAME"
store_snowflake_queries=[]
call_api_info = []

#file_name = '665085fc5e50f4e84d1b39155 2023-11-0101:19:50.json'
if __name__ == "__main__":
    in_file_list = list(inputDF['file_list'])  
  
  
    temp = []
    conn = snowflake.connector.connect(
        account="UCDGBCO-apollo_dataengineeringconnection.privatelink",
        user="SERVICE_DEV_PORTFOLIO_REALASSET_DATAENG",
        password="R3@Lassets",
        warehouse="PORTFOLIO_DEV_REALASSET_OTHER_WH",
        database="PORTFOLIO_DEV_DB",
        schema="REALASSET_L0"
        )
    
    cs=conn.cursor()
 
    for file_name in in_file_list:
        print(file_name) 
        report_id = str(get_report_id_from_file(file_name))
        
        try:
           
            url = API_URL_TEMPLATE.replace("FILE_NAME",file_name)
            temp.append(url)
            response = requests.get(url)
            res_code = response.status_code
            temp.append(res_code)
            query = response.content  
            temp.append(query)
            call_api_info.append(temp)
            query=query.decode()
            
            EXT_TIME_TAKEN = """UPDATE RUNNING_STATS  SET EXT_TIME_MINS = DATEDIFF(MINUTE,EXT_START_TIME::TIMESTAMP,EXT_END_TIME::TIMESTAMP)"""
            cs.execute(EXT_TIME_TAKEN)
            
            first_few = query[0:50]
            
            Query1 = f"UPDATE RUNNING_STATS SET API_CALL_2 = COALESCE('{url}','UNKNOWN') , API_CALL_RESULT_2 = COALESCE('{first_few}','UNKNOWN') WHERE REPORT_ID = '{report_id}'"
            cs.execute(Query1)

            if 'CREATE' not in query:
                ERROR_STATUS = f"UPDATE RUNNING_STATS SET STATUS = 'ERROR' WHERE REPORT_ID = '{report_id}'"
                cs.execute(ERROR_STATUS)
            else:
                SUCCESS_STATUS = f"UPDATE RUNNING_STATS SET STATUS = 'OK' WHERE REPORT_ID = '{report_id}'"
                cs.execute(SUCCESS_STATUS)


            store_snowflake_queries.append(query)
            
            
        except Exception as e :
            temp.append(e)
            store_snowflake_queries.append(temp)
            print(f"Error as {e}")
            exit -1 

  
    cs.close()
    conn.close()
    snowflake_queries = pd.DataFrame({'SF_QUERIES': store_snowflake_queries})
   