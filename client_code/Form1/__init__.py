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
        self.leaderboard_list.items = anvil.server.call('get_leaderboard')

        # Initialize timer
        self.time_left = 
    
    def timer_1_tick(self, **event_args):
        """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
        self.time_left -= 1
        self.time_remaining.text = str(timedelta(seconds=self.time_left))