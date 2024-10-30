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

    def createStorageFile(self,password_attempt): 
        self.password_attempt = password_attempt     
        with open(self.storage_directory, 'w', encoding='utf-8') as f:
            self.createEncryptionKey()
            message = bytes("[0] V4l1dP4ssw0rd 4uth0r1zedUs4g3","utf-8")
            f.writelines(str(self.fernet_object.encrypt(message)))
        f.close()

    def createEncryptionKey(self,password_attempt):
        numeric_values = [ord(char) for char in password_attempt]
        i =0
        while len(numeric_values) < 43:
            additional_constant = int(numeric_values[i]/2)
            i+=1
            for num in numeric_values:
                if len(numeric_values) <43:
                    numeric_values.append(num+additional_constant)
        password_list = []
        encryption_digits = []
        with open(self.password_directory, 'r', encoding='utf-8') as f :
            for line in f:
                password_line = line
            f.close()
        for char in password_line:
            password_list.append(char)
        for val in numeric_values:
            encryption_digits.append(password_list[val])
        encryption_digits.append("=")
        encryption_key = "".join(encryption_digits)
        encryption_key_bytes = bytes(encryption_key,"utf-8")
        self.encryption_key = encryption_key_bytes
        self.fernet_object = Fernet(self.encryption_key)

    def validateIdentity(self):
        with open(self.storage_directory, 'r', encoding='utf-8') as f:
            validation_line = f.readline()
            val_list = []
            for letter in validation_line:
                val_list.append(letter)
            new_val = val_list[2 :-1]
            character = "".join(new_val)
            byte_validation_line = bytes(character, 'utf-8')
            password_correct = False

            try :
                validation_line_decrypted = self.fernet_object.decrypt(byte_validation_line)
                password_correct = True
            except :
                self.password_attempts += 1
                if self.password_attempts == 3 :
                    print("Too many Incorrect Attempts")
                    sys.exit()
                else :
                    print("Incorrect Password, Please Retry")
                    self.passwordFileCheck()

            if password_correct :
                string_validation_line_d = bytes.decode(validation_line_decrypted)
                if string_validation_line_d == "[0] V4l1dP4ssw0rd 4uth0r1zedUs4g3" :
                    self.Journal()
                else :
                    self.password_attempts += 1
                    if self.password_attempts == 3 :
                        print("Too many Incorrect Attempts")
                        sys.exit()
                    else :
                        print("Incorrect Password, Please Retry")
                        self.passwordFileCheck()