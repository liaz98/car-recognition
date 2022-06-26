import streamlit as st
from PIL import Image

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


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "Avtomobil yoqilg'i turini korsating",
    ('Benzin', 'Gaz', 'Dizel')
)
# Add a slider to the sidebar:
probeg = st.sidebar.number_input(
    "Bosib o'tgan masofasini kiriting"
)
st.write("Bosib o'tgan masofasi: ",probeg)


if st.sidebar.button('Get prediction'):
     st.write("Hozircha hech nima yo'q")
