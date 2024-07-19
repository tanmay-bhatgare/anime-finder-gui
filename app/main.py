from src.app import App


def main():
    app = App(title="Anime Finder", resizable=False, width=320, height=530)
    app.mainloop()


if __name__ == "__main__":
    main()
