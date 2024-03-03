import streamlit as st
import random

def main():
    st.title('Antonia Website')
    st.write('Das ist eine, mit Streamlit programmierte, App.')
    st.write('Um etwas auszulösen, löse den folgenden Code aus')
    st.code('streamlit run hello_world.py')
    st.sidebar.title('Heyy, im Menu unterhalb kannst du die Einstellungen ändern')

    # Text input for scatter plot title
    scatter_plot_title = st.sidebar.text_input("Scatter Plot Title", "Random Data")

    # Slider for selecting number of data points
    num_points = st.sidebar.slider("Select number of data points", min_value=10, max_value=100, value=50)

    # Checkbox for gridlines
    show_gridlines = st.sidebar.checkbox("Show Gridlines", value=True)

    # Selectbox for marker color
    marker_color = st.sidebar.selectbox("Select marker color", ["blue", "red", "green"])

    # Radio button for marker symbol
    marker_symbol = st.sidebar.radio("Select marker symbol", ["circle", "square", "diamond"])

    # Slider for marker size
    marker_size = st.sidebar.slider("Select marker size", min_value=1, max_value=20, value=5)

    data = [[random.random() for _ in range(20)] for _ in range(num_points)]

    st.write('DataFrame')
    st.dataframe(data)

    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]

    st.write(f'### {scatter_plot_title}')
    st.write('This scatter plot chart is based on the first two columns of the DataFrame.')
    st.write(f'X-axis: Column 0, Y-axis: Column 1')

    # Scatter plot with customization based on user input
    fig = {
        "data": [{
            "x": x_values,
            "y": y_values,
            "type": "scatter",
            "mode": "markers",
            "marker": {"color": marker_color, "symbol": marker_symbol, "size": marker_size}
        }],
        "layout": {
            "title": scatter_plot_title,
            "xaxis": {"title": "Column 0", "showgrid": show_gridlines},
            "yaxis": {"title": "Column 1", "showgrid": show_gridlines}
        }
    }

    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
