import os
import re
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import webbrowser

current_dir = os.getcwd()

file_names = []
values = []
numbers = []

pattern = r'(\d{4})'

for filename in os.listdir(current_dir):
    if filename.endswith('.txt') and 'Table 3.1' in filename:
        file_path = os.path.join(current_dir, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1].strip()
            last_column_value = float(last_line.split()[-1])

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

first_num = sorted_numbers[0]

xaxis_range = [sorted_file_names[0], sorted_file_names[-1]]

fig.update_layout(
    title=f'Title',
    xaxis=dict(title='File Names', range=xaxis_range),
    yaxis=dict(title=f'Y-Axis Values (First Number: {first_num})', range = [0, 35000])
)

html_file_path = 'line_graph.html'
pio.write_html(fig, file=html_file_path)

webbrowser.open(html_file_path)


