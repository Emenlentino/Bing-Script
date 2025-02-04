import logging
import time
import os 
from os import system

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture detailed information
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

class Bing:
    def __init__(self) -> None:
        self.menu_ascii = '''
                    Ghost_Bot Farmer !\n
                        Select an action:\n
                            1) Save login to json.
                            2) Initialize json.
                            3) Crawl Bing Searches.
                            4) Donate Wallet.
                            5) Exit Program.
                        '''

    def start_bot(self):
        while True:
            try:
                option_menu_selected = int(input(self.menu_ascii))
            except ValueError:
                logging.warning("Invalid input: Please enter a valid option.")
                continue

            if option_menu_selected == 1:
                from form_data import user_define
                logging.info("Option 1 selected: Save login to JSON.")
                logging.debug(f"Loaded module output: {user_define}")

            elif option_menu_selected == 2:
                from tasker import login_post
                logging.info("Option 2 selected: Initialize JSON.")
                logging.debug(f"Loaded module output: {login_post}")

            elif option_menu_selected == 3:
                from tasker import crawl
                logging.info("Option 3 selected: Crawl Bing Searches.")
                logging.debug(f"Loaded module output: {crawl}")

            elif option_menu_selected == 4:
                path_to_md = "./tasker/donate.md"
                try:
                    with open(path_to_md , encoding='utf-8') as md_file:
                        donate_content = md_file.read()
                        logging.info("Option 4 selected: Display Donate Wallet.")
                        logging.debug(f"Content of donate.md: {donate_content}")
                        print(donate_content)
                except FileNotFoundError:
                    logging.error(f"File not found: {path_to_md}")
                time.sleep(2)

            elif option_menu_selected == 5:
                logging.info("Option 5 selected: Exiting program.")
                print("Exiting program.")
                break

            else:
                logging.warning('Invalid option selected. Please select a correct option.')

            time.sleep(1)
            system('cls' if os.name == 'nt' else 'clear')

start_handler = Bing()
start_handler.start_bot()
