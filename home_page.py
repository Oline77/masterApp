import customtkinter as ctk
from tkinter import PhotoImage
from pathlib import Path
from PIL import Image
class MainGUI:
    def __init__(self, root):
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
        
        # Welcome text
        self.welcome_label = ctk.CTkLabel(self.frame, text="Bienvenue", font=("Arial", 24, "bold"),bg_color="#265461", text_color="#FFFFFF")
        self.welcome_label.pack(pady=20)
        self.welcome_label.place(x=10, y=0)
        # Start button
        self.start_button = ctk.CTkButton(self.frame, text="Start", command=self.start_action,font=("Arial", 16, "bold"), width=200, height=40)
        self.start_button.pack(pady=20)
        
        # Logout button
        self.logout_button = ctk.CTkButton(self.frame, text="Logout", command=self.logout_action,font=("Arial", 16, "bold"), width=130, height=30, hover_color="red", background_corner_colors=("#265461", "#265461", "#265461", "#265461"))
        self.logout_button.pack(pady=20)
        self.logout_button.place(x=10, y=420)
        
        
       
     
    def start_action(self):
        print("Start button clicked")
        
    def logout_action(self):
        self.root.destroy()  # Close the main application window

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainGUI(root)
    root.mainloop()
