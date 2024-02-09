import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

class DynamicItemView:
    def __init__(self, parent, bg_color="green"):
        self.parent = parent
        # self.add_item_callback = add_item_callback
        self.bg_color = bg_color

        self.create_dynamic_item_view()

    def create_dynamic_item_view(self):
        # Dynamic item view frame
        self.item_view_frame = ctk.CTkFrame(self.parent, bg_color=self.bg_color)
        self.item_view_frame.grid_rowconfigure(0, weight=1)  
        self.item_view_frame.grid_rowconfigure(1, weight=0)  
        self.item_view_frame.grid_columnconfigure(0, weight=1)

        self.create_scrollable_item_view(self.item_view_frame)

        # self.item_view_frame.bind("<Configure>", self.redraw_widgets)
        
        # Frame for Add and Remove buttons
        self.button_frame = ctk.CTkFrame(self.item_view_frame, bg_color="lightgrey")
        self.button_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.btn_add = ctk.CTkButton(self.button_frame, text="Add Item", command=self.add_item)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    def create_scrollable_item_view(self, parent):
        # Adjust the width as needed
        self.scrollable_frame = ctk.CTkScrollableFrame(parent, corner_radius=10)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.populate_scrollable_frame()
    


    def update_selected_item(self, item_name):
        print("update_selected_item", item_name)
        # Directly update the label text with the passed item name

        # self.selected_item_label.configure(text=item_name)

        # Optionally update the label's text color to indicate selection

        # self.selected_item_label.configure(text_color="white")  # Example color for selected item text
        
    def remove_selected_item(self, item_frame):
        # Function to remove the selected item from the Listbox
        item_frame.destroy()

    def add_item(self):
        # Function to add an item to the Listbox
        item = simpledialog.askstring("Item", "Enter item name:")
        if item:  # Ensure the user entered something
            self.add_item_to_scrollable_frame(item)


    def populate_scrollable_frame(self):
        for i in range(20):  # Example starting number of items
            self.add_item_to_scrollable_frame(f"Item {i}")

    def add_item_to_scrollable_frame(self, item_name):
        h = 30
        w = 30
        item_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10)
        item_frame.grid(sticky="ew", padx=5, pady=2)
        # item_frame.grid_columnconfigure(1, weight=1) 
        item_frame.grid_columnconfigure(0, minsize=30)  # Reserve space for the "X" button
        item_frame.grid_columnconfigure(1, weight=1)  

        # "X" button for removing the item
        remove_button = ctk.CTkButton(item_frame, text="X", fg_color="red", width=w, height=h,
                                    command=lambda: self.remove_selected_item(item_frame))
        remove_button.grid(row=0, column=0, sticky="nsew", padx=(0, 10))  # Ensure "X" button is small and aligned to the left

        # Item button, placed next to the "X" button and allowed to expand
        item_button = ctk.CTkButton(item_frame, text=item_name, height=h,
                                    command=lambda: self.update_selected_item(item_name))
        item_button.grid(row=0, column=1, sticky="nsew")  # Expands to fill available space


    def get_PlacementFrame(self):
        return self.item_view_frame
    
    # def redraw_widgets(self, event):
    #     # This function is called when the window is resized
    #     for widget in self.item_view_frame.winfo_children():
    #         widget.update()