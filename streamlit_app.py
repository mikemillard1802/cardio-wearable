   """
   Wearables Visualizer - Simple Physician Demo
   Clean, simple dashboard for client demonstrations
   Simulated vital signs that auto-update every 3 seconds
   No backend required - works standalone
   URL Usage: https://cardio-wearable.streamlit.app/?patient=JohnDoe&device=watch123
   """
   import streamlit as st
   import random
   import time
   from datetime import datetime

   # Page config
   st.set_page_config(
       page_title="Wearables Visualizer - Demo",
       page_icon="⌚",
       layout="centered"
   )

   # Parse URL parameters
   query_params = st.query_params
   patient_id = query_params.get("patient", "Patient")
   device_id_param = query_params.get("device", "Unknown")

   # Title
   st.title("⌚ Wearables Visualizer")
   st.markdown(f"**Patient:** {patient_id} | **Device:** {device_id_param}")
   st.markdown("**Samsung Watch Active 2** | Real-Time Vital Signs Monitoring")

   # Sidebar
   st.sidebar.title("👤 Patient Info")
   patient_name = st.sidebar.text_input("Patient Name", patient_id)
   patient_dob = st.sidebar.text_input("Date of Birth", "1965-03-15")
   device_id = st.sidebar.text_input("Device ID", device_id_param)
   st.sidebar.markdown("---")
   st.sidebar.title("📡 Status")
   st.sidebar.success("✅ Connected")
   st.sidebar.info("🌐 Verizon LTE Hotspot")

   # Initialize simulated data
   if "heart_rate" not in st.session_state:
       st.session_state.heart_rate = 72
       st.session_state.spo2 = 98
       st.session_state.steps = 5432
       st.session_state.bp_sys = 120
       st.session_state.bp_dia = 80
       st.session_state.glucose = 95
       st.session_state.last_update = datetime.now()

   def generate_vitals():
       """Generate realistic simulated vital signs"""
       st.session_state.heart_rate = random.randint(65, 95)
       st.session_state.steps += random.randint(1, 10)
       st.session_state.spo2 = random.randint(96, 100)
       st.session_state.bp_sys = random.randint(115, 130)
       st.session_state.bp_dia = random.randint(75, 85)
       st.session_state.glucose = random.randint(85, 110)
       st.session_state.last_update = datetime.now()

   # Auto-refresh using native Streamlit (no extra deps)
   auto_refresh = st.sidebar.checkbox("Auto-refres h (3s)", value=True)
   if auto_refresh:
       time.sleep(3)
       generate_vitals()
       st.rerun()

   # Main Display
   st.header("❤️ Vital Signs")
   col1, col2, col3 = st.columns(3)

   with col1:
       hr = st.session_state.heart_rate
       st.metric("Heart Rate", f"{hr} BPM")
       if hr > 100:
           st.error("🔴 Tachycardia")
       elif hr < 60:
           st.error("🔴 Bradycardia")
       else:
           st.success("✅ Normal")

   with col2:
       spo2 = st.session_state.spo2
       st.metric("SpO2", f"{spo2}%")
       if spo2 < 95:
           st.warning("⚠️ Low O2")
       else:
           st.success("✅ Normal")

   with col3:
       st.metric("Steps", f"{st.session_state.steps:,}")

   # Secondary metrics
   st.header("📊 Additional Metrics")
   col4, col5 = st.columns(2)

   with col4:
       bp = f"{st.session_state.bp_sys}/{st.session_state.bp_dia}"
       st.metric("Blood Pressure", f"{bp} mmHg")

   with col5:
       st.metric("Blood Glucose", f"{st.session_state.glucose} mg/dL")

   # Alerts
   st.header("🚨 Clinical Alerts")
   hr = st.session_state.heart_rate
   spo2 = st.session_state.spo2
   has_alert = False

   if hr > 100 or hr < 60:
       st.error(f"🔴 Heart Rate Alert: {hr} BPM")
       has_alert = True

   if spo2 < 95:
       st.warning(f"⚠️ Low Oxygen: {spo2}%")
       has_alert = True

   if not has_alert:
       st.success("✅ All vitals normal")

   # Test buttons
   st.markdown("---")
   col_btn1, col_btn2 = st.columns(2)

   with col_btn1:
       if st.button("🔄 Refresh"):
           generate_vitals()
           st.rerun()

   with col_btn2:
       if st.button("⚠️ Test Alert"):
           st.session_state.heart_rate = 115
           st.session_state.spo2 = 93
           st.rerun()

   # Footer
   st.markdown("---")
   st.caption(
       f"**Patient:** {patient_name} | **DOB:** {patient_dob} | "
       f"**Updated:** {datetime.now().strftime('%H:%M: %S')} | **Demo Mode**"
   )
