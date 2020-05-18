# ~~~~~~~~~~~~~~~~~~~~~~~
## Hannah Shumway
## Geospatial Analyst
## NGA/AOCC
## Code idea adapted from:
##  http://qingkaikong.blogspot.com/2016/08/clustering-with-dbscan.html
# ~~~~~~~~~~~~~~~~~~~~~~~
# TODO
# Possibly add a GUI input for an output shapefile name.

# imports
import os
import pandas as pd
import geopandas as gpd
from IPython.core.display import display
from folium import Map
from geopandas import GeoDataFrame
from sklearn.cluster import DBSCAN
import numpy as np
from shapely.geometry import Point
import folium
import folium.plugins as plug



class DensityAnalyzer:
    def __init__(self):
        self.kms_per_radian = 6371.0088
        self.output_frame = pd.DataFrame()
        self.n_clusters = 0

    def read_data_to_df(self, file_path):  # remember to generate an auto file path from the _input folder & dropdown
        df = pd.read_csv(file_path)
        return df

    def df_condition(self, data_frame, lat_col, lon_col):
        df1 = data_frame.filter([lat_col, lon_col])
        coords = df1.values
        return coords

    def dbscanner(self, data_frame, coordinates, eps_input, pts_input):
        epsilon = eps_input / self.kms_per_radian
        db = DBSCAN(eps=epsilon, min_samples=pts_input,
                    algorithm='ball_tree', metric='haversine').fit(np.radians(coordinates))
        cluster_labels = db.labels_
        self.n_clusters = len(set(cluster_labels))
        data_frame["Clust_DB"] = cluster_labels
        self.output_frame = data_frame
        # cluster_labels = -1 means outliers
        clusters = pd.DataFrame([coordinates[cluster_labels == n] for n in range(-1, self.n_clusters)])
        return clusters

    def create_plot_layers(self, lat_col, lon_col):
        lat_mean = self.output_frame[lat_col].mean()
        lon_mean = self.output_frame[lon_col].mean()
        counter = 0
        m = Map(location=[lat_mean, lon_mean], zoom_start=4)
        latitudes = list(self.output_frame[lat_col])
        longitudes = list(self.output_frame[lon_col])
        labels = list(self.output_frame["Clust_DB"])
        color_list = ['orange', 'pink', 'lightred', 'cadetblue', 'darkgreen',
                      'lightgray', 'lightblue', 'lightgreen',
                      'green', 'blue', 'purple', 'darkblue', 'gray',
                      'white', 'red', 'darkpurple', 'beige', 'darkred', 'black']
        for lat, lng, label in zip(latitudes, longitudes, labels):
            if label == 0:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="darkred", icon='info-sign')
                ).add_to(m)
            if label == 1:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="beige", icon='info-sign')
                ).add_to(m)
            if label == 2:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="darkpurple", icon='info-sign')
                ).add_to(m)
            if label == 3:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="black", icon='info-sign')
                ).add_to(m)
            if label == 4:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="red", icon='info-sign')
                ).add_to(m)
            if label == 5:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="orange", icon='info-sign')
                ).add_to(m)
            if label == 6:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="gray", icon='info-sign')
                ).add_to(m)
            if label == 7:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="darkblue", icon='info-sign')
                ).add_to(m)
            if label == 8:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="purple", icon='info-sign')
                ).add_to(m)
            if label == 9:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="blue", icon='info-sign')
                ).add_to(m)
            if label == 10:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="green", icon='info-sign')
                ).add_to(m)
            if label == 11:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="lightgreen", icon='info-sign')
                ).add_to(m)
            if label == 12:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="lightblue", icon='info-sign')
                ).add_to(m)
            if label == 13:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="lightgray", icon='info-sign')
                ).add_to(m)
            if label == 14:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="darkgreen", icon='info-sign')
                ).add_to(m)
            if label == 15:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="cadetblue", icon='info-sign')
                ).add_to(m)
            if label == 16:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="lightred", icon='info-sign')
                ).add_to(m)
            if label == 17:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="pink", icon='info-sign')
                ).add_to(m)
            if label == 18:
                folium.Marker(
                    location=[lat, lng],
                    popup=label,
                    icon=folium.Icon(color="white", icon='info-sign')
                ).add_to(m)
            if label >= 19:
                if counter == 0:
                    print("Warning: DBSCAN has identified 20+ in your data. You may want to adjust"
                      "your clustering specifications or view your data in a desktop GIS.")
                    counter += 1

        display(m)

    def get_shapefile(self, data_frame, lon_col, lat_col):
        crs = {'init': 'epsg:4326'}
        geometry = [Point(xy) for xy in zip(data_frame[lon_col], data_frame[lat_col])]
        gdf = GeoDataFrame(data_frame, crs=crs, geometry=geometry)
        a = os.path.realpath("output/donotdelete.txt")
        b = "donotdelete.txt"
        c = a[:-1 * len(b)]
        gdf.to_file(c + "dbscan_output.shp")


    def run_density_analysis(self, file_path, lat_col, lon_col, eps_input, pts_input):
        df = self.read_data_to_df(file_path)
        conditioned_coords = self.df_condition(df, lat_col, lon_col)
        self.dbscanner(df, conditioned_coords, eps_input, pts_input)
        self.get_shapefile(self.output_frame, lon_col,lat_col)
        self.create_plot_layers(lat_col, lon_col)

