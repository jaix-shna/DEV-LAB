import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import requests
import zipfile
import io
import os

# Correct URL to the Natural Earth shapefile ZIP
url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"

extract_folder = "ne_110m_admin_0_countries"

if not os.path.exists(extract_folder):
    print("Downloading shapefile...")
    r = requests.get(url)
    r.raise_for_status()  # Raise error if download fails

    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Extracting shapefile...")
    z.extractall(extract_folder)
else:
    print("Shapefile already downloaded and extracted.")

# Find the .shp file path inside the extracted folder
shp_path = None
for file in os.listdir(extract_folder):
    if file.endswith(".shp"):
        shp_path = os.path.join(extract_folder, file)
        break

if shp_path is None:
    raise FileNotFoundError("Could not find the .shp file in extracted contents.")

# Load the shapefile
world_map = gpd.read_file(shp_path)

# Your sample data
world_data = pd.DataFrame({
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})

# Merge shapefile GeoDataFrame with your data
world_data_geo = world_map.merge(world_data, how='left', left_on='NAME', right_on='Country')

# Plotting
fig, ax = plt.subplots(figsize=(15, 10))
world_data_geo.boundary.plot(ax=ax, linewidth=1, color='black')
world_data_geo.plot(column='Value', ax=ax, legend=True,
                    legend_kwds={'label': "Values by Country"},
                    cmap='OrRd', missing_kwds={"color": "lightgrey"})

ax.set_title('World Map with Values by Country', fontsize=16)
ax.axis('off')

plt.show()
