import plotly.express as px

# NOTE: from core
# import sys
# sys.path.append('../core')
# import db_api

data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='lifeExp')
fig.show()

count = [9607, 4851, 3318, 2290, 1770, 1341, 1030, 918, 778, 640]
price_groups = ['$1', '$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9', '$10']
fig = px.bar(x=price_groups, y=count)
fig.update_xaxes(showgrid=True, ticks="outside")
fig.update_xaxes(type='category')
fig.show()