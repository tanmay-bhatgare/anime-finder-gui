from typing import Tuple
import customtkinter as ctk


class CButton(ctk.CTkButton):
    def __init__(
        self,
        master: ctk.CTk,
        command,
        text: str = "CButton",
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] = None,
        text_color: str | Tuple[str, str] = "black",
        hover_color: str | Tuple[str, str] = None,
        height: int = 28,
        width: int = 100,
        font: ctk.CTkFont = None,
    ) -> None:
        super().__init__(
            master=master,
            text=text,
            height=height,
            width=width,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            command=command,
            font=font,
        )
