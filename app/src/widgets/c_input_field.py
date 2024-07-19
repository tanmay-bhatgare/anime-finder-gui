import customtkinter as ctk
from typing import Optional, Callable


class CInputField(ctk.CTkEntry):
    def __init__(
        self,
        master: ctk.CTk,
        textvariable: ctk.StringVar,
        font: ctk.CTkFont,
        placeholder: str = "",
        fg_color: str = None,
        border_color: str = None,
        width: int = 140,
        height: int = 28,
        validatecommand: Optional[Callable] = None,
        state: str = "normal",
        justify: str = "right",
    ) -> None:
        kwargs = {
            "master": master,
            "state": state,
            "width": width,
            "height": height,
            "textvariable": textvariable,
            "font": font,
            "justify": justify,
            "validate": "key",
            "placeholder_text": placeholder,
            "fg_color": fg_color,
            "border_color": border_color,
        }
        if validatecommand:
            kwargs["validatecommand"] = validatecommand

        super().__init__(**kwargs)
