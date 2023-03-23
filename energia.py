import streamlit as st


st.title('Diagnosticamos tu potencial ahorro energético')


st.slider('En kilovatios hora (Kwh): ¿cuál es tu consumo energético mensual?', 0, 100000, key="consumo")

st.slider('En millones de pesos al año: ¿cuánto inviertes en energía?', 0, 1000000, key="presupuesto")

st.radio('¿Cuál es tu fuente principal de energia?', ['Agua', 'Carbon', 'Combustible', 'Termoelectrica', 'Solar', 'Viento'], key="fuente")


    def render_basic_radar():
        option = {
                "title": {"text": "Transición energética"},
                "legend": {"data": ["Consumo Actual", "Consumo Óptimo"]},
                "radar": {
                    "indicator": [
                        {"name": "Agua", "max": 6500},
                        {"name": "Carbón", "max": 16000},
                        {"name": "Viento", "max": 30000},
                        {"name": "Sol", "max": 38000},
                        {"name": "Petróleo", "max": 52000},
                        {"name": "Gas", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Consumo Actual Vs Óptimo",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Consumo Actual",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Consumo Óptimo",
                            },
                        ],
                    }
                ],
            }
        st_echarts(option, height="500px")
    render_basic_radar()
# Data src:  https://www.kaggle.com/manohar676/hotel-reviews-segmentation-recommended-system
# Credit to: Manohar Reddy
    df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Radar-chart/ExistingHotels_CustomerVisitsdata-1554810038262.csv")
    df = df[df['Hotelid'].isin(['hotel_101','hotel_102','hotel_103'])]
    print(df.iloc[:20, :8])

    df = df.groupby('Hotelid')[['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                    'Rooms_rating','Checkin_rating',
                                    'Businessservice_rating']].mean().reset_index()
    print(df)

# Convert from wide data to long data to plot radar chart
    df = pd.melt(df, id_vars=['Hotelid'], var_name='category', value_name='rating',
                     value_vars=['Cleanliness_rating', 'Service_rating', 'Value_rating',
                                 'Rooms_rating','Checkin_rating','Businessservice_rating'],
        )
    print(df)

# radar chart Plotly examples - https://plotly.com/python/radar-chart/
# radar chart Plotly docs = https://plotly.com/python-api-reference/generated/plotly.express.line_polar.html#plotly.express.line_polar
    fig = px.line_polar(df, r='rating', theta='category', color='Hotelid', line_close=True,
                                    line_shape='linear',  # or spline
                            hover_name='Hotelid',
                            hover_data={'Hotelid':False},
                            markers=True,
                            # labels={'rating':'stars'},
                            # text='Hotelid',
                            # range_r=[0,10],
                            direction='clockwise',  # or counterclockwise
                            start_angle=45
                            )
        # fig.update_traces(fill='toself')
    fig.show()
    
