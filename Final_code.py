import pandas as pd

pie_df=pd.read_csv('pie_df.csv')
bar_df=pd.read_csv('bar_df.csv')
stacked_df=pd.read_csv('stacked_df.csv')
pie1=pd.read_csv('pie1.csv')


import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


app = dash.Dash(__name__)



pie_chart = px.pie(pie_df, values='count', names='race', hole=0.6, template='plotly_dark', title='Races by percentage')
bar_chart=px.bar(bar_df, x='education', y='count', template='plotly_dark', title='education type by number')
stacked_bar= px.bar(stacked_df, x="education", y=[">50K", "<50K"], title="salary comparison (Advanced , Non-Advanced education)", template='plotly_dark')

app.layout = html.Div([
    dbc.Row([
		dbc.Col(html.H3('demographic data visualization'),
			xs=10, sm=10, md=10, lg=11, xl=11,
			className='header'),

            
        dbc.Col(html.Img(src=app.get_asset_url('image1.png'), height=50,), 
			xs=2, sm=2, md=2, lg=1, xl=1,
			className='theimage' )
    ]),

    dbc.Row([
		dbc.Col([
			html.Div(
				[
					html.Div(
						[
							html.H4("Race counts", className=('title')),
							html.P('white : 25926', className=('textA')),
							html.P('Black : 2815', className=('textA')),
							html.P('Asian : 894', className=('textA')),
							html.P('Indian : 286', className=('textA'))
						],
						className = "card_container "
					),
		])
    	],
		xs=6, sm=6, md=6, lg=3, xl=3,
		),

		dbc.Col([
			html.Div(
				[
					html.Div(
						[
							html.H4("Average age of men", className=('title')),
							html.P('38 Years', className=('text')),
							
						],
						className = "card_container "
					),
		])
		],
		xs=6, sm=6, md=6, lg=3, xl=3,
		),

		dbc.Col([
			html.Div(
				[
					html.Div(
						[
							html.H4("Percentage of people with Bachelors degree", className=('title')),
							html.P('16.8%', className=('text')),
							
						],
						className = "card_container "
					),
		])
		],
		xs=12, sm=12, md=12, lg=6, xl=6,
		),
	]),

	dbc.Row([
		dbc.Col(
			dcc.Graph(figure=pie_chart),
			# width={'size':6, 'offset':0},
			xs=12, sm=12, md=12, lg=6, xl=6,
			className='graph'
	 	),

		 dbc.Col(
			dcc.Graph(figure=bar_chart),
			# width={'size':6, 'offset':0},
			xs=12, sm=12, md=12, lg=6, xl=6,
			className='graph1'
	 	),
	]),
	dbc.Row([
		dbc.Col([
			html.Div([
			html.P("Salary comparison according to education type", className='p'),
    		dcc.Dropdown(
			id='names', 
			value='advanced education salary', 
			options=[{'value': x, 'label': x} 
					for x in ['advanced education salary', 'non advanced education salary']],
			clearable=False, className='dropdown',
			),
			],id='dropdowncol')
		],xs=12, sm=12, md=12, lg=6, xl=6,
		),
	]),
	dbc.Row([
		dbc.Col(
			dcc.Graph(id="pie-chart",className='tgraph'), 
			xs=12, sm=12, md=12, lg=6, xl=6,
			className='graph2'
		),

		dbc.Col(
			dcc.Graph(figure=stacked_bar), 
			xs=12, sm=12, md=12, lg=6, xl=6,
			className='graph2'
		)
	])
], className='app')

@app.callback(
   Output("pie-chart", "figure"), 
   [Input("names", "value"),] 
   )
def generate_chart(names):
   df = pie1
   fig = px.pie(df, names=names, template='plotly_dark',title='salary by percentage')

   return fig

if __name__ == "__main__":
   app.run_server(host='0.0.0.0', port=8050, debug=False)



