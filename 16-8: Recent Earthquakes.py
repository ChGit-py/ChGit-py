import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data
filename = 'My_Data/eq_data_30_days_sig.json'
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

# Extracting Magnitudes and Location data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the Earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='significant_earthquakes_in_prev_30_days.html')
