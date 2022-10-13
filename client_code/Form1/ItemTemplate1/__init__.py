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

	def on_score_button_click(self, **event_args):
		"""This method is called when the button is clicked"""
		team_no = 0
		score = int(self.score_text_box.text)
		for i in anvil.server.call('set_play_score', team_no, score):
			alert(f'Team no.: {i[0]}\nTeam name: {i[1]}\nScore: {i[2]}')
