from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import timedelta

class Form1(Form1Template):
    
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
    
        # Any code you write here will run when the form opens.
        self.time_left = 648000
    
    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self.time_left -= 1
        self.time_remaining.text = str(time)
    
    def timer_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.timer_button.text == "Start Timer":
            self.timer_1.interval = 1
            self.timer_button.text == "Pause Timer"
        elif self.timer_button.text == "Pause Timer":
            self.timer_1.interval = 0
            self.timer_button.text = "Start Timer"
          


