import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('resiko_kesehatan_ibu.sav', 'rb'))

#judul web
st.title('Prediksi Resiko Kesehatan Ibu')


col1, col2,  = st.columns(2)

st.text ('Vina Alviani , 191351102')
with col1 :
    Age = st.number_input('Usia')
with col2 :
    SystolicBP = st.number_input('BP Sistolik')
with col1 :
    DiastolicBP = st.number_input('BP Diastolik')
with col2 :
    BS = st.number_input('Kadar Glukosa Darah')
with col1 :
    BodyTemp = st.number_input('Suhu Tubuh')
with col2 :
    HeartRate = st.number_input('Detak jantung')

# code for prediction
resiko_kesehatan_ibu_diagnosis =''

# membuat tombol prediksi 
if st.button('Prediksi Resiko Kesehatan Ibu'):
    resiko_kesehatan_ibu_prediction = model.predict([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])

    if (resiko_kesehatan_ibu_prediction[0]==1):
        resiko_kesehatan_ibu_diagnosis = 'Resiko Rendah Kesehatan Ibu'
    else :
        resiko_kesehatan_ibu_diagnosis = 'Resiko Tinggi Kesehatan Ibu'
st.success(resiko_kesehatan_ibu_diagnosis)