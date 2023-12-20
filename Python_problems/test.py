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
    
    MOVE_TO_HISTORY = """INSERT INTO RUNNING_STATS_HISTORY (REPORT_ID,BATCH_ID,EXT_START_TIME,EXT_END_TIME,API_CALL_RESULT_1,API_CALL_2,API_CALL_RESULT_2,CAPTURED_TIME,STATUS,RUN_DAY)
                            SELECT REPORT_ID,
                                DOMAIN,
                                BATCH_ID,
                                EXT_START_TIME,
                                EXT_END_TIME,
                                API_CALL_RESULT_1,
                                API_CALL_2,
                                API_CALL_RESULT_2,
                                CAPTURED_TIME,
                                'DONE',
								RUN_DAY
                            FROM  RUNNING_STATS WHERE STATUS = 'OK'; """
    
    TRUNCATE_DRIVER = "DELETE FROM RUNNING_STATS WHERE STATUS = 'OK';"

    CLEAR_STATS = """UPDATE RUNNING_STATS 
                            SET API_CALL_RESULT_1 = NULL,
                                API_CALL_2 = NULL,
                                EXT_START_TIME = CURRENT_TIMESTAMP(),
                                EXT_END_TIME = NULL,
                                API_CALL_RESULT_2 = NULL,
                                CAPTURED_TIME = CURRENT_TIMESTAMP(),
                                RUN_DAY = CURRENT_DATE()                           
                            WHERE STATUS = 'ERROR' """
    
    MOVE_LOAD_STATS_TO_HIST = """INSERT INTO LOAD_STATS_HISTORY ( DATABASE_NAME,SCHEMA,VIEW_NAME,CURRENT_COUNT,PREVIOUS_COUNT,DIFFERENCE,REFRESHED_DATE,PREV_REFRESHED_DATE)
                                        SELECT DATABASE_NAME,
                                                SCHEMA,
                                                VIEW_NAME,
                                                CURRENT_COUNT,
                                                PREVIOUS_COUNT,
                                                DIFFERENCE,
                                                REFRESHED_DATE,
                                                PREV_REFRESHED_DATE 
                                        FROM LOAD_STATS; """
    
    MOVE_MERGE_STATS_TO_HIST = """INSERT INTO MERGE_STATS_HISTORY (QUERY_NUMBER,LAST_RUN_STATUS,ROWS_AFFECTED,LAST_MODIFIED,MERGE_QUERY_DESCRIPTION,ERROR_DETAILS)
                                        SELECT QUERY_NUMBER,
                                                LAST_RUN_STATUS,
                                                ROWS_AFFECTED,
                                                LAST_MODIFIED,
                                                MERGE_QUERY_DESCRIPTION,
                                                ERROR_DETAILS 
                                        FROM MERGE_STATS;  """
    try:
        #cs.execute(MOVE_TO_HISTORY)
        #cs.execute(TRUNCATE_DRIVER)
        cs.execute(CLEAR_STATS)
        cs.execute(MOVE_LOAD_STATS_TO_HIST)
        cs.execute(MOVE_MERGE_STATS_TO_HIST)
    
    except Exception as e:
        print("Error while DB operation")
        cs.close()
        conn.close()
        raise e
        
    cs.close()
    conn.close()

    START_PROCESS = pd.DataFrame({'START_STATUS':['OK']})