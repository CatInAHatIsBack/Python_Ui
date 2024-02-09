
class TabSwitcher:
    def __init__(self, tabs, parent):
        """
        Initializes the TabSwitcher with a dictionary of tabs.

        Args:
            tabs (dict): A dictionary where keys are tab identifiers (integers or strings)
                         and values are tab instances that have show() and hide() methods.
        """
        self.parent = parent
        self.tabs = tabs  # {tab_identifier: tab_instance}
        self.current_tab = None  # Track the current visible tab

    
    def set_current_tab(self, tab_identifier):

        self.current_tab = tab_identifier
        self.reaffirm_active_tab()
    
    def reaffirm_active_tab(self):
        
        for identifier, tab in self.tabs.items():
            tab.hide()

        # Then, show the currently active tab if there is one
        if self.current_tab is not None:
            self.tabs[self.current_tab].show()
        self.parent.update_idletasks()
        self.parent.update()
        