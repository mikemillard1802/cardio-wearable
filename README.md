# Cardio Wearable — Streamlit Demo App

Live demo: https://cardio-wearable.streamlit.app/

## Overview
Simple physician-facing dashboard showing simulated real-time vital signs from a Samsung Galaxy Watch Active 2. Designed for client demonstrations — no backend required.

## Features
- Simulated vitals: Heart Rate, SpO2, Steps, Blood Pressure, Blood Glucose
- Auto-refresh every 3 seconds (native Streamlit, no extra deps)
- Clinical alerts: Tachycardia, Bradycardia, Low O2
- URL parameter support: `?patient=JohnDoe&device=watch123`
- Test alert button for demos
- Clean, mobile-friendly layout

## Deploy to Streamlit Cloud
1. Fork/clone this repo
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Set main file: `streamlit_app.py`
4. Deploy — no secrets needed

## Local Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## URL Parameters
| Param | Default | Description |
|-------|---------|-------------|
| `patient` | "Patient" | Patient name |
| `device` | "Unknown" | Device identifier |

Example: `https://cardio-wearable.streamlit.app/?patient=JohnDoe&device=Samsung_Active2_001`

## Architecture
- **Frontend only** — pure Streamlit, session_state for persistence
- **No external deps** — `streamlit_autorefresh` removed, uses native `time.sleep` + `st.rerun`
- **Minimal requirements** — only `streamlit` and `pandas`

---

Part of Clinical Alert AI remote monitoring system.
Archive workspace: `mikemillard1802/-expo-workspace`