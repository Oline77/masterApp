from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\victor\Desktop\Test\myAppLogin\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("703x462")
        self.root.configure(bg="#FFFFFF")
        self.root.title("Main Application")

        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=462,
            width=703,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            703.0,
            462.0,
            fill="#EFEFEF",
            outline=""
        )
        self.canvas.create_text(
            63.0,
            18.0,
            anchor="nw",
            text="Welcome",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=581.0, y=30.0, width=84.0, height=38.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=123.0, y=169.0, width=84.0, height=38.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=123.0, y=262.0, width=84.0, height=38.0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            452.0,
            231.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            32.0,
            36.0,
            image=self.image_image_2
        )

        self.root.resizable(False, False)
