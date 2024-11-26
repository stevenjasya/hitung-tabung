import streamlit as st
import math

st.title("Menghitung : red[Volume Tabung] :moon:")

r = st.number_input("Masukkan Jari-jari (cm): ",0)
t = st.number_input("Masukkan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {v:.2f}')
