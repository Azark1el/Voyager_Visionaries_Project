import os
import re
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import webbrowser
from extractor import name_list

current_dir = os.getcwd()

def makegraph(word, name):
    file_names = []
    values = []
    numbers = []

    pattern = r'(\d{4})'

    max_y_value = 0

    for filename in os.listdir(current_dir):
        # change the name of the 'Table 3...' to extract a new table
        if filename.endswith('.txt') and word in filename:
            file_path = os.path.join(current_dir, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                last_line = lines[-1].strip()
                last_column_value = float(last_line.split()[-1])

                if last_column_value > max_y_value:
                    max_y_value = round(last_column_value *1.2, -3)

                extracted_num = re.findall(pattern, filename)

                if extracted_num:
                    file_names.append(filename)
                    values.append(last_column_value)
                    numbers.append(int(''.join(extracted_num)))

    sorted_data = sorted(zip(numbers, file_names, values))
    sorted_numbers, sorted_file_names, sorted_values = zip(*sorted_data)

    fig = make_subplots()
    trace = go.Scatter(x=sorted_file_names, y=sorted_values, mode = 'lines+markers')
    fig.add_trace(trace)

    xaxis_range = [name[:4] for name in sorted_file_names]

    fig.update_layout(
        title=name,
        xaxis=dict(title='Years', tickvals=sorted_file_names, ticktext=xaxis_range),
        yaxis=dict(title=name, range = [0, max_y_value])
    )

    html_file_path = 'line_graph'+ word + '.html'
    pio.write_html(fig, file=html_file_path)

    webbrowser.open(html_file_path)

title_list = ['Number of objects orbiting Earth','Mass in tons orbiting Earth','Area in m2 orbiting Earth']

for name in name_list:
    makegraph(name, title_list[name_list.index(name)])


