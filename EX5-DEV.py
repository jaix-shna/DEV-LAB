import pandas as pd
import numpy as np
import folium

# Generate random data
np.random.seed(42)
num_points = 100
latitude = np.random.uniform(37.5, 38.5, num_points)
longitude = np.random.uniform(-123, -121, num_points)
value = np.random.randint(1, 100, num_points)

# Create a DataFrame
df = pd.DataFrame({
    'Latitude': latitude,
    'Longitude': longitude,
    'Value': value
})

# Save the DataFrame to a CSV file
df.to_csv('map_data.csv', index=False)

# Load the generated CSV file
df = pd.read_csv('map_data.csv')

# Display basic statistics about the data
print("Basic Statistics:")
print(df.describe())

# Create a base map centered at the mean location
base_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()],
                      zoom_start=10)

# Add data points to the map with popups showing the 'Value'
for index, row in df.iterrows():
    popup_text = f"Value: {row['Value']}"
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=popup_text).add_to(base_map)

# Save the map as an HTML file
base_map.save('interactive_map.html')

# If running in Jupyter Notebook, display the map inline
# base_map
