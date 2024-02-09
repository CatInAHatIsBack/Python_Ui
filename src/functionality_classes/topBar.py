import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk


class TopBar:
    def __init__(self, master, button_commands, height=50, bg_color="grey"):
        self.master = master
        self.button_commands = button_commands
        self.height = height
        self.bg_color = bg_color
        self.create_top_bar()

    def create_top_bar(self):
        self.top_bar = ctk.CTkFrame(self.master, height=self.height, bg_color=self.bg_color)
        self.top_bar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.top_bar.grid_propagate(True)

        for i, (btn_text, btn_command) in enumerate(self.button_commands):
            self.top_bar.grid_columnconfigure(i, weight=1)
            button = ctk.CTkButton(self.top_bar, text=btn_text, command=btn_command)
            button.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)