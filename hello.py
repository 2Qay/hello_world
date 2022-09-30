from PIL import Image
import streamlit as st
image = Image.open('ssssss.jpg')
st.write("ШРЕК")


#if st.button('Say hello', on_click):
#    st.image(image, caption = 'SHREEEEEEEEK')
#else:
#    st.write('Goodbye')

agree = st.checkbox('Показать шрека?')
if agree:
    st.image(image, caption = 'SHREEEEEEEEK')
else:
    st.write('Нажми на квадратик')
