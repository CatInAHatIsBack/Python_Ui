import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar
import customtkinter as ctk

class HorizontalScrollableFrame:
    def __init__(self, parent):
        self.parent = parent

        

    def get_frame(self):
        return self.frame