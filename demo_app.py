import time
import streamlit as st
st.title("Streamlit Redis Demo")


@st.cache_data
def square(x):
    print("IN SQUARE!!!")
    time.sleep(0.5)
    return str(x).encode("utf-8") * (x * 100_000_000)


y = st.slider("Slider:", 1, 5, 1)

st.write(len(square(y)))
