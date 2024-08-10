import json
import time
from getpass import getpass

def save_userdata():
    # Get user-data and convert it to json for login system !
    print('Please provide your Microsoft Bing account !\n')
    uname = input('Enter username or email : \n')
    pwd = getpass('Enter password : \n')

    toWrite = {"username": [uname],"password": [pwd]}

    path_to_json = "./form_data/accounts.json"

    with open(path_to_json , "w") as datafile:
        json.dump(toWrite, datafile , indent=4)
        datafile.write("\n")

    print('waiting 2 seconds...', flush=True)
    time.sleep(5)
    print(f'accounts successfully saved',uname)
    time.sleep(1)

save_userdata()