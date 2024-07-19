import customtkinter as ctk
import requests

from src.widgets.c_label import CLabel
from src.utils.fetch_image import fetch_image
from src.constants.urls import Url
from src.widgets.c_button import CButton
from src.widgets.c_input_field import CInputField
from src.widgets.c_scrollable_frame import CScrollableFrame
from src.widgets.c_frame import CFrame
from src.constants.c_fonts import CFont
from src.utils.fetch_data import get_anime_info


class App(ctk.CTk):
    def fetch_anime_info(self):
        search_query = self.search_field.get().lower().replace(" ", "%20")

        response = requests.get(url=f"{Url.anime_name_url}/anime?q={search_query}")

        title, description, image_url = get_anime_info(response=response)

        self.anime_title.configure(state="normal")
        self.anime_title.delete(0, "end")
        self.anime_title.insert("end", title)
        self.anime_title.configure(state="readonly")

        self.description_text.configure(state="normal")
        self.description_text.delete(1.0, "end")
        self.description_text.insert(ctk.END, description)
        self.description_text.configure(state="disabled")

        self.anime_image.configure(
            image=fetch_image(url=image_url, image_size=(225, 309))
        )

    def __init__(
        self,
        title: str = "App",
        width: int = 400,
        height: int = 500,
        resizable: bool = True,
    ) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)

        # ? Custom functions

        #! search frame don't use
        self.search_frame = CFrame(self, fg_color="#191919", height=38)
        #! Main frame use it as a root window
        self.content_frame = CScrollableFrame(
            master=self, fg_color="#191919", orientation="vertical"
        )

        # ? Search query entry
        self.search_field = CInputField(
            master=self.search_frame,
            width=270,
            textvariable=None,
            font=CFont.font_med(),
            placeholder="Search",
        )
        # ? Search Button
        self.search_btn = CButton(
            master=self.search_frame,
            text="Go",
            font=CFont.font_med(),
            width=20,
            command=self.fetch_anime_info,
            fg_color=("#161616", "#5e55c8"),
            hover_color=("#151515", "#4138ab"),
            text_color=("black", "white"),
        )

        # ? content
        self.anime_title = CInputField(
            master=self.content_frame,
            textvariable=None,
            font=CFont.font_med(),
            fg_color="transparent",
            border_color="#191919",
            state="readonly",
            justify="center",
        )

        self.anime_image = CLabel(master=self.content_frame, text="")

        self.description_text = ctk.CTkTextbox(
            self.content_frame,
            state="disabled",
            height=150,
            fg_color="transparent",
            border_width=2,
            border_color="#191919",
            font=CFont.s_font_sm(),
            wrap="word",  # Add this line
        )

        # ? All Widgets packing
        self.search_field.place(x=0, y=0)
        self.search_btn.place(x=271, y=0)

        self.anime_title.pack(pady=10, fill="x")
        self.anime_image.pack()
        self.description_text.pack(fill="both", expand=True, pady=5)

        self.search_frame.pack(fill="x")
        self.content_frame.pack(fill="both", expand=True)
