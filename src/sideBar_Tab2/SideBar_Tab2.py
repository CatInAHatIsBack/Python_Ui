import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

class SideBar_tab2:
    def __init__(self, master):
        self.master = master
        self.tab2_main_content_frame()
        
    def tab2_main_content_frame(self):
        self.main_content_frame = ctk.CTkFrame(self.master, corner_radius=20, bg_color="blue")
        # self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        label2 = ctk.CTkLabel(self.main_content_frame, text="Content for Tab 2")
        label2.grid(pady=20)  # Use grid within tab content

    def show(self):
        """Show Tab1 content."""
        self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    def hide(self):
        """Hide Tab1 content."""
        # print("hide tab2 content")
        self.main_content_frame.grid_remove()