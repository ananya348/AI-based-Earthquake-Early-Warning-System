# 🌍 AI-Based Earthquake Early Warning System 🚨

A real-time AI-powered disaster monitoring platform that detects nearby earthquakes and alerts users instantly using Machine Learning, geospatial filtering, and browser push notifications.

🔴 **Live AI alerts**
📡 **Real-time seismic data**
📍 **Location-based danger detection**
🔔 **Browser notifications**

---

## 🚀 Live Demo

> Deploy link here
> `https://your-app-name.streamlit.app`

---

## ✨ Key Features

* 🌐 Real-time earthquake data from USGS API
* 🤖 Machine Learning-based risk prediction
* 📍 Location-based alert filtering
* 🔔 Browser push notifications
* ⏱️ Auto-refresh every 60 seconds
* 🗺️ Interactive global earthquake map
* 🚨 High-risk alert system

---

## 🧠 How It Works

1. Fetches live earthquake data from USGS
2. Uses ML model to classify earthquake risk
3. Calculates distance from user location
4. Triggers alerts if dangerous quake is nearby
5. Sends browser push notification

---

## 🛠️ Tech Stack

| Category    | Technology                   |
| ----------- | ---------------------------- |
| Language    | Python                       |
| ML Model    | Random Forest (Scikit-learn) |
| Frontend    | Streamlit                    |
| Maps        | Folium                       |
| Data Source | USGS Earthquake API          |
| Deployment  | Streamlit Cloud              |

---

## 📊 System Architecture

```
USGS API → Data Processing → ML Model → Distance Filter → Alert Engine → Streamlit UI
```

---

## 📁 Project Structure

```
earthquake-alert-system/
│
├── app.py               # Main Streamlit application
├── fetch_data.py        # Real-time data collection
├── train_model.py       # ML model training
├── utils.py             # Distance calculations
├── model.pkl            # Trained ML model
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-Earthquake-Alert-System.git
cd AI-Earthquake-Alert-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train Model

```bash
python train_model.py
```

### 4️⃣ Run App

```bash
streamlit run app.py
```

---

## 🔔 Enable Notifications

1. Click **Enable Notifications** inside the app
2. Allow browser permission
3. Receive real-time earthquake alerts 🚨

---

## 📸 Screenshots

### 🖥️ Dashboard
![Dashboard](<img width="1910" height="1075" alt="Screenshot 2026-03-01 121019" src="https://github.com/user-attachments/assets/e767b8ac-c27f-4c77-99ff-64f13ab22f40" />)
)

---

### 🗺️ Live Earthquake Map
![Map](<img width="1364" height="707" alt="Screenshot 2026-03-01 121301" src="https://github.com/user-attachments/assets/2beab8a5-ed89-43ac-8b6b-97c2988da729" />
)

---

### 🔔 Notifications Enabled
![Notification](<img width="1144" height="392" alt="image" src="https://github.com/user-attachments/assets/1ed7360f-3aff-45a4-866d-d2ff06f76d2d" />
)

---

### 🚨 Alert Mode
![Alert](assets/alert.png)

## 💡 Use Cases

* Disaster early warning systems
* Smart city monitoring
* Research in seismic AI
* Emergency response tools
* EdTech AI projects

---

## 🧪 Future Enhancements

* 📧 Email + SMS alerts
* 📱 Mobile app version
* 🧠 Deep learning (LSTM prediction)
* 🌡️ Damage estimation AI
* 📊 Advanced analytics dashboard
* 📡 IoT seismic sensors

---

## 🎓 Learning Outcomes

* Real-time data engineering
* Applied Machine Learning
* Geospatial analytics
* Streamlit app deployment
* AI for social good

---

## 👩‍💻 Author

**Ananya**
B.Tech CSE (AI/ML) Student
Passionate about AI for real-world impact 🌍

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---

## 📜 License

This project is open-source and available under the MIT License.
