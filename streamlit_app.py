import os
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from st_clickable_images import clickable_images
import js2py 
  
#res_2 = js2py.eval_js("$('*').click(()=>{console.log('BLYAAA')})") 


def list_folders(path):
    return [f.name for f in os.scandir(path) if f.is_dir()]

def list_files(path):
    return [f.name for f in os.scandir(path) if f.is_file()]

def on_image_click(image_path):
    st.write(f"Clicked on image: {image_path}")

def display_images(image_folder):
    captions = list_files(image_folder)
    captions
    images = ["/"+image_folder+"/"+img for img in captions]
    images = ["\\"+os.path.join(image_folder,img) for img in captions]
    images
    clicked = clickable_images(
        images,
        titles=captions,
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )
    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
    # for i in range(0, len(images), 5):
    #     cols = st.columns(5)
    #     for j in range(5):
    #         if i + j < len(images):
    #             image_path = os.path.join(image_folder, images[i + j])
    #             img_obj = Image.open(image_path)
    #             aspect_ratio = img_obj.width / img_obj.height
    #             target_width = int(300 * aspect_ratio)
    #             cols[j].image(img_obj, caption=images[i + j], output_format="auto", width=target_width)



def copy_caption_callback(caption):
    def callback():
        st.success(f"Caption '{caption}' copied!")
    return callback


st.title("File Explorer with Streamlit")

# Вибрати категорію
selected_category = st.sidebar.selectbox("Select a category", ["bg", "chars", "thoughts"])

if selected_category == "chars":
    # Вибрати папку персонажа
    chars_path = os.path.join("textures", "chars")
    available_chars = list_folders(chars_path)

    # Відобразити чекбокси для кожного персонажа
    st.sidebar.subheader("Select characters:")
    selected_chars = []
    for char in available_chars:
        selected = st.sidebar.checkbox(char)
        if selected:
            selected_chars.append(char)

    if not selected_chars:
        st.warning("Please select at least one character.")
    else :
        st.header("Images for Selected Characters")
        for char_folder in selected_chars:
            display_images(os.path.join(chars_path, char_folder))
else:
    # Відобразити зображення для обраної категорії (bg або thoughts)
    st.header(f"Images for {selected_category}")
    display_images(os.path.join("textures", selected_category))


# components.html("""<script>
#     var images = parent.window.querySelectorAll('img');
#     console.log(images);
#     images.forEach(function(img) {
#         img.addEventListener('click', function() {
#             console.log("BLYAAA");
#         });
#     });
# </script>""")