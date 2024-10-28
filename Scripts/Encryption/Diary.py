import os
import random
import string
import sys
from datetime import datetime as d
from cryptography.fernet import Fernet

class Diary:
    def __init__(self):
        self.password_attempts = 0

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.current_directory = os.getcwd()

        self.password_directory = os.path.join(os.path.dirname(__file__), "Password.txt")
        self.storage_directory = os.path.join(os.path.dirname(__file__), "Storage.txt")
        self.sections_directory = os.path.join(os.path.dirname(__file__), "Sections.txt")
        self.first_login = True
    
    def check_password_file_exists(self):
        self.file_list = os.listdir(self.current_directory)
        if "Password.txt" in self.file_list:
            self.first_login = True
            return True
        else:
            self.first_login = False
            return False


    # def check_password_file_exists(self):
    #     self.file_list = os.listdir(self.current_directory)
    #     if "Password.txt" in self.file_list:
    #         self.new_password_file = False
    #     else:
    #         self.createPasswordFile()
    #     if "Sections.txt" in self.file_list:
    #         pass
    #     else:
    #         with open(self.sections_directory, 'w', encoding='utf-8') as f :
    #             f.writelines("")    

    def createPasswordFile(self):
        #Creates the text to fill in a password document so the password can pull pieces for the encryption code
        res = "".join(random.choices(string.ascii_uppercase + string.digits, k=3000))
        final_document_list = []
        for letter in res :
            fifty_percent = random.randint(0, 1)
            if fifty_percent == 1 :
                letter = letter.lower()
            final_document_list.append(letter)
        final_document_line = "".join(final_document_list)

        #The password file creation portion that also uploads the final_document_line text
        with open(self.password_directory, 'w', encoding='utf-8') as f :
            i=0
            temp_list = []
            for letter in final_document_line:
                i+=1
                if i%50:
                    f.writelines("".join(temp_list))
                    temp_list = []
                temp_list.append(letter)
        # expects password
        print("Password File Created")
        self.password_attempt = input("Input your permanent password: ")
        self.createStorageFile()