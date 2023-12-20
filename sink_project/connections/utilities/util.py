import json 

CRED_PATH = "/Applications/MyData/MY_DEVELOPMENT_WORK/dev_work/Python_Challenges/sink_project/connections/connections/connection_params.json"

def read_credentials(file_path):
   
    with open(file_path) as e:
        data = json.load(e)
        print(data)
    return data         



