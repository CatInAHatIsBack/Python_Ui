import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

from functionality_classes.Create_DynamicItemView import DynamicItemView

class Tab2_Items:
    def __init__(self, master):
        self.master = master
        self.createMainContentFrame()
        
    def createMainContentFrame(self):
        self.main_content_frame = ctk.CTkFrame(self.master, corner_radius=20, bg_color="blue")
        # self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_content_frame.grid_rowconfigure(0, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_content_frame,corner_radius=20, bg_color="red", orientation="horizontal")
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")

        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        for i in range(5):
            objectTree = DynamicItemView(self.scrollable_frame, bg_color="green")
            objectTree.get_PlacementFrame().grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
            # self.objectTrees.append(objectTree)  # Add this line

    def show(self):
        """Show Tab1 content."""
        self.main_content_frame.grid(row=0, column=1, sticky="nsew")

    def hide(self):
        """Hide Tab1 content."""
        # print("hide tab2 content")
        self.main_content_frame.grid_remove()