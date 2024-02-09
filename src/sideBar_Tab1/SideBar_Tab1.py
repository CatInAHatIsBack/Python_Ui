import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

from functionality_classes.Tab_Switcher import TabSwitcher
from functionality_classes.topBar import TopBar
from functionality_classes.Create_DynamicItemView import DynamicItemView
from .Utility_Functions.MainContentFrame_Functions import top_bar_button1, top_bar_button2, top_bar_button3, top_bar_button4
from functionality_classes.sideBarWithTabs import SidebarWithTabs
from .SubTabs.Tab1_InterfaceDefininition import Tab1_InterfaceDefininition
from .SubTabs.Tab2_Items import Tab2_Items
from functionality_classes.Horizontal_scroller import HorizontalScrollableFrame

class SideBar_tab1:
    def __init__(self, master):
        self.master = master
        self.tab1_main_content_frame()
        
    def tab1_main_content_frame(self):
    # def create_main_content_frame(self):
        self.main_content_frame = ctk.CTkFrame(self.master, corner_radius=20, bg_color="blue")
        # self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Configure the main content frame to expand
        self.main_content_frame.grid_rowconfigure(0, weight=0)
        self.main_content_frame.grid_rowconfigure(1, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)

        # self.add_top_bar()
        topBar_Buttons = [("button 1",top_bar_button1), ("button 2",top_bar_button2), ("button 3",top_bar_button3), ("button 4",top_bar_button4)]  
        self.topBar = TopBar(self.main_content_frame, topBar_Buttons)
        # self.topBar.top_bar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        

        # Container for dynamic item view and item frame
        self.container_frame = ctk.CTkFrame(self.main_content_frame, bg_color="orange")
        self.container_frame.grid(row=1, column=0, sticky="nsew")

        # Configure the container frame for dynamic resizing
        self.container_frame.grid_columnconfigure(0,weight=0)  # Set a specific width for the Listbox container
        self.container_frame.grid_columnconfigure(1, weight=1)  # Item frame takes the rest of the space
        self.container_frame.grid_rowconfigure(0, weight=1)
        

        self.objectTree = DynamicItemView(self.container_frame, bg_color="green")
        self.objectTree.get_PlacementFrame().grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        
        
        self.tab1_TabSwitchers = None

        self.add_SelectedObjectFrame()

    def add_SelectedObjectFrame(self):
        # Item frame (to the right of the dynamic item view)
        self.selectedObjectFrame = ctk.CTkFrame(self.container_frame, bg_color="white")
        self.selectedObjectFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

       # Configure the container frame for dynamic resizing
        self.selectedObjectFrame.grid_columnconfigure(0,weight=0)  # Set a specific width for the Listbox container
        self.selectedObjectFrame.grid_columnconfigure(1, weight=1)  # Item frame takes the rest of the space
        self.selectedObjectFrame.grid_rowconfigure(0, weight=1) 

        self.create_sideBarWithTabs(self.selectedObjectFrame)

        # # Create a new frame for the HorizontalScrollableFrame
        # self.scrollable_frame_container = ctk.CTkFrame(self.selectedObjectFrame)
        # self.scrollable_frame_container.grid(row=0, column=1, sticky="nsew")  # Adjust the row and column as needed
        # self.scrollable_frame_container.grid_rowconfigure(0, weight=1)
        # self.scrollable_frame_container.grid_columnconfigure(0, weight=1)

        # # Create the CTkScrollableFrame within the new frame
        # self.scrollable_frame = ctk.CTkScrollableFrame(self.scrollable_frame_container,corner_radius=20, bg_color="purple", orientation="horizontal")
        # self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        
    def create_sideBarWithTabs(self, parent, w=1100/20):
        types_SideBar_Tab1 = ("Interface Definition", Tab1_InterfaceDefininition(parent))
        types_SideBar_Tab2 = ("Items", Tab2_Items(parent))
        tabs = [types_SideBar_Tab1, types_SideBar_Tab2]

        self.tab1_SideBar = SidebarWithTabs(parent, tabs, w)
        self.tab1_TabSwitchers = self.tab1_SideBar.getTabSwitcher()
        
        # for switcher in self.tab1_TabSwitchers:
        # self.tab1_TabSwitchers.reaffirm_active_tab()
        
    
    def getTabSwitcher(self):
        return self.tab1_TabSwitchers
    
    def show(self):
        """Show Tab1 content."""
        self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.tab1_TabSwitchers.reaffirm_active_tab()

    def hide(self):
        """Hide Tab1 content."""
        # print("hide tab1 content")
        self.main_content_frame.grid_remove()
        
    
