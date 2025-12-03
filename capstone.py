from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

years = ["2016", "2017", "2018", "2019"]

HI = [175, 190, 130, 160]
HI_err = [40, 35, 30, 30]

HO = [120, 140, 130, 135]
HO_err = [20, 25, 20, 25]

PU = [90, 275, 95, 150]
PU_err = [40, 190, 30, 40]

x = list(range(len(years)))
width = 0.25

p = figure(
    width=800,
    height=500,
    title="Counts by Division",
    background_fill_color="#EBECED"
)

colors = {
    "HI": "red",
    "HO": "green",
    "PU": "blue"
}

def add_group(label, values, errors, offset, color):
    xs = [i + offset for i in x]
    
    p.vbar(
        x=xs, 
        top=values, 
        width=0.22,
        color=color,
        legend_label=label
    )
    
    for xi, yi, err in zip(xs, values, errors):
        p.segment(x0=xi, y0=yi - err, x1=xi, y1=yi + err, color="black")
        p.segment(x0=xi - 0.05, y0=yi + err, x1=xi + 0.05, y1=yi + err, color="black")
        p.segment(x0=xi - 0.05, y0=yi - err, x1=xi + 0.05, y1=yi - err, color="black")

add_group("HI", HI, HI_err, offset=-0.25, color=colors["HI"])
add_group("HO", HO, HO_err, offset=0, color=colors["HO"])
add_group("PU", PU, PU_err, offset=0.25, color=colors["PU"])

p.xaxis.ticker = x
p.xaxis.major_label_overrides = {i: years[i] for i in x}

p.xaxis.axis_label = "Year"
p.yaxis.axis_label = "Number of Individuals"
p.title.text_font_size = "16px"
p.legend.title = "Division"
p.grid.grid_line_color = "white"

show(p)