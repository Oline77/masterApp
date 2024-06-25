import tkinter.messagebox as tkmb
import firebase_admin
from firebase_admin import credentials, firestore
import customtkinter as ctk
from home_page import MainGUI

class LoginApp:
    def __init__(self):
        # Initialize Firebase
        self.cred = credentials.Certificate("tkinter-42267.json")
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        
        # Configure interface
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize main application window
        self.app = ctk.CTk()
        self.app.geometry("400x400")
        self.app.resizable(width=False, height=False)
        self.app.title("Login")
        
        self.build_interface()
    
    def build_interface(self):
        label = ctk.CTkLabel(self.app, text="Bienvenue, \nVeuillez vous connecter")
        label.pack(pady=20)
        
        frame = ctk.CTkFrame(master=self.app)
        frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        label = ctk.CTkLabel(master=frame, text='Login')
        label.pack(pady=12, padx=10)
        
        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)
        
        self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.user_pass.pack(pady=12, padx=10)
        
        button = ctk.CTkButton(master=frame, text='Login', hover_color='green', command=self.login)
        button.pack(pady=12, padx=10)
        
        checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
        checkbox.pack(pady=12, padx=10)
        
        self.progressbar = ctk.CTkProgressBar(master=frame, orientation="horizontal")
        self.progressbar.set(0)
        self.app.mainloop()
    
    def login(self):
        self.progressbar.pack()
        self.progressbar.start()
        username = self.user_entry.get()
        password = self.user_pass.get()
        
        # Query Firestore collection
        collection_ref = self.db.collection("tkinter-testing")
        query = collection_ref.where("username", "==", username).limit(1)
        docs = query.stream()
        
        login_successful = False
        
        for doc in docs:
            doc_data = doc.to_dict()
            if doc_data['password'] == password:
                login_successful = True
                break
        
        if login_successful:
            self.open_main_application()
        else:
            tkmb.showwarning(title='Login Failed', message='Invalid username or password')
        self.progressbar.stop()

    def open_main_application(self):
        self.app.destroy()  # Close the login window
        main_app = ctk.CTk()  # Create a new root window for the main application
        MainGUI(main_app)
        main_app.mainloop()


if __name__ == "__main__":
    LoginApp()
