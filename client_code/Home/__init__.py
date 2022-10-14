from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
	def __init__(self, **properties):
		# Set Form properties and Data Bindings.
		self.init_components(**properties)

		# Any code you write here will run when the form opens.
	def on_add_team_click(self, **event_args):
		"""This method is called when the button is clicked"""
		team_no = int(self.team_1.text)
		team_name = self.team_name.text
		print(anvil.server.call('add_team', team_no, team_name))

	def on_score_button_click(self, **event_args):
		"""This method is called when the button is clicked"""
		team_no = int(self.team_1.text)
		score = int(self.score_text_box.text)
		print(anvil.server.call('set_score', team_no, score))

	def on_easy_click(self, **event_args):
		"""This method is called when the button is clicked"""
		team_no = int(self.team_1.text)
		print(anvil.server.call('solve_easy', team_no))

	def on_hard_click(self, **event_args):
		"""This method is called when the button is clicked"""
		team_no_1 = int(self.team_1.text)
		team_no_2 = int(self.team_2.text)
		print(anvil.server.call('solve_hard', team_no_1, team_no_2))
