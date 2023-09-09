import streamlit as st
from text_extraction import load_file, extract_text


st.title("Handwritten-to-Text Convertor")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    with st.status("Extracting text..."):
        img = load_file(uploaded_file)
        data = extract_text(img)[0]

    st.subheader("Extracted text:", divider="grey")
    st.text(data)
    st.download_button(
        label="Download",
        data=data,
        file_name='result.text',
        mime='text',
    )