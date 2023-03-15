import osmnx as ox

# Define the bounding box for Hefei city
north, south, east, west = 32.043, 31.754, 117.559, 117.166
bbox = (north, south, east, west)

# Download the street network of Hefei city as a graph
G = ox.graph_from_bbox(north, south, east, west, network_type='drive')

# Save the street network as a shapefile
ox.io.save_graph_shapefile(G, filepath='hefei_streets')
