import streamlit as st
import gradio as gr

gr.load("models/ZB-Tech/Text-to-Image").launch()

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
