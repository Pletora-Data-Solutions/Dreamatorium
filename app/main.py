import streamlit as st
from streamlit_image_select import image_select
import pyautogui

import uuid
import copy

from utils import generate_image
from utils import download_image

st.markdown("""
<style>
    textarea[rows="1"] {
        height: auto;
    }
    button[title="View fullscreen"]{
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit app title
st.title("Dreamatorium :comet:")
st.markdown('---')

# # Input prompt
st.markdown("<h5 style='text-align: center;'>What is on your mind?</h5>", unsafe_allow_html=True)
st.text_area("", height=100, key='input', help='')

st.session_state.session_id = uuid.uuid4()
    
if "dream" not in st.session_state:
    st.session_state.dream = False

if "img" not in st.session_state:
    st.session_state.img = ''

if st.button("Dream"):
    if st.session_state.input != "" and "prompt" not in st.session_state:
        st.session_state.prompt = st.session_state['input']
        st.session_state.generated = generate_image(st.session_state.prompt)
        st.session_state.dream = True
    elif st.session_state.input != "" and st.session_state['input'] != st.session_state.prompt:
        st.session_state.prompt = st.session_state['input']
        st.session_state.generated = generate_image(st.session_state.prompt)
    else:
        st.error("Provide Input to Dream")

if "generated" in st.session_state and st.session_state.dream == True:
    st.session_state.img = image_select("", st.session_state.generated) #Implement on streamlit-image-select index = None test
    if st.session_state.img != '':
        try:
            st.image(st.session_state.img, use_column_width=True, output_format="JPEG")
            if st.button("Download"):
                if st.session_state.img != '':
                    download_image(st.session_state.img, str(st.session_state.session_id))
                else:
                    st.error("No image selected to download")
        except Exception as e:
            st.error(e)

    
    