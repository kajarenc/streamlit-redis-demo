import time
import streamlit as st
st.title("Streamlit Redis Demo")


@st.cache_data
def load_data(x):
    print("IN LOAD DATA!!!")
    time.sleep(0.5)
    return str(x).encode("utf-8") * (x * 100_000_000)


y = st.slider("Slider:", 1, 5, 1)

st.write(len(load_data(y)))
