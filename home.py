import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Selamat datang di AI Rekomendasi Karir!")
st.write("Masukkan input, nanti kami akan merekomendasikan jalur karir yang cocok denganmu!")

with st.form(key='my_form'):
    nama = st.text_input("Masukkan Nama: ")
    data1 = st.text_input("Masukkan pengelolaan informasi pembelajaran: ")
    data2 = st.text_input("Masukkan pengelolaan situasi yang dihadapi: ")
    data3 = st.text_input("Masukkan kreativitas dalam bersikap: ")
    data4 = st.text_input("Masukkan pola komunikasi: ")
    data5 = st.text_input("Masukkan interaksi dengan lingkungan pembelajaran: ")
    data6 = st.text_input("Masukkan Pengambilan Keputusan dan Kepemimpinan: ")
    data7 = st.text_input("Masukkan minat karir dan kesesuaian potensi bidang pekerjaan: ")
    data8 = st.text_input("Masukkan saran pengembangan diri 1: ")
    data9 = st.text_input("Masukkan saran pengembangan diri 2: ")
    data10 = st.text_input("Masukkan saran pengembangan diri 3: ")
    data11 = st.text_input("Masukkan saran pengembangan diri 4: ")
    submitted = st.form_submit_button(label="Submit")

if submitted:
    # Lakukan tindakan sesuai dengan apa yang Anda inginkan saat tombol "Submit" ditekan
    st.write("Nama: ", nama)
    st.write("Pengolalaan Informasi Pemebelajaran: ", data1)
    st.write("Pengelolaan situasi yang dihadapi: ", data2)
    st.write("Kreativitas dalam bersikap: ", data3)
    st.write("Pola Komunikasi: ", data4)
    st.write("Interaksi dengan lingkungan pembelajaran: ", data5)
    st.write("Pemngambilan Keputusan dan Kepemimpinan: ", data6)
    st.write("Minat Karir dan Kesesuaian potensi bidang pekerjaan: ", data7)
    st.write("Saran pengembangan diri 1: ", data8)
    st.write("Saran pengembangan diri 2: ", data9)
    st.write("Saran pengembangan diri 3: ", data10)
    st.write("Saran pengembangan diri 4: ", data11)