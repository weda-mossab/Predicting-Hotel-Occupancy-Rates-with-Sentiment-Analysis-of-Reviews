import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import joblib

# Load the trained model
model = joblib.load('rd_clf.pkl')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('Hotel Booking Predictor', style={'textAlign': 'center', 'color': '#004d99', 'fontSize': '3em', 'fontFamily': 'Arial, sans-serif'}),
        html.Hr(),
    ], style={'margin': '20px'}),

    html.Div([
        # Reference Guide Section
        html.Div([
            html.H3('Reference Guide'),
            html.Pre("""
                Hotel: 'Resort Hotel' = 0, 'City Hotel' = 1
                Meal: 'BB' = 0, 'FB' = 1, 'HB' = 2, 'SC' = 3, 'Undefined' = 4
                Children: Number of children
                Babies: Number of babies
                """, style={'whiteSpace': 'pre-wrap', 'wordWrap': 'break-word', 'border': '1px solid #ccc', 'padding': '20px', 'height': '80vh', 'overflowY': 'auto'})
        ], style={'flex': 1, 'borderRight': '1px solid #ccc'}),
        html.Div([
            html.H2('Enter Hotel Booking Details', style={'color': '#004d99', 'marginBottom': '20px', 'fontSize': '2em'}),
            html.Div([
                html.Label('Hotel:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n1', type='text', placeholder='Enter hotel name', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Meal:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n2', type='text', placeholder='Enter meal preference', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Market Segment:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n3', type='text', placeholder='Enter market segment', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Distribution Channel:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n4', type='text', placeholder='Enter distribution channel', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Reserved Room Type:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n5', type='text', placeholder='Enter room type', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Deposit Type:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n6', type='text', placeholder='Enter deposit type', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Customer Type:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n7', type='text', placeholder='Enter customer type', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Year:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n8', type='text', placeholder='Enter year', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Month:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n9', type='text', placeholder='Enter month', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Day:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n10', type='text', placeholder='Enter day', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Lead Time:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n11', type='text', placeholder='Enter lead time', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Arrival Date Week Number:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n12', type='text', placeholder='Enter week number', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Arrival Date Day Of Month:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n13', type='text', placeholder='Enter day of month', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Stays In Weekend Nights:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n14', type='text', placeholder='Enter weekend nights', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Stays In Week Nights:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n15', type='text', placeholder='Enter weekday nights', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Adults:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n16', type='text', placeholder='Enter number of adults', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Children:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n17', type='text', placeholder='Enter number of children', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Babies:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n18', type='text', placeholder='Enter number of babies', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Is Repeated Guest:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n19', type='text', placeholder='Enter guest status', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Previous Cancellations:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n20', type='text', placeholder='Enter cancellations', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Previous Bookings Not Canceled:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n21', type='text', placeholder='Enter bookings', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Agent:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n22', type='text', placeholder='Enter agent name', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Company:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n23', type='text', placeholder='Enter company name', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('ADR:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n24', type='text', placeholder='Enter ADR', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Required Car Parking Spaces:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n25', type='text', placeholder='Enter parking spaces', style={'width': '100%', 'display': 'block'}),
            ]),
            html.Div([
                html.Label('Total Of Special Requests:', style={'fontWeight': 'bold'}),
                dcc.Input(id='n26', type='text', placeholder='Enter special requests count', style={'width': '100%', 'display': 'block'}),
            ]),       
            html.Button('Submit', id='submit-button', className='btn btn-primary', style={'marginBottom': '10px'}),
            html.Div(id='result-display')
        ], style={'height': '80vh', 'overflowY': 'auto', 'padding': '20px', 'border': '1px solid #dee2e6', 'borderRadius': '5px', 'backgroundColor': '#f8f9fa', 'boxShadow': '0 4px 8px rgba(0,0,0,0.1)', 'textAlign': 'center'}),
    ], style={'display': 'flex', 'height': '100vh'})
])

@app.callback(
    Output('result-display', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.State('n1', 'value'), dash.State('n2', 'value'), dash.State('n3', 'value'), dash.State('n4', 'value'),  dash.State('n5', 'value'),  
    dash.State('n6', 'value'), dash.State('n7', 'value'), dash.State('n8', 'value'),  dash.State('n9', 'value'),  dash.State('n10', 'value'), 
    dash.State('n11', 'value'), dash.State('n12', 'value'), dash.State('n13', 'value'),  dash.State('n14', 'value'),  dash.State('n15', 'value'), 
    dash.State('n16', 'value'), dash.State('n17', 'value'),  dash.State('n18', 'value'),  dash.State('n19', 'value'), dash.State('n20', 'value'), 
    dash.State('n21', 'value'), dash.State('n22', 'value'),  dash.State('n23', 'value'),  dash.State('n24', 'value'), dash.State('n25', 'value'), dash.State('n26', 'value')]  
)

def predict_booking(n, hotel, meal, market_segment, distribution_channel, reserved_room_type, deposit_type, customer_type, year, month, day, lead_time, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, agent, company, adr, required_car_parking_spaces, total_of_special_requests):
    
    prediction = model.predict([[hotel, meal, market_segment, distribution_channel, reserved_room_type, deposit_type, customer_type, year, month, day, lead_time, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, agent, company, adr, required_car_parking_spaces, total_of_special_requests]])
    
    if prediction==[1]: 
        result = 'High Occupancy Risk'
    else:
        result = 'Low Occupancy Risk'
    
    if n:
        return html.Div([
            html.H3('Prediction Result', style={'color': '#004d99'}),
            html.P(result, style={'font-weight': 'bold'})
        ], style={'text-align': 'center'})
    return None
    
if __name__ == '__main__':
    app.run_server(debug=True)