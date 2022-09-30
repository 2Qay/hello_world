from PIL import Image
import streamlit as st
import dalle import create_and_show_images

st.title('2Qay dalle')

text = st.text_input("че хочешь нарисовать")
num_images = st.slider("сколько картинок надо??", 1, 4)

ok = st.button("нарисовать!!!")

if ok:
	create_and_show_images(text, num_images)



#image = Image.open('ssssss.jpg')
#st.write("ШРЕК")
#if st.button('Say hello', on_click):
#    st.image(image, caption = 'SHREEEEEEEEK')
#else:
#    st.write('Goodbye')

#agree = st.checkbox('Показать шрека?')
#if agree:
#    st.image(image, caption = 'SHREEEEEEEEK')
#else:
#    st.write('Нажми на квадратик')


