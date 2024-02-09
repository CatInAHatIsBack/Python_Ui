from functionality_classes.Tab_Switcher import TabSwitcher
import customtkinter as ctk

class SidebarWithTabs:
    def __init__(self, parent, tab_info, w=1100/20):
        self.parent = parent
        self.tab_info = tab_info
        self.w = w
        self.buttons = []

        self.initialize_sidebar_tabs()

    def initialize_sidebar_tabs(self):
        # Create tab instances
        tabs = {i: tab_class for i, (_, tab_class) in enumerate(self.tab_info, start=1)}
        # Initialize TabSwitcher with a dictionary of these instances
        self.tab_switcher = TabSwitcher(tabs, self.parent)

        # Initially show the first tab
        self.tab_switcher.set_current_tab(1)
        self.create_sidebar_frameXButtons()

    def create_sidebar_frameXButtons(self):
        # Create sidebar frame with widgets using grid
        self.sidebar_frame = ctk.CTkFrame(self.parent, width=self.w, corner_radius=20, bg_color="red")
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")  # Sidebar sticks to north-south
        self.sidebar_frame.grid_propagate(False)  # Prevents the frame from resizing to fit its contents

        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)       

        # Create a button for each tab
        for i, (button_name, _) in enumerate(self.tab_info, start=1):
            button = ctk.CTkButton(self.sidebar_frame, text=button_name, command=lambda i=i: self.tab_switcher.set_current_tab(i))
            button.grid(row=i-1, column=0, sticky="nsew", padx=5, pady=5)
            self.buttons.append(button)
    
    def getTabSwitcher(self):
        return self.tab_switcher