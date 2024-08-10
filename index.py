import time
import os 
from os import system

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
                print("Please enter a valid option.")
                continue

            if option_menu_selected == 1:
                from form_data import user_define
                print(user_define)

            elif option_menu_selected == 2:
                from tasker import login_post
                print(login_post)

            elif option_menu_selected == 3:
                from tasker import crawl
                print(crawl)

            elif option_menu_selected == 4:
                path_to_md = "./tasker/donate.md"
                with open(path_to_md , encoding='utf-8') as md_file:
                    print(md_file.read())
                time.sleep(2)

            elif option_menu_selected == 5:
                print("Exiting program.")
                break

            else:
                print('Please select a correct option.')

            time.sleep(1)
            system('cls' if os.name == 'nt' else 'clear')

start_handler = Bing()
start_handler.start_bot()