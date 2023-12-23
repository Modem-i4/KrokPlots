import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os

def list_files_and_folders(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                st.write("Папка:", entry.name)
                list_files_and_folders(entry.path)
            elif entry.is_file():
                st.write("Файл:", entry.name)

# Задати шлях до кореневого каталогу
root_path = "textures/chars/"

# Викликати функцію для кореневого каталогу
list_files_and_folders(root_path)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

