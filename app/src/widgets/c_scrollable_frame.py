from typing import Literal
import customtkinter as ctk


class CScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(
        self,
        master: ctk.CTk,
        fg_color: str | None,
        width: int = 200,
        height: int = 200,
        bg_color: str = "transparent",
        orientation: Literal["vertical", "horizontal"] = "vertical",
        corner_radius: int = 0,
    ) -> None:
        super().__init__(
            master=master,
            fg_color=fg_color,
            width=width,
            height=height,
            bg_color=bg_color,
            orientation=orientation,
            corner_radius=corner_radius,
        )
