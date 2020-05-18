# ~~~~~~~~~~~~~~~~~~~~~~~
# Hannah Shumway
# Geospatial Analyst
# NGA/AOCC
# 17 April 2020
# ~~~~~~~~~~~~~~~~~~~~~~~

# imports
import os
from IPython.core.display import display, clear_output
import ipywidgets as widgets
from density_tool import DensityAnalyzer


class GUI:
    def __init__(self):
        self.c = None
        self.t1_inputs = self.create_t1_inputs()
        self.t1_specs = self.create_t1_specs()
        self.run_button = self.create_runbutton()
        self.my_query_hbox = self.create_t1_widgets()
        self.out = self.create_output_space()

    def create_runbutton(self):
        run_button = widgets.Button(description="Run")
        GUI.run_button = run_button
        run_button.on_click(self.run_all)
        return run_button

    def create_output_space(self):
        out = widgets.Output()
        GUI.out = out
        return self.out

    def display(self):
        display(self.my_query_hbox, self.run_button)

    def create_t1_inputs(self):
        # pre-processing
        a = os.path.realpath("input/donotdelete.txt")
        b = "donotdelete.txt"
        self.c = a[:-1 * len(b)]
        d = os.listdir(self.c)
        ##
        my_label = widgets.HTML(value="<center>Data Inputs</center>")
        GUI.my_label = my_label
        ##
        input_csv = widgets.Dropdown(description="Input .csv", options=d, continuous_update=False)
        # This is the name of the input .csv you would like to analyze.
        self.input_csv = input_csv
        ##
        lat = widgets.Text(description="Latitude Field", value="latitude")
        self.lat = lat
        lat.on_submit(self.handler)
        ##
        lon = widgets.Text(description="Longitude Field", value="longitude")
        self.lon = lon
        lon.on_submit(self.handler)
        ##
        t1_inputs = widgets.VBox([my_label,
                                 input_csv, lat, lon])
        return t1_inputs
        # a VBox is a vertical box, whereas an HBox is a horizontal box...because of course it is

    def create_t1_specs(self):
        specs = widgets.HTML(value="<center>Clustering Specifications</center>")
        GUI.specs = specs
        ##
        eps = widgets.FloatSlider(description="Spatial Eps", value=.1, step=.1, max=5, orientation="horizontal", readout=True,
                                  readout_format='.1f')
        self.eps = eps
        ##
        min_pts = widgets.IntSlider(description="Min Pts", value="5", step=1, orientation="horizontal",
                                    readout=True, readout_format='d')
        self.min_pts = min_pts
        ##
        t1_specs = widgets.VBox([specs, eps, min_pts])
        return t1_specs

    def create_t1_widgets(self):
        my_query_hbox = widgets.HBox([self.t1_inputs, self.t1_specs])
        GUI.my_query_hbox = my_query_hbox
        return my_query_hbox

    def run_all(self, sender):
        d = DensityAnalyzer()
        d.run_density_analysis(self.c + self.input_csv.value, self.lat.value,
                               self.lon.value, self.eps.value, self.min_pts.value)

    def handler(self, sender):
        self.run_all(sender)






