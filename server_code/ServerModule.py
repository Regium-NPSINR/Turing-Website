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
def add_team(team_no, team_name):
	if app_tables.leaderboard.search(team_no = team_no):
		return False
	
	if app_tables.leaderboard.search(team_name = team_name):
		return False

	app_tables.leaderboard.add_row(
		team_no = team_no, 
		team_name = 'Test Team',
		team_score = 0
	)
	return True


@anvil.server.callable
def set_score(team_no, score):
	# set team's score to new score
	if not app_tables.leaderboard.search(team_no = team_no):
		return False
	
	# Team already exists
	app_tables.leaderboard.get(team_no = team_no)[score] = score
	return True

@anvil.server.callable
def solve_easy(team_no):
	# set team's score to new score
	if not app_tables.leaderboard.search(team_no = team_no):
		return False

	# Team already exists
	app_tables.leaderboard.get(team_no = team_no)[score] += 1
	return True

@anvil.server.callable
def solve_hard(team_no_1, team_no_2):
	# check if the teams exist
	if ((not app_tables.leaderboard.search(team_no_1 = team_no_1)) or
		not app_tables.leaderboard.search(team_no_2 = team_no_2)):
		return False

	# Team already exists
	app_tables.leaderboard.get(team_no_1 = team_no_1)[score] += 1
	app_tables.leaderboard.get(team_no_2 = team_no_2)[score] += 1
	return True
