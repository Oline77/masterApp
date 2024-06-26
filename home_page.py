import customtkinter as ctk
from tkinter import PhotoImage
from pathlib import Path
from PIL import Image
import openai
import firebase_admin
from firebase_admin import credentials, firestore

class MainGUI:
    def __init__(self, root):
        # Initialize Firebase
        self.cred = credentials.Certificate("tkinter-42267.json")
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        
        self.root = root
        self.root.geometry("700x460")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="#FFFFFF")
        self.root.title("Main Application")

        self.create_widgets()

    def create_widgets(self):
        # Frame to hold the content
        self.frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="#FFFFFF")
        self.frame.pack(fill="both", expand=True)
        
        
        #Frame menu
        self.frame2 = ctk.CTkFrame(master=self.frame, width=200,height=200, corner_radius=0, fg_color="#265461")
        self.frame2.pack(side="left", fill="both", expand=True)
        self.frame2.place(x=0, y=0)
        self.frame2.place_configure(height="700px", width="150px")
        
        #frame menu 1
        self.frame3 = ctk.CTkFrame(master=self.frame, width=50,height=50, corner_radius=0, fg_color="#FFFFFF")
       
        
        
        # Welcome text
        self.welcome_label = ctk.CTkLabel(self.frame, text="Bienvenue", font=("Arial", 24, "bold"),bg_color="#265461", text_color="#FFFFFF")
        self.welcome_label.pack(pady=20)
        self.welcome_label.place(x=15, y=5)
        
        # Frame 3 component
        self.start_button = ctk.CTkButton(self.frame3, text="Sauvegarder", command=self.sauvegarder_action,font=("Arial", 16, "bold"), width=130, height=30, hover_color="green")
        self.start_button.pack(pady=20)
        self.start_button.place(x=370, y=400)  
        
        self.label_texte = ctk.CTkLabel(self.frame3, text="Paramètres",text_color="black", font=("Arial", 24, "bold"))
        self.label_texte.pack(pady=20)
        self.label_texte.place(x=200, y=10)
        
        self.label_texte_api = ctk.CTkLabel(self.frame3, text="API Key ChatGPT :",text_color="black", font=("Arial", 14))
        self.label_texte_api.pack(pady=20)
        self.label_texte_api.place(x=150, y=70)
        self.entry_api_key = ctk.CTkEntry(self.frame3, placeholder_text="api key", width=130, height=30)
        self.entry_api_key.pack(pady=20)
        self.entry_api_key.place(x=280, y=70)
        
        
        
        #Menu button
        self.home_button = ctk.CTkButton(self.frame2, text="Home", command=self.home_menu_action,font=("Arial", 16, "bold"),  width=130, height=30)
        self.home_button.pack(pady=20)
        self.home_button.place(x=15, y=140)
        
        self.menu2_button = ctk.CTkButton(self.frame2, text="App", command=None,font=("Arial", 16, "bold"),  width=130, height=30)
        self.menu2_button.pack(pady=20)
        self.menu2_button.place(x=15, y=190)
        
        self.menu3_button = ctk.CTkButton(self.frame2, text="Paramètres", command=self.parametres_action,font=("Arial", 16, "bold"),  width=130, height=30)
        self.menu3_button.pack(pady=20)
        self.menu3_button.place(x=15, y=240)
        
        # Logout button
        self.logout_button = ctk.CTkButton(self.frame2, text="Logout", command=self.logout_action,font=("Arial", 16, "bold"), width=130, height=30, hover_color="red")
        self.logout_button.pack(pady=20)
        self.logout_button.place(x=15, y=420)
        
    
    def calcul_action(self):
        print("Calcul button clicked")
        api_key = 'your_api_key_here'
        openai.api_key = api_key

        # Ask a question to ChatGPT
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What is the capital of France?",
        max_tokens=100
        )

        # Print the response
        print(response.choices[0].text.strip())

    
    def home_menu_action(self):
        print("Home menu button clicked")
        if self.frame3.winfo_exists():
            self.frame3.place_forget()
            self.frame3.pack_forget()
            #self.frame3.destroy()
        
    def parametres_action(self):
        self.frame3.pack(fill="both", expand=True)
        self.frame3.place(x=160, y=0)
        self.frame3.place_configure(height="460px", width="700px")
        print("Menu1 button clicked")
        
     
    def sauvegarder_action(self):
        api_key = self.entry_api_key.get()
        self.api_key_value = api_key
        print(self.api_key_value)
         # Send the API key to Firebase
    
                    
    def logout_action(self):
        self.root.destroy()  # Close the main application window

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()