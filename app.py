from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

# Ruta principal con un menú
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el gráfico
@app.route('/chart')
def chart():
    # Crear datos de ejemplo para la gráfica
    x_values = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
    y_values = [10, 15, 13, 17, 20]

    # Crear una gráfica de líneas con Plotly
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines+markers'))
    fig.update_layout(title='Ventas Mensuales', xaxis_title='Mes', yaxis_title='Ventas')

    # Convertir el gráfico a HTML para incrustarlo en la página
    graph_html = pio.to_html(fig, full_html=False)

    return render_template('chart.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
