import requests

def get_anime_info(response: requests.Response):
    try:
        data = response.json().get("data", [])
        if not data:
            return None
        # ? anime name section
        title: str = data[0].get("title_english")

        # ? anime description section
        description: str = data[0].get("synopsis")

        # ? images section
        images = data[0].get("images", {})
        jpg = images.get("jpg", {})
        image_url: str = jpg.get("image_url")

        return title, description, image_url
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error accessing image URL: {e}")
        return None