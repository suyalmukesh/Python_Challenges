## Read variable @snowflake_queries 
## Execute the SQLs in snowflake as per given in @snowflake queries 
## Also , need to store the External table name in a list 
## update the variable @external_tables 

import snowflake.connector
import pandas as pd

if __name__ == '__main__':

     
    conn = snowflake.connector.connect(
        account="UCDGBCO-apollo_dataengineeringconnection.privatelink",
        user="SERVICE_DEV_PORTFOLIO_REALASSET_DATAENG",
        password="R3@Lassets",
        warehouse="PORTFOLIO_DEV_REALASSET_OTHER_WH",
        database="PORTFOLIO_DEV_DB",
        schema="REALASSET_L0"
        )
    
    cs=conn.cursor()
    
    MOVE_TO_HISTORY = """INSERT INTO RUNNING_STATS_HISTORY (REPORT_ID,DOMAIN_NAME,BATCH_ID,EXT_START_TIME,EXT_END_TIME,API_CALL_RESULT_1,API_CALL_2,API_CALL_RESULT_2,CAPTURED_TIME,STATUS,RUN_DAY)
                            SELECT REPORT_ID,
                                BATCH_ID,
                                DOMAIN_NAME,
                                EXT_START_TIME,
                                EXT_END_TIME,
                                API_CALL_RESULT_1,
                                API_CALL_2,
                                API_CALL_RESULT_2,
                                CAPTURED_TIME,
                                'DONE',
								RUN_DAY
                            FROM  RUNNING_STATS; """
    
    TRUNCATE_DRIVER = "TRUNCATE RUNNING_STATS;"
    
    INSERT_REPORT_ID = """INSERT INTO RUNNING_STATS(REPORT_ID,DOMAIN_NAME,BATCH_ID,EXT_START_TIME,EXT_END_TIME,CAPTURED_TIME,RUN_DAY) 
                          SELECT REPORT_ID,
                                 DOMAIN,
                                 BATCH,
                                 CURRENT_TIMESTAMP(),
                                 NULL,
                                 CURRENT_TIMESTAMP(),
                                 CURRENT_DATE() 
                         FROM STG_STATS_REALASSEST_REFERENCE WHERE ENVIRONMENT = 'Prod';"""

    try:
        cs.execute(MOVE_TO_HISTORY)
        cs.execute(TRUNCATE_DRIVER)
        cs.execute(INSERT_REPORT_ID)
    except Exception as e:
        print("Error while DB operation")
        cs.close()
        conn.close()
        raise e
        
    cs.close()
    conn.close()

    START_PROCESS = pd.DataFrame({'START_STATUS':['OK']})

    