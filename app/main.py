import streamlit as st
from streamlit_image_select import image_select

import uuid

from utils import generate_image
from utils import download_image
from utils import get_user_ip


def main():

    if "session_id" not in st.session_state:
        st.session_state.session_id = uuid.uuid4()

    if "session_ip" not in st.session_state:
        user_ip = get_user_ip()
        if user_ip:
            st.session_state.session_ip = user_ip
        else:
            st.error("Failed to fetch user IP address.")
        
    if "dream" not in st.session_state:
        st.session_state.dream = False

    if "img" not in st.session_state:
        st.session_state.img = ''

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

    st.markdown(f"<h5 style='text-align: center;'>User ip: {st.session_state.session_ip}</h5>", unsafe_allow_html=True)

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

if __name__ == "__main__":
    main()

    
    