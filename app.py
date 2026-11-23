import streamlit as st

st.set_page_config(
    page_title="Ask your CSV",
    page_icon= "📊",
    layout="wide"
)

st.title("Ask your CSV")
st.markdown("Upload your data and ask questions in plain English!")

#Sidebar for file upload
with st.sidebar:
    st.header("Data Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])