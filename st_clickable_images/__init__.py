import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "clickable_images", url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "st_clickable_images", path=build_dir
    )


def clickable_images(paths, titles=[], div_style={}, img_style={}, key=None):
    component_value = _component_func(
        paths=paths,
        titles=titles,
        div_style=div_style,
        img_style=img_style,
        key=key,
        default=-1,
    )

    return component_value


if not _RELEASE:
    import streamlit as st

    clicked = clickable_images(
        [
            "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
            "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
            "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
            "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
            "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
        key="foo",
    )

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
