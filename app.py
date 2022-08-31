#Image to Pencil sketch app
#import libraries
import streamlit as st
import numpy as np
from PIL import Image
import cv2
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Convert Image To Pencil Sketch")
st.set_page_config(page_title="Image to Pencil Sketch",page_icon="👋")
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)
#convert into sketch
def pencilsketch(inp_image):
    image_gray = cv2.cvtColor(inp_image, cv2.COLOR_BGR2GRAY)
    image_invert = cv2.bitwise_not(image_gray)
    image_smoothing = cv2.GaussianBlur(image_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_image = dodgeV2(image_gray, image_smoothing)
    return(finalimage)
st.write("This Web App is to help convert your photos to realistic Pencil Sketches")
file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])
if file_image is None:
    st.write("You haven't uploaded any image file")
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_image))
    st.write("**Input Photo**")
    st.image(input_image, use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)
