import requests
import time
import snowflake.connector
import pandas as pd

def update_running_stats_error(sf_cursor,query=None):

    if query is None:
        query =  """INSERT INTO RUNNING_STATS_ERROR 
                        SELECT 
                                REPORT_ID,
                                DOMAIN_NAME,
                                BATCH_ID,
                                EXT_START_TIME,
                                EXT_END_TIME,
                                EXT_TIME_MINS,
                                API_CALL_RESULT_1,
                                API_CALL_2,
                                API_CALL_RESULT_2,
                                CAPTURED_TIME,
                                STATUS,
                                RUN_DAY
                        FROM PORTFOLIO_DEV_DB.REALASSET_L0.RUNNING_STATS
                        WHERE STATUS = 'ERROR'; """
        
    try:
        sf_cursor.execute(query)

    except Exception as e:     
        print(f"{query} : {e}")
        return -1 
    return 0 
    


def read_file_from_azure(connection_string,container_name,blob_name):

        from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
       
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        content = blob_client.download_blob()
        data = content.readall()
        decoded_data = data.decode('utf-8')
       
        cleaned_data = decoded_data.replace('\n', '').replace('\r', '')
       
        query_list = cleaned_data.split(";")
        query_list = [query for query in query_list if len(query) > 0 ]
        return query_list 



