
import tkinter as tk
from tkinter import ttk, simpledialog
import customtkinter as ctk

from sideBar_Tab1.SideBar_Tab1 import SideBar_tab1
from sideBar_Tab2.SideBar_Tab2 import SideBar_tab2
from functionality_classes.app_menu import AppMenu
from functionality_classes.Tab_Switcher import TabSwitcher
from functionality_classes.sideBarWithTabs import SidebarWithTabs

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        w, h = 1100, 580
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{w}x{h}")
        self.resizable(True, True)
        setScale = "70%"
        sidebar_w = w//20


        self.configure_grid()

        self.tabSwitchers = [] 
        self.create_sideBarWithTabs(self, sidebar_w)
        
        # print(self.tabSwitchers)
        
        # self.sideBar.buttons[0].bind("<Enter>", self.print_enter_event)
        self.change_scaling_event(setScale)
        AppMenu(self, self.change_appearance_mode, self.change_scaling_event)

    def create_sideBarWithTabs(self, parent, w=1100/20):
        tab1 = SideBar_tab1(parent)
        tab2 = SideBar_tab2(parent)
        sideBar_tab1 = ("Tab1", tab1)
        sideBar_tab2 = ("TabX", tab2)
        self.tabs = [sideBar_tab1, sideBar_tab2]
    
        
        self.sideBar = SidebarWithTabs(parent, self.tabs, w)
        self.tabSwitchers.append(self.sideBar.getTabSwitcher())
        # self.tabSwitchers.append(tab1.getTabSwitcher())
        
        
        
    def configure_grid(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

        for switcher in self.tabSwitchers:
            switcher.reaffirm_active_tab()

        self.update_idletasks()
        self.update()
    #     self.delayed_redraw()
        
    # def delayed_redraw(self):
    #     self.after(1000, self.update)


        

# from src.SideBar_Tab1.test.test import te
if __name__ == "__main__":
    # te()
    app = App()
    app.mainloop()
