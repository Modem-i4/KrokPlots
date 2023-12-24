import os
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title="Крок емоційний!", page_icon="🌠", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        .centered-text {
            position: fixed;
            top: 80%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            width: 100%;
            z-index: 1;
            text-shadow: -2px -2px 0 #fff, 2px -2px 0 #fff, -2px 2px 0 #fff, 2px 2px 0 #fff;
            pointer-events: none;
            opacity: 0;
        }
        [data-testid=stImage] { 
            cursor: pointer;
        }
        .animated {
            animation: fade 1s;
        }

        @keyframes fade {
            0%, 100% {
                opacity: 0;
            }
            50% {
                opacity: 1;
            }
        }
    </style>
    <div class="centered-text" id="clipboard-anim">
        <h1>Скопійовано!</h1>
    </div>
""", unsafe_allow_html=True)

def list_folders(path):
    return [f.name for f in os.scandir(path) if f.is_dir()]

def list_files(path):
    return [f.name for f in os.scandir(path) if f.is_file()]

def display_cat_images(image_folder) :
    display_images(list_files(image_folder), image_folder)
    


def display_images(images, image_folder, captions = None):
    if not captions : captions = images 
    colsNumber = 2 if image_folder == 'textures\\bg' else 3 if image_folder == 'textures\\thoughts' else 5
    cols = st.columns(colsNumber)
    for i in range(0, len(images), colsNumber):
        for j in range(colsNumber):
            if i + j < len(images):
                image_path = os.path.join(image_folder, images[i + j])
                img_obj = Image.open(image_path)
                aspect_ratio = img_obj.width / img_obj.height
                target_width = int(300 * aspect_ratio)
                cols[j].image(img_obj, caption=captions[i + j], output_format="auto", width=target_width)


st.title("Крок вибіркових емоцій!")
st.sidebar.title("🌠 Крок до зірок")
selected_category = st.sidebar.selectbox("Обери категорію!", ["Всі персонажі", "Персонажі", "Фони", "Думки"])

translations = {"Фони": "bg", "Думки": "thoughts"}

chars_path = os.path.join("textures", "chars")
selected_chars = []
if selected_category == "Всі персонажі":
    chars = list_folders(chars_path)
    chars_urls = [os.path.join(char, f"{char}_default.png") for char in chars]
    display_images(chars_urls, chars_path, chars)

elif selected_category == "Персонажі":
    available_chars = list_folders(chars_path)

    st.sidebar.subheader("Обери персонажів:")
    for char in available_chars:
        selected = st.sidebar.checkbox(char)
        if selected:
            selected_chars.append(char)

    if not selected_chars:
        st.warning("Вік, вибери хоч одненького :)")
    else :
        st.header("Емоції обраних персонажів:")
        for char_folder in selected_chars:
            display_cat_images(os.path.join(chars_path, char_folder))
else:
    st.header(f"Зображення з {selected_category}")
    display_cat_images(os.path.join("textures", translations[selected_category]))


components.html("""<script>
    var images = parent.document.querySelectorAll('[data-testid=stImage]');
    
    function copyToClipboard(text) {
        var tempInput = document.createElement('input');
        tempInput.value = text;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
    }
    var animatedText = parent.document.getElementById('clipboard-anim');
    images.forEach(function(imgBlock) {
        imgBlock.addEventListener('click', function(e) {
            let caption = imgBlock.querySelector('[data-testid="caption"]').textContent.trim();
            copyToClipboard(caption);
            animatedText.classList.add('animated');
        });
    });
                
    animatedText.addEventListener('animationend', function() {
        animatedText.classList.remove('animated');
    });
        
</script>""")