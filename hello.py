from PIL import Image
import streamlit as st
image = Image.open('ssssss.jpg')
st.write("ШРЕК")


if st.button('Say hello', on_click):
    st.image(image, caption = 'SHREEEEEEEEK')
else:
    st.write('Goodbye')


