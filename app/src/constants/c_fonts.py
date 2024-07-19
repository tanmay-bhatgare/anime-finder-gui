import customtkinter as ctk


class CFont:
    @staticmethod
    def font_small() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=18, weight="bold")

    @staticmethod
    def font_med() -> ctk.CTkFont:
        return ctk.CTkFont(family="Courier", size=25, weight="bold")

    @staticmethod
    def font_large() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=35, weight="bold")

    @staticmethod
    def font_xl() -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=46, weight="bold")

    @staticmethod
    def s_font_sm() -> ctk.CTkFont:
        return ctk.CTkFont(family="Courier", size=20, weight="bold")
