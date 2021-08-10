import csv

from plotly.graph_objs import Bar,Layout
from plotly import offline
import pandas as pd
import numpy as np

filename = 'Data/premier_league_team_stats1819.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get team names and wins
    team_names, wins = [], []
    for row in reader:
        team_name = row[0]
        team_names.append(team_name)
        total_wins = row[8]
        wins.append(total_wins)

# Plot the team names and their total wins
data = ([Bar(x=team_names, y=wins)])

x_axis_config = {'title': 'Team', 'dtick': 1}
y_axis_config = {'title': 'Total wins'}
my_layout = Layout(title='Premier League teams and their total wins - 2018/19')

offline.plot({'data': data, 'layout': my_layout}, filename='Premier_League_wins_1819.html')