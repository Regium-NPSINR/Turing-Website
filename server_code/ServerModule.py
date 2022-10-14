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
	# check if the team exists
	if app_tables.leaderboard.get(team_no = team_no) != None:
		return False
	
	if app_tables.leaderboard.get(team_name = team_name) != None:
		return False

	app_tables.leaderboard.add_row(
		team_no = team_no, 
		team_name = team_name,
		team_score = 0
	)
	return True

@anvil.server.callable
def set_score(team_no, score):
	# check if the team exists
	if app_tables.leaderboard.get(team_no = team_no) == None:
		return False
	
	# Team already exists
	app_tables.leaderboard.get(team_no = team_no)['team_score'] = score
	return True

@anvil.server.callable
def solve_easy(team_no):
	# check if the team exists
	if app_tables.leaderboard.get(team_no = team_no) == None:
		return False

	# Team already exists
	print(app_tables.leaderboard.get(team_no = team_no))
	print(dict(app_tables.leaderboard.get(team_no = team_no)))
	app_tables.leaderboard.get(team_no = team_no)['team_score'] += 1
	return True

@anvil.server.callable
def solve_hard(team_no_1, team_no_2):
	# check if the teams exist
	if ((app_tables.leaderboard.get(team_no = team_no_1) == None) or
		(app_tables.leaderboard.get(team_no = team_no_2) == None)):
		return False

	# Teams already exists
	app_tables.leaderboard.get(team_no = team_no_1)['team_score'] += 1
	app_tables.leaderboard.get(team_no = team_no_2)['team_score'] -= 1
	return True

@anvil.server.callable
def get_score(team_no):
	# check if the team exists
	if app_tables.leaderboard.get(team_no = team_no) == None:
		return False

	# Team exists
	return app_tables.leaderboard.get(team_no = team_no)['team_score']

@anvil.server.callable
def get_leaderboard():
	return app_tables.leaderboard.search()
