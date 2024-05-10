import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sistem_rekomendasi_modul

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

# ini disini data nama dan data 1 - 10 dimasukin ke database dulu


if submitted:
    # mulai dari sini, sistem rekomendasinya berjalan
    df_new = pd.DataFrame(columns=['Pengelolaan informasi pembelajaran', 'Pengelolaan situasi yang dihadapi', 'Kreativitas dalam bersikap', 'Pola Komunikasi', 'Interaksi dengan lingkungan pembelajaran', 'Pengambilan Keputusan dan Kepemimpinan', 'Minat Karir dan Kesesuaian potensi bidang pekerjaan', 'Saran Pengembangan Diri 1', 'Saran Pengembangan Diri 2', 'Saran Pengembangan Diri 3', 'Saran Pengembangan Diri 4'])

    item_df = pd.read_csv('training_data_cleaned_translated.csv')

    df_new.loc[len(df_new)] = [data1, data2, data3, data4, 
                            data5, data6, data7, data8,
                            data9, data10, data11]

    df_cleaned_neww = sistem_rekomendasi_modul.get_user_input(df_new)
    item_ranking_new, item_ranking_aggregated, item_df  = sistem_rekomendasi_modul.tfidf_new(df_cleaned_neww, item_df)
    top_3_new, top_3_aggregated = sistem_rekomendasi_modul.result(item_ranking_new, item_ranking_aggregated, item_df)

    st.subheader("Rekomendasi top berdasarkan skor kesamaan pengguna baru:")
    st.write(top_3_new)

    st.subheader("\nRekomendasi top berdasarkan agregasi skor kesamaan pengguna lain:")
    st.write(top_3_aggregated)
