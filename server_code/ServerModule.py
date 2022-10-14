import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#


@anvil.server.callable
def set_play_score(team_no, score):
	# set team's score to new score
<<<<<<< HEAD
	print(team_no, team_name, score)
	app_tables.leaderboard.add_row(team_no, 'Test Team', score)
=======
	print(team_no, score)
	app_tables.leaderboard.add_row(
        team_no = team_no, 
        team_name = 'Test Team',
        team_score = score
    )
>>>>>>> ef4436205be77c76caf3a558b6ecbd06575b5efe
	return app_tables.leaderboard.search()
