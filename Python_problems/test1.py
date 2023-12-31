import requests
import time
import snowflake.connector
import pandas as pd
import json
import warnings
import time
import datetime
from datetime import datetime
from azure.storage.filedatalake import DataLakeServiceClient,DataLakeDirectoryClient,FileSystemClient
from azure.storage.blob import BlobServiceClient
warnings.filterwarnings('ignore')



rep_id=@ReQuery4

rep_id = ['65170756d070ccc5e15931c5','651319d1451365745f96b696','6513a93b451365745f96fe8a','6513b462451365745f970038','651395402f17cbb15c76a9d2']

processed_files = []

rep_id=rep_id
url_link=@url_link
customercode=@customercode
loginid=@loginid
password=@password

ctx = snowflake.connector.connect(
        account="UCDGBCO-apollo_dataengineeringconnection.privatelink",
        user="SERVICE_DEV_PORTFOLIO_REALASSET_DATAENG",
        password="R3@Lassets",
        warehouse="PORTFOLIO_DEV_REALASSET_OTHER_WH",
        database="PORTFOLIO_DEV_DB",
        schema="REALASSET_L0"
        )
cs = ctx.cursor()

for id in rep_id:
    url = url_link+"/reportsapilogin?ActionCode=LOGIN&\
    customercode="+customercode+"&loginid="+loginid+"&password="+password+"&reportid="+id

    payload = 'CustomerCode='+customercode+'&LoginID='+loginid+'&Password='+password
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
      }

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)

    json_data=response.json()
    session_id=json_data['SessionId']
    url = url_link+"/reportsapi?ActionCode=SUBMIT"
    session_id=requests.utils.quote(session_id)
    SessionId='SessionId='+session_id+'&ReportId='+id
    payload = SessionId
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)

    json_data=response.json()
    JobId=json_data['JobId']

    time.sleep(10)
    url = url_link+"/reportsapi?ActionCode=STATUS"
    SessionId='SessionId='+session_id+'&JobId='+JobId
    print(SessionId)
    payload = SessionId

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)

    json_data=response.json()

    JobStatus=json_data['JobStatus']['JobStatus']
    for key,value in json_data.items():
        if key=='JobStatus':
            for key,value in value.items():
                if JobStatus=='RUNNING':
                    time.sleep(120)
                    json_data=response.json()
                    continue
                else:
                    JobStatus=json_data['JobStatus']['JobStatus']
                    break

    for key,value in json_data.items():
        if key=='JobStatus':
            for key,value in value.items():
                if JobStatus=='RUNNING':
                    time.sleep(120)
                    json_data=response.json()
                    continue
                else:
                    JobStatus=json_data['JobStatus']['JobStatus']
                    break    

    JobId=json_data['JobId']
    print(JobId)

    url = url_link+"/reportsapi?ActionCode=OUTPUT"

    SessionId='SessionId='+session_id+'&JobId='+JobId
    print(SessionId)
    payload = SessionId
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
      }

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)



    response_data=response.json()
    final_data=json.dumps(response_data)
    connect_str = @connect_str
    datalake_service_client = DataLakeServiceClient.from_connection_string(connect_str)
    destination_container_name = "ice"
    destination_blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    all_intervals={'year':'Y','month':'m','day':'d','hour':'H','minute':'H'}
    pattern=''
    interval=@interval
    for key,value in all_intervals.items():
        pattern=pattern+'%'+value+'/'
        if key.upper()==interval.upper():
            break
    currenttime=datetime.now()
    current_time=currenttime.strftime("%Y-%m-%d %H:%M:%S")
    date_time=datetime.strptime(current_time,'%Y-%m-%d %H:%M:%S')
    path=date_time.strftime(pattern)
    directory_path=destination_container_name+'/realinsight/'
    file_path=directory_path  # +path
    print(file_path)
    file_time=currenttime.strftime("%Y-%m-%d%H:%M:%S")
    file_name=id+' '+file_time+'.json'
    processed_files.append(file_name)
    
    #ct = datetime.datetime.now()
    INS1 = f"UPDATE RUNNING_STATS SET API_CALL_RESULT_1 = '{file_name}' WHERE REPORT_ID = '{id}'"
    INS2 = F"UPDATE RUNNING_STATS SET EXT_END_TIME = CURRENT_TIMESTAMP() WHERE REPORT_ID = '{id}'"
    cs.execute(INS1)
    cs.execute(INS2)
    try:
        file_system_client = datalake_service_client.get_file_system_client(directory_path)            
        directory_client = file_system_client.create_directory(path)
        print("Directory '%s' created successfully" % path)

        blob_client = destination_blob_service_client.get_blob_client(file_path,blob=file_name)
        blob_client.upload_blob(final_data)
        

    except OSError as error:
        print("Directory '%s' can not be created" % path)

cs.close()
ctx.close()
outputDF = pd.DataFrame({'EXTRACTED_FILES':['processed_files']})