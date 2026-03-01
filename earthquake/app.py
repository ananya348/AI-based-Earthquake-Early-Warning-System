import streamlit as st
import joblib
from fetch_data import get_earthquake_data
from utils import calculate_distance
import folium
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components
st.subheader("🔔 Enable Browser Notifications")

if st.button("Enable Notifications"):
    components.html("""
    <script>
    Notification.requestPermission().then(function(permission) {
        if (permission === "granted") {
            alert("Notifications Enabled ✅");
        } else {
            alert("Notifications Blocked ❌");
        }
    });
    </script>
    """)

st.set_page_config(page_title="AI Earthquake Alert", layout="wide")
# Auto refresh every 60 seconds
st_autorefresh(interval=60000, key="datarefresh")

st.title("🌍 AI-Based Earthquake Early Warning System")

# Sidebar inputs
st.sidebar.header("📍 Enter Your Location")

user_lat = st.sidebar.number_input("Latitude", value=22.5726)
user_lon = st.sidebar.number_input("Longitude", value=88.3639)
radius = st.sidebar.slider("Alert Radius (km)", 50, 1000, 500)

# Load model
model = joblib.load("model.pkl")

# Fetch live data
df = get_earthquake_data()

# Predict risk
df["predicted_risk"] = model.predict(df[["magnitude", "depth"]])

# Calculate distance
df["distance_km"] = df.apply(
    lambda row: calculate_distance(user_lat, user_lon, row["lat"], row["lon"]),
    axis=1
)

# Filter high-risk nearby quakes
alerts = df[(df["distance_km"] < radius) & (df["predicted_risk"] == 2)]

# Alert Section
st.subheader("🚨 Alert Status")

if not alerts.empty:
    st.error("⚠️ HIGH RISK EARTHQUAKE DETECTED NEAR YOU!")

    # Browser Push Notification
    components.html("""
    <script>
    if (Notification.permission !== "granted") {
        Notification.requestPermission();
    } else {
        new Notification("🚨 Earthquake Alert!", {
            body: "High-risk earthquake detected near your location!",
            icon: "https://cdn-icons-png.flaticon.com/512/616/616490.png"
        });
    }
    </script>
    """)
    st.dataframe(alerts[["place", "magnitude", "distance_km"]])
else:
    st.success("✅ No high-risk earthquakes nearby")

# Map Section
st.subheader("🗺️ Live Earthquake Map")

m = folium.Map(location=[user_lat, user_lon], zoom_start=3)

# User marker
folium.Marker(
    [user_lat, user_lon],
    popup="Your Location",
    icon=folium.Icon(color="blue")
).add_to(m)

# Earthquake markers
for _, row in df.iterrows():
    color = "red" if row["predicted_risk"] == 2 else "orange"
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=row["magnitude"] * 2,
        popup=f"{row['place']} | Mag: {row['magnitude']}",
        color=color,
        fill=True
    ).add_to(m)

st_folium(m, width=1000, height=500)