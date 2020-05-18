# (U) DBSCAN Density Tool

## (U) Overview

(U) The DBSCAN Density Tool takes any comma separated values (.csv) file with latitude and longitude fields and performs density-based clustering on the data using user-provided values for spatial search radius and minimum number of points per cluster; it outputs a shapefile with the clustered data and an interactive map depicting the clusters.

## (U) What is DBSCAN?

(U) DBSCAN stands for **d**ensity-**b**ased **s**patial **c**lustering of **a**pplications with **n**oise. It is a popular unsupervised machine learning algorithm that divides data into meaningful sub-groups. It assumes that 'clusters' are dense regions in space separated by regions of lower density. The algorithm finds dense areas and expands these recursively to find dense, often
arbitrarily shaped clusters.

(U) Two main parameters to DBSCAN are ‘ε’ (also known as ‘spatial epsilon‘) and ‘minPoints’. 

    - ‘ε’ defines the radius of the ‘neighborhood region’ for data points to be considered in the same cluster
    - ‘minPoints’ defines the minimum number of points thats should be contained within that neighborhood in order to deem it a cluster

[U) More technical details from the academic paper that introduced the DBSCAN algorithm](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf)

[(U) Documentation for the scikit-learn DBSCAN method used in this tool](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)


## (U) How to use the DBSCAN Density Tool

### (U) Setup

(U) Option 1: If you have SSH keys set up with GitHub, clone this repository into a Jupyter instance by pasting ```git+ssh...``` into a new Terminal. BAM! Now you have all of the ```dbscan_density_tool``` files. ***This is by far the most straightforward option, and getting your SSH keys set up in GitHub will be useful for quick use of other tools as well.***

(U) Option 2: If you don't have your SSH keys set up in GitHub or aren't comfortable using the Terminal window, you can download this GitHub repository as a .zip file, upload it to your Jupyter home page, and use the [```unzip``` tool](provide link here) to automatically unzip the file into its correct folder structure. 

(U) You can also upload each file individually to Jupyter and recreate the repository's file folder structure yourself, but this is **not recommended** because it is quite time-consuming.

### (U) Inputs

(U) First, open up the ```dbscan_density tool``` folder and navigate to the subfolder called ```input``` . Once there, upload a .csv file with the data you would like to analyze. This can be any kind of data - it just has to have separate columns for latitude and longitude values expressed in decimal degrees (e.g., -74.23245). You can upload numerous files if you would like; the user interface of the tool allows you to choose from a dropdown list of files in this folder to analyze.

(U) Next, navigate back to the first layer of the ```dbscan_density_tool``` folder and open the ```DBSCAN_density_tool.ipynb``` file. Run the first cell of the file by clicking on it and pressing SHIFT + ENTER. A small user interface will pop up after a couple of seconds.

(U) The inputs for the tool fall into two categories: Data Inputs and Clustering Specifications.

#### (U) Data Inputs

(U) **Input .csv**: Use the dropdown menu to select the file from your ```input``` folder that you would like to perform clustering on.

(U) **Latitude field**: Enter the name of the field/column in your .csv file that contains latitude information. The default value is "latitude", but other common field names include "lat" or "y", so make sure to double-check the field names in your data.

(U) **Longitude field**: Enter the name of the field/column in your .csv file that contains longitude information. The default value is "longitude", but other common field names include "lon","long", or "x", so make sure to double-check the field names in your data.

#### Clustering Specifications

(U) **Spatial Eps**: Use the sliding widget to select an appropriate spatial epsilon to define the radius of the 'neighborhood region' (in this case, expressed as distance in kilometers) for DBSCAN. In other words, what is the maximum distance between two points that you would still want the tool deem them "in the same cluster"? 

(U) The default value is .1 KM or 100m, which is meant for situations where you 1) have good, granular location data, and 2) have a desire to pinpoint very specific locations. Otherwise, if you're looking at a phenomenon that might be more useful to analyze at the neighborhood or city level, you might choose 1-3 KM as your spatial epsilon. 

(U) **Min Pts**: Use the sliding widget to select the minimum number of points that you would like DBSCAN to consider a "cluster". The default value is 5, but depending on the size of your dataset, you may want to change this. If you want to reduce the number of output clusters that you get, for example, make the Min Pts value larger.

(U) Feel free run the tool multiple times with different spatial epsilon and min pts values if you're unsure about where to set these parameters. Go to ```Kernel``` --> ```Restart & Run All``` to reset the tool.

#### (U) When you're done filling in your inputs, click the ```Run``` button to start your DBSCAN analysis.

### (U) Outputs

(U) **Shapefile**: The DBSCAN Density Tool creates an point shapefile with your clustering results that you can find in the ```output``` folder, labeled with a timestamp. You can then import this file into ArcGIS or another spatial analysis tool to view the clusters and complete further analysis. The tool preserves all of your original data's columns and adds a ```Clust_DB``` field that indicates which, if any, cluster a particular entry was sorted into. A value of ```-1``` means that the entry was not added to a cluster (either because it was in a cluster that did not fit the min pts threshold or because it wasn't within the spatial eps distance of any other entries). 

(U) **Interactive map**: The DBSCAN Density Tool also automatically creates an interactive map in the Jupyter widget interface that pops up within seconds after you run the tool. It depicts each cluster with a unique color of map marker, so that you can quickly get a visual sense of where all the clusters are located. Plus, you can zoom in to see the individual points that are contained within a cluster of interest.

## (U) Point of Contact

(U) If you have any questions about the tool or suggestions for improvement, please contact [insert email here](@.com)