import streamlit as st
import pickle
import numpy as np

# --- Load pipeline ---
Banjir_model = pickle.load(open('Banjir_model.sav', 'rb'))

st.title('Data Mining Prediksi Banjir di Bandung')

col1, col2 = st.columns(2)

with col1:
    Bulan = st.number_input('Bulan', min_value=1, max_value=12, step=1)
    Curah_Hujan = st.number_input('Curah Hujan (mm)', step=0.1)
    max_temp = st.number_input('Suhu Maksimum (°C)', step=0.1)
    min_kelembapan = st.number_input('Kelembapan Minimum (%)', step=0.1)
    avg_kelembapan = st.number_input('Kelembapan Rata-rata (%)', step=0.1)

with col2:
    Tahun = st.number_input('Tahun', min_value=2000, max_value=2100, step=1)
    Min_temp = st.number_input('Suhu Minimum (°C)', step=0.1)
    avg_temp = st.number_input('Suhu Rata-rata (°C)', step=0.1)
    max_kelembapan = st.number_input('Kelembapan Maksimum (%)', step=0.1)

if st.button('Prediksi Banjir'):
    input_data = np.array([[Bulan, Tahun, Curah_Hujan, Min_temp, max_temp,
                            avg_temp, min_kelembapan, max_kelembapan, avg_kelembapan]])
    prediction = Banjir_model.predict(input_data)

    if prediction[0] == 0:
        st.success("Hasil Prediksi: Tidak akan terjadi banjir")
    else:
        st.error("Hasil Prediksi: Akan terjadi banjir")

    # Menampilkan probabilitas
    proba = Banjir_model.predict_proba(input_data)
    st.info(f"Probabilitas Tidak Banjir: {proba[0][0]*100:.2f}% | Banjir: {proba[0][1]*100:.2f}%")
