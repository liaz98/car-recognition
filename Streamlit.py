import streamlit as st
from PIL import Image
import random

st.header('Texnik pasporti orqali avtomobilning bozor narxini aniqlash')
def load_image(image_file):
	img = Image.open(image_file)
	return img
st.sidebar.subheader("Texnik passport rasmlarini tarafini yuklang")
uploaded_files  = st.sidebar.file_uploader("Upload Images", type=["png","jpg","jpeg"],accept_multiple_files=True)
if uploaded_files:
    st.text("Fayllar muvaffaqiyatli yuklandi")

for uploaded_file in uploaded_files:
    st.image(load_image(uploaded_file),width=300)

predicted_price = random.randrange(3000,5000,100)

# Add a selectbox to the sidebar:
yoqilgi = st.sidebar.selectbox(
    "Avtomobil yoqilg'i turini korsating",
    ('Benzin', 'Gaz', 'Dizel')
)
# Add a slider to the sidebar:
probeg = st.sidebar.number_input(
    "Bosib o'tgan masofasini kiriting"
)

if st.sidebar.button('Get prediction') and uploaded_files:
     st.write("Avtomobil modeli: Chevrolet Matiz")
     st.write("Bosib o'tgan masofasi:",probeg)
     st.write("Avtomobil rangi: Oq beliy")
     st.write("Avtomobil yoqilg'i turi: ",yoqilgi)
     st.write("Ishlab chiqarilgan yili: 2007")
     st.subheader(f"Avtomobilingizga tavsiya qilingan narx: {predicted_price} dollar")
else:
    st.subheader("Iltimos texpasportni yuklang!")
