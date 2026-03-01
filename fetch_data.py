import requests
import pandas as pd

def get_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url)
    data = response.json()

    rows = []

    for feature in data["features"]:
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]

        # Skip if magnitude is None
        if props["mag"] is None:
            continue

        rows.append({
            "magnitude": props["mag"],
            "place": props["place"],
            "lat": coords[1],
            "lon": coords[0],
            "depth": coords[2]
        })

    df = pd.DataFrame(rows)
    return df