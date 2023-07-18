import streamlit as st
from streamlit_image_select import image_select
import pyautogui

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
    
if "dream" not in st.session_state:
    st.session_state.dream = False

if "img" not in st.session_state:
    st.session_state.img = ''

if st.button("Dream"):
    st.session_state.dream = True

if st.session_state != "":
    if "generated" not in st.session_state and st.session_state.dream == True:
        prompt = st.session_state['input']
        st.session_state.generated = generate_image(prompt)

    if "generated" in st.session_state and st.session_state.dream == True:
        st.session_state.img = image_select("", st.session_state.generated) #Implement on streamlit-image-select index = None test
        if st.session_state.img != '':
            try:
                st.image(st.session_state.img, use_column_width=True, output_format="JPEG")
                col1, col2 = st.columns([1,1])
                if col2.button("Forget"):
                    pyautogui.hotkey("ctrl","F5")
                if col1.button("Download"):
                    if st.session_state.img != '':
                        download_image(st.session_state.img)
                    else:
                        st.error("No image selected to download")
            except:
                st.error("Could not show image")
else:
    st.error("Input needed to dream.")
    
    