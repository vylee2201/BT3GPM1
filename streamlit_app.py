import streamlit as st
import pandas as pd

st.title("📂 Upload File App")

uploaded_file = st.file_uploader("Chọn một file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Xem trước dữ liệu:")
    st.dataframe(df)
