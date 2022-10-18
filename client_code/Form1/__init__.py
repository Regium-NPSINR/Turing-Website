from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta

class Form1(Form1Template):
	def __init__(self, **properties):
		# Set Form properties and Data Bindings.
		self.init_components(**properties)

		# Any code you write here will run when the form opens.
		self.leaderboard_list.items = anvil.server.call('get_leaderboard')

		# Initialize timer
		self.end_time = datetime(2022, 10, 18, 13, 55)

	def timer_1_tick(self, **event_args):
		"""This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
		self.time_remaining.text = datetime.fromtimestamp((self.end_time - datetime.now()).total_seconds() - 19800).strftime("%M:%S" if (self.end_time - datetime.now()).total_seconds() < 3600 else "%H:%M")
    

	def on_refresh_leaderboard(self, **event_args):
		"""This method is called when the refresh_leaderboard button is called"""
		self.update_leaderboard()
	
	def update_leaderboard(self):
		"""This method updates the leaderboard"""
		self.leaderboard_list.items = anvil.server.call('get_leaderboard')
		self.refresh_data_bindings()

	def leaderboard_refresh_timer_tick(self, **event_args):
		"""This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
		self.update_leaderboard()

