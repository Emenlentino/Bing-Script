import logging
import json
import time
from getpass import getpass

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def save_userdata():
    # Get user data and convert it to JSON for the login system
    logging.info('Starting user data collection for Microsoft Bing account.')

    try:
        uname = input('Enter username or email: \n')
        pwd = getpass('Enter password: \n')

        toWrite = {"username": [uname], "password": [pwd]}
        path_to_json = "./form_data/accounts.json"

        with open(path_to_json, "w") as datafile:
            json.dump(toWrite, datafile, indent=4)
            datafile.write("\n")

        logging.info(f"User data successfully saved to {path_to_json}.")
        logging.debug(f"Saved data: {toWrite}")

        print('Waiting 2 seconds...', flush=True)
        time.sleep(2)
        print('Accounts successfully saved.')
        time.sleep(1)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

save_userdata()
