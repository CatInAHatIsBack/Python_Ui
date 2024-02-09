import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

from functionality_classes.Create_DynamicItemView import DynamicItemView

class Tab1_InterfaceDefininition:
    def __init__(self, master):
        self.master = master
        self.objectTrees = [] 
        self.createMainContentFrame()
        
    def createMainContentFrame(self):
        self.main_content_frame = ctk.CTkFrame(self.master, corner_radius=20, bg_color="gray")
        # self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    
        self.main_content_frame.grid_rowconfigure(0, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)

        objectTree = DynamicItemView(self.main_content_frame, bg_color="green")
        objectTree.get_PlacementFrame().grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        # self.objectTree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
      

    def show(self):
        """Show Tab1 content."""
        self.main_content_frame.grid(row=0, column=1, sticky="nsew")
        # self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        # for i, objectTree in enumerate(self.objectTrees):
        #             objectTree.get_PlacementFrame().grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
        

    def hide(self):
        """Hide Tab1 content."""
        self.main_content_frame.grid_remove()