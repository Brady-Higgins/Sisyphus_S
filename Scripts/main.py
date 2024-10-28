import tkinter as tk
from tkinter import messagebox
from Scripts.Encryption.Diary import Diary
def init():
    return None,True
    diary = Diary()
    first_login = diary.check_password_file_exists()
    return diary, first_login

def main(root, diary, first_login):
    # Set up the main Tkinter window
    root.title("Sisyphus")
    root.geometry("650x600")
    sisyphus_title = tk.Label(root, text="Sisyphus: for students", width=45, height=5, font=('Times 34'))
    sisyphus_title.pack(pady=3)
    if first_login:
        body = tk.Label(root, text="Welcome, please input your permanet password below and click submit when you're finished", width=45, height=5, font=('Times 20'))
    else:
        body = tk.Label(root, text="Welcome back, please enter your password", width=45, height=5, font=('Times 20'))
    body.pack(pady=1,padx=2)
    # Create entry widget for password input
    text_entry = tk.Entry(root, width=40)
    text_entry.pack(pady=10)

  
    # Create button to submit password
    button = tk.Button(root, text="Submit", width=15, height=2)
    button.pack(pady=10)

    # Start the main Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    diary,first_login = init()
    root = tk.Tk()
    main(root, diary,first_login)