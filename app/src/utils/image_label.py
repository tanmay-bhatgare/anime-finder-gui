import io
from typing import Tuple
import requests
from PIL import Image
import customtkinter as ctk


def image_label(master, url, image_size: Tuple[int, int]) -> ctk.CTkImage:
    response = requests.get(url)
    response.raise_for_status()

    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)

    photo = ctk.CTkImage(image, size=(image_size[0], image_size[1]))

    return ctk.CTkLabel(master=master, image=photo, text="")
