import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Crear la aplicación de Dash
app = dash.Dash(__name__)

# Datos de ejemplo
data = {
    'locations': ['Lima', 'Cusco', 'Arequipa'],
    'latitudes': [-12.0464, -13.5319, -16.4090],
    'longitudes': [-77.0428, -71.9675, -71.5375],
}

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Gráfico Scattergeo básico"),
    dcc.Graph(id='scattergeo-plot'),
])

# Callback para actualizar el gráfico
@app.callback(
    Output('scattergeo-plot', 'figure'),
    Input('scattergeo-plot', 'id')
)
def update_graph(_):
    fig = go.Figure(go.Scattergeo(
        locationmode = 'ISO-3',  # Modo de localización de país (opcional)
        lon = data['longitudes'],  # Longitudes
        lat = data['latitudes'],  # Latitudes
        text = data['locations'],  # Nombres o etiquetas de las ubicaciones
        mode = 'markers',  # Modo de visualización de puntos
        marker=dict(
            size=10,  # Tamaño de los marcadores
            color='blue',  # Color de los marcadores
            line=dict(width=1, color='darkblue')  # Borde de los marcadores
        )
    ))

    # Configuración del diseño del mapa
    fig.update_layout(
        title="Ubicaciones en Perú",
        geo=dict(
            scope='south america',  # Limitar el alcance del mapa
            projection_type='natural earth',  # Tipo de proyección
            showland=True,
            landcolor='lightgrey'
        )
    )
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)