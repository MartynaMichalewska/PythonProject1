import openpyxl
from openpyxl.chart import Reference,BarChart
wb = openpyxl.load_workbook('../data/videogamesales.xlsx')
ws=wb.active

ws=wb['Breakdown of Sales by Genre']

values=Reference(ws,
                 min_col=2,
                 min_row=1,
                 max_col=5,
                 max_row=13)

cats=Reference(ws,
                min_col=1,
                min_row=2,
                max_col=1,
                max_row=13)

chart=BarChart()
chart.add_data(values,titles_from_data=True)
chart.set_categories(cats)

chart.title='Sales Breakdown'
chart.x_axis.title='Genre'
chart.y_axis.title='Breakdown of Sales by Genre'
ws.add_chart(chart, 'H2')

wb.save('../data/videogamesales.xlsx')