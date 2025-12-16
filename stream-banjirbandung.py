import pickle
import streamlit as st

# membaca model
Banjir_model = pickle.load(open('Banjir_model.sav', 'rb'))

# judul web
st.title('Data Mining Prediksi Banjir di Bandung')

# membagi column
col1, col2 = st.columns(2)

with col1 :
    Tahun = st.text_input('Input Tahun')

with col2 :
    Bulan = st.text_input('Input Bulan')

with col1 :
    Curah_Hujan = st.text_input('Input Curah Hujan (mm)')

with col2 :
    Min_temp = st.text_input('Input Suhu Minimum (°C)')

with col1 :
    max_temp = st.text_input('Input Suhu Maksimum (°C)')

with col2 :
    avg_temp = st.text_input('Input Suhu Rata-rata (°C)')   

with col1 :
    min_kelembapan = st.text_input('Input Kelembapan Minimum (%)')

with col2 :
    max_kelembapan = st.text_input('Input Kelembapan Maksimum (%)')

with col1 :
    avg_kelembapan = st.text_input('Input Kelembapan Rata-rata (%)')

# code untuk prediksi
banjir_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Prediksi Banjir'):
    banjir_prediction = Banjir_model.predict([[Bulan, Tahun, Curah_Hujan, Min_temp, max_temp, avg_temp, min_kelembapan, max_kelembapan, avg_kelembapan]])

    if (banjir_prediction[0] == 1):
        banjir_diagnosis = 'Area Berpotensi Banjir'
    else:
        banjir_diagnosis = 'Area Tidak Berpotensi Banjir'

    st.success(banjir_diagnosis)

