import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk   

class AppMenu:
    def __init__(self, master, appearance_callback, scaling_callback):
        self.master = master
        self.appearance_callback = appearance_callback
        self.scaling_callback = scaling_callback
        self.add_menu_items()
        
    def add_menu_items(self):
        # Create a menu bar
        menu_bar = tk.Menu(self.master)

        # Create the appearance mode menu
        appearance_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Appearance Mode", menu=appearance_menu)
        appearance_menu.add_command(label="Light", command=lambda: self.appearance_callback("light"))
        appearance_menu.add_command(label="Dark", command=lambda: self.appearance_callback("dark"))
        appearance_menu.add_command(label="System", command=lambda: self.appearance_callback("system"))

        # Create the UI scaling menu
        scaling_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="UI Scaling", menu=scaling_menu)
        scaling_factors = ["70%", "80%", "90%", "100%", "110%", "120%", "130%", "140%", "150%"]
        for factor in scaling_factors:
            scaling_menu.add_command(label=factor, command=lambda factor=factor: self.scaling_callback(factor))

        redraw = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="redraw", menu=redraw)
        redraw.add_command(label="Light", command=lambda: self.master.update)
        # Set the menu bar as the application's menu
        self.master.config(menu=menu_bar)
