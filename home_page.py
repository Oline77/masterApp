import customtkinter as ctk
from tkinter import PhotoImage
from pathlib import Path
from PIL import Image, ImageTk
from openai import OpenAI
import firebase_admin
from firebase_admin import credentials, firestore
from script.generateFacture import generate_invoice
import tkintermapview


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
        self.root.title("Cyber Garde Admin Panel")
        self.root.iconbitmap("images/earth.ico")

        self.todo_list = []
         
        self.create_widgets()

    def create_widgets(self):
        # Frame to hold the content
        self.frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="#FFFFFF")
        self.frame.pack(fill="both", expand=True)
        
        self.explication_label = ctk.CTkLabel(self.frame, text="Bienvenue sur votre application d'administration", font=("Arial", 16, "bold"), text_color="black")
        self.explication_label.pack(pady=20)
        self.explication_label.place(x=200, y=10)
        
        self.home_label = ctk.CTkLabel(self.frame, text="Cette application va vous permettre de gérer simplement \nvos votre entreprise",font=("Arial", 13), text_color="black")
        self.home_label.pack(pady=20)
        self.home_label.place(x=220, y=50)
        
        # Image
        self.home_image = Image.open("images/iconPDF.png")
        self.home_image = ImageTk.PhotoImage(self.home_image)
        
        # Frame menu
        self.frame2 = ctk.CTkFrame(master=self.frame, width=200, height=200, corner_radius=0, fg_color="#265461")
        self.frame2.pack(side="left", fill="both", expand=True)
        self.frame2.place(x=0, y=0)
        self.frame2.place_configure(height="700px", width="150px")
        
        # Frame menu 1
        self.frame3 = ctk.CTkFrame(master=self.frame, width=50, height=50, corner_radius=0, fg_color="#FFFFFF")
       
        self.frame4App = ctk.CTkFrame(master=self.frame, width=50, height=50, corner_radius=0, fg_color="#FFFFFF")
        
        # Welcome text
        self.welcome_label = ctk.CTkLabel(self.frame, text="Bienvenue", font=("Arial", 24, "bold"), bg_color="#265461", text_color="#FFFFFF")
        self.welcome_label.pack(pady=20)
        self.welcome_label.place(x=15, y=5)
        
        # Frame 3 component
        self.start_button = ctk.CTkButton(self.frame3, text="Sauvegarder", command=self.sauvegarder_action, font=("Arial", 16, "bold"), width=130, height=30, hover_color="green")
        self.start_button.pack(pady=20)
        self.start_button.place(x=370, y=400)  
        
        self.label_texte = ctk.CTkLabel(self.frame3, text="Paramètres", text_color="black", font=("Arial", 24, "bold"))
        self.label_texte.pack(pady=20)
        self.label_texte.place(x=200, y=10)
        
        self.label_texte_api = ctk.CTkLabel(self.frame3, text="API Key ChatGPT :", text_color="black", font=("Arial", 14))
        self.label_texte_api.pack(pady=20)
        self.label_texte_api.place(x=150, y=70)
        self.entry_api_key = ctk.CTkEntry(self.frame3, placeholder_text="api key", width=130, height=30)
        self.entry_api_key.pack(pady=20)
        self.entry_api_key.place(x=280, y=70)
        
        # Frame 4 App component
        self.start_button = ctk.CTkButton(self.frame4App, text="ChatGPT", command=self.send_prompt_action, font=("Arial", 16, "bold"), width=130, height=30, hover_color="green")
        self.start_button.pack(pady=20)
        self.start_button.place(x=370, y=400)
        
        self.button_carre1 = ctk.CTkButton(self.frame4App, text="Génerer \nfacture", command=None, font=("Arial", 16, "bold"), width=130, height=30, hover_color="white", corner_radius=15, fg_color="#BBE9FF", text_color="black")
        self.button_carre1.pack(pady=20)
        self.button_carre1.place(x=30, y=30)
        self.button_carre1.place_configure(height="130px", width="130px")
        
        self.button_carre2 = ctk.CTkButton(self.frame4App, text="Gérer \nclients", command=None, font=("Arial", 16, "bold"), width=130, height=30, hover_color="white", corner_radius=15, fg_color="#BBE9FF", text_color="black")
        self.button_carre2.pack(pady=20)
        self.button_carre2.place(x=190, y=30)
        self.button_carre2.place_configure(height="130px", width="130px")
        
        self.button_carre3 = ctk.CTkButton(self.frame4App, text="Todo \nlist", command=self.todo_list_action, font=("Arial", 16, "bold"), width=130, height=30, hover_color="white", corner_radius=15, fg_color="#BBE9FF", text_color="black")
        self.button_carre3.pack(pady=20)
        self.button_carre3.place(x=350, y=30)
        self.button_carre3.place_configure(height="130px", width="130px")
        
        self.button_carre4 = ctk.CTkButton(self.frame4App, text="Localisation \nchantier", command=self.localisation_chantier_action, font=("Arial", 16, "bold"), width=130, height=30, hover_color="white", corner_radius=15, fg_color="#BBE9FF", text_color="black")
        self.button_carre4.pack(pady=20)
        self.button_carre4.place(x=30, y=190)
        self.button_carre4.place_configure(height="130px", width="130px")
        
        # Frame for to-do list
        self.todo_frame = ctk.CTkFrame(master=self.frame, width=50, height=50, corner_radius=0, fg_color="#FFFFFF")
        
        # Frame for chantier
        self.chantier_frame = ctk.CTkFrame(master=self.frame, width=50, height=50, corner_radius=0, fg_color="#FFFFFF")
        
        # Menu button
        self.home_button = ctk.CTkButton(self.frame2, text="Acceuil", command=self.home_menu_action, font=("Arial", 16, "bold"),  width=130, height=30)
        self.home_button.pack(pady=20)
        self.home_button.place(x=15, y=140)
        
        self.menu2_button = ctk.CTkButton(self.frame2, text="App", command=self.app_menu_action, font=("Arial", 16, "bold"),  width=130, height=30)
        self.menu2_button.pack(pady=20)
        self.menu2_button.place(x=15, y=190)
        
        self.menu3_button = ctk.CTkButton(self.frame2, text="Paramètres", command=self.parametres_action, font=("Arial", 16, "bold"),  width=130, height=30)
        self.menu3_button.pack(pady=20)
        self.menu3_button.place(x=15, y=240)
        
        # Logout button
        self.logout_button = ctk.CTkButton(self.frame2, text="Logout", command=self.logout_action, font=("Arial", 16, "bold"), width=130, height=30, hover_color="red")
        self.logout_button.pack(pady=20)
        self.logout_button.place(x=15, y=420)
    
    def send_prompt_action(self):
        #api_key = 'your_api_key_here'
        #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
        # Récupérer l'API key depuis Firebase
        doc_ref = self.db.collection('api_keys').document('api_keys')
        doc = doc_ref.get()
        api_key_user = doc.get('api_key')
        client = OpenAI(
        # This is the default and can be omitted
            api_key=api_key_user
            )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="babbage-002",
        )


    def app_menu_action(self):
        if self.frame3.winfo_exists():
            self.frame3.place_forget()
            self.frame3.pack_forget()
        
        self.frame4App.pack(fill="both", expand=True)
        self.frame4App.place(x=160, y=0)
        self.frame4App.place_configure(height="460px", width="700px")
        
            #self.frame3.destroy()
    def home_menu_action(self):
        if self.frame3.winfo_exists():
            self.frame3.place_forget()
            self.frame3.pack_forget()
            #self.frame3.destroy()
        if self.frame4App.winfo_exists():
            self.frame4App.place_forget()
            self.frame4App.pack_forget()
        
    def parametres_action(self):
        if self.frame4App.winfo_exists():
            self.frame4App.place_forget()
            self.frame4App.pack_forget()
            
        self.frame3.pack(fill="both", expand=True)
        self.frame3.place(x=160, y=0)
        self.frame3.place_configure(height="460px", width="700px")
        
        
    def sauvegarder_action(self):
        api_key = self.entry_api_key.get()
        self.api_key_value = api_key
         # Send the API key to Firebase
        doc_ref = self.db.collection('api_keys').document('api_keys')
        doc_ref.set({'api_key': api_key})
        
    def logout_action(self):
        self.root.destroy()  # Close the main application window
    
    def get_chantier_entry_value(self,event):
        adresse = self.chantier_entry.get()
        self.map_widget.set_address(adresse)
        
    def localisation_chantier_action(self):
         # Hide other frames
        if self.frame3.winfo_exists():
            self.frame3.place_forget()
            self.frame3.pack_forget()
        if self.frame4App.winfo_exists():
            self.frame4App.place_forget()
            self.frame4App.pack_forget()
        
        # Show chantier_frame
        self.chantier_frame.pack(fill="both", expand=True)
        self.chantier_frame.place(x=160, y=0)
        self.chantier_frame.place_configure(height="460px", width="700px")
        
        self.chantier_label = ctk.CTkLabel(self.chantier_frame, text="Vos chantiers en cours", font=("Arial", 24, "bold"), text_color="black")
        self.chantier_label.pack(pady=20)
        self.chantier_label.place_configure(x=170, y=10)
        
        self.chantier_entry = ctk.CTkEntry(self.chantier_frame, placeholder_text="Entrer une adresse", width=300, height=30)
        self.chantier_entry.pack(pady=20)
        self.chantier_entry.place(x=110, y=45)
        
        # Bind the Return key to a function to get the value of todo_entry
        self.chantier_entry.bind("<Return>", self.get_chantier_entry_value)
        
        # create map widget
        self.map_widget = tkintermapview.TkinterMapView(self.chantier_frame, width=600, height=450, corner_radius=15)
        self.map_widget.place(x=40, y=100)
        # set current widget position and zoom
        self.map_widget.set_position(45.750000, 4.850000)  # Lyon, France
        self.map_widget.set_zoom(13)
        def add_marker_event(coords):
            print("Add marker:", coords)
            new_marker = self.map_widget.set_marker(coords[0], coords[1], text="Chantier")
            

        self.map_widget.add_right_click_menu_command(label="Ajouter un chantier",
                                                command=add_marker_event,
                                                pass_coords=True)
        
         # Add a button to close the frame
        self.close_todo_button = ctk.CTkButton(self.chantier_frame, text="x", command=self.close_chantier_frame, font=("Arial", 16, "bold"), width=13, height=13, fg_color="red", corner_radius=100)
        self.close_todo_button.pack(pady=20)
        self.close_todo_button.place(x=515, y=430)
        
    def todo_list_action(self):
        # Hide other frames
        if self.frame3.winfo_exists():
            self.frame3.place_forget()
            self.frame3.pack_forget()
        if self.frame4App.winfo_exists():
            self.frame4App.place_forget()
            self.frame4App.pack_forget()
        
        # Show todo_frame
        self.todo_frame.pack(fill="both", expand=True)
        self.todo_frame.place(x=160, y=0)
        self.todo_frame.place_configure(height="460px", width="700px")
        
        # Add a label and entry for the to-do list
        self.todo_label = ctk.CTkLabel(self.todo_frame, text="To-Do List", font=("Arial", 24, "bold"), text_color="black")
        self.todo_label.pack(pady=20)
        self.todo_label.place(x=170, y=10)
        
        self.todo_entry = ctk.CTkEntry(self.todo_frame, placeholder_text="Entrer une tâche", width=300, height=30)
        self.todo_entry.pack(pady=20)
        self.todo_entry.place(x=110, y=70)
        
        # Bind the Return key to a function to get the value of todo_entry
        self.todo_entry.bind("<Return>", self.get_todo_entry_value)
        
        # Create a frame to hold the list of tasks
        self.todo_list_frame = ctk.CTkFrame(self.todo_frame, width=600, height=300, fg_color="#FFFFFF")
        self.todo_list_frame.pack(pady=20)
        self.todo_list_frame.place(x=50, y=120)
        
        # Load existing tasks
        for item in self.todo_list:
            self.create_task_frame(item)
            
        # Add a button to close the frame
        self.close_todo_button = ctk.CTkButton(self.todo_frame, text="Close", command=self.close_todo_frame, font=("Arial", 16, "bold"), width=90, height=30)
        self.close_todo_button.pack(pady=20)
        self.close_todo_button.place(x=400, y=400)
        
    def get_todo_entry_value(self, event):
        task = self.todo_entry.get()
        if task:
            self.add_task(task)
            self.todo_entry.delete(0, 'end')
    
    def add_task(self, task):
        new_task = {"task": task, "done": False}
        self.todo_list.append(new_task)
        self.create_task_frame(new_task)
    
    def create_task_frame(self, item):
        task_frame = ctk.CTkFrame(self.todo_list_frame, fg_color="#E0E0E0", height=40)
        task_frame.pack(fill="x", pady=2)

        task_label = ctk.CTkLabel(task_frame, text=item["task"], font=("Arial", 14), text_color="gray" if item["done"] else "black", width=270)
        task_label.pack(side="left", padx=10)

        done_button = ctk.CTkButton(task_frame, text="Done", command=lambda lbl=task_label, t=item["task"]: self.mark_task_done(lbl, t), font=("Arial", 12, "bold"), width=50, height=30)
        done_button.pack(side="right", padx=5)

        delete_button = ctk.CTkButton(task_frame, text="Delete", command=lambda frm=task_frame, t=item["task"]: self.delete_task(frm, t), font=("Arial", 12, "bold"), width=50, height=30)
        delete_button.pack(side="right", padx=5)
    
    def mark_task_done(self, task_label, task):
        task_label.configure(text_color="gray")
        for item in self.todo_list:
            if item["task"] == task:
                item["done"] = True
                break
    
    def delete_task(self, task_frame, task):
        task_frame.destroy()
        self.todo_list = [item for item in self.todo_list if item["task"] != task]
    
    def close_todo_frame(self):
        self.todo_frame.place_forget()
        self.todo_frame.pack_forget()
        
        self.todo_list_frame.place_forget()
        self.todo_list_frame.pack_forget()
        
        self.frame4App.pack(fill="both", expand=True)
        self.frame4App.place(x=160, y=0)
        self.frame4App.place_configure(height="460px", width="700px")
        
    def close_chantier_frame(self):
        self.chantier_frame.place_forget()
        self.chantier_frame.pack_forget()
        
        self.frame4App.pack(fill="both", expand=True)
        self.frame4App.place(x=160, y=0)
        self.frame4App.place_configure(height="460px", width="700px")

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()
